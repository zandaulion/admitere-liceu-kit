#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Refresh school-level BAC aggregates from PlusEdu's labelled public table.

Never ingest candidate or class rows. The existing school list is the input;
unsourced schools fail the run instead of retaining old values silently.
"""

import argparse
from datetime import date
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import time
import unicodedata
from urllib.parse import urlsplit, urlunsplit
from urllib.request import Request, urlopen

SOURCE_HOSTS = {"www.bacplus.ro", "bacplus.ro", "www.plusedu.ro", "plusedu.ro"}
HEADERS = ["", "Medie Admitere", "Medie Bac", "Poziție Națională Bac", "Elevi Bac", "Rată de promovare"]
YEARS = set(range(2018, 2027))


class SchoolTable(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self.in_title = False
        self.tables = []
        self.table = None
        self.row = None
        self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "h1" and self.title is None:
            self.title, self.in_title = "", True
        elif tag == "table":
            self.table = []
        elif tag == "tr" and self.table is not None:
            self.row = []
        elif tag in ("th", "td") and self.row is not None:
            self.cell = ""

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.cell is not None:
            self.cell += data

    def handle_endtag(self, tag):
        if tag == "h1":
            self.in_title = False
        elif tag in ("th", "td") and self.cell is not None:
            self.row.append(" ".join(self.cell.split()))
            self.cell = None
        elif tag == "tr" and self.row is not None:
            self.table.append(self.row)
            self.row = None
        elif tag == "table" and self.table is not None:
            self.tables.append(self.table)
            self.table = None


def normalize(value):
    value = value.translate(str.maketrans("ăâîșşțţ", "aaisstt"))
    value = unicodedata.normalize("NFKD", value.casefold())
    value = "".join(c for c in value if not unicodedata.combining(c))
    return " ".join(re.findall(r"[a-z0-9]+", value))


def slugs(school):
    value = normalize(school).replace(" ", "-")
    return [value, value + "-bucuresti"]


def decimal(value, maximum, percent=False):
    value = value.strip()
    if percent:
        if not value.endswith("%"):
            raise ValueError("pass rate lacks percent sign: " + value)
        value = value[:-1]
    value = value.replace(",", ".")
    if not re.fullmatch(r"\d+(?:\.\d{1,2})?", value):
        raise ValueError("invalid decimal: " + value)
    number = float(value)
    if not 0 <= number <= maximum:
        raise ValueError("number outside valid range: " + value)
    return value


def extract(html, expected_school):
    parser = SchoolTable()
    parser.feed(html)
    if normalize(parser.title or "") != normalize(expected_school):
        raise ValueError("page title does not match school: " + repr(parser.title))
    matches = [table for table in parser.tables if table and table[0] == HEADERS]
    if len(matches) != 1:
        raise ValueError("expected one BAC history table with exact headings")
    history = {}
    for row in matches[0][1:]:
        if len(row) != len(HEADERS) or not re.fullmatch(r"20\d{2}", row[0]):
            raise ValueError("invalid BAC history row")
        year = int(row[0])
        if year not in YEARS:
            continue
        if str(year) in history:
            raise ValueError("duplicate year " + str(year))
        history[str(year)] = {
            "medie_bac": decimal(row[2], 10),
            "promovare_%": decimal(row[5], 100, percent=True),
        }
    if not history or "2026" not in history:
        raise ValueError("missing 2026 or entire BAC history")
    return dict(sorted(history.items(), reverse=True))


def fetch(school):
    failures = []
    for slug in slugs(school):
        url = "https://www.bacplus.ro/i/" + slug
        for attempt in range(3):
            try:
                with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=25) as response:
                    final_url = response.url
                    if urlsplit(final_url).hostname not in SOURCE_HOSTS:
                        raise ValueError("redirected outside expected source hosts")
                    html = response.read().decode("utf-8")
                history = extract(html, school)
                final = urlsplit(final_url)
                source_url = urlunsplit((final.scheme, final.netloc, final.path, "", ""))
                return history, source_url
            except (OSError, UnicodeError, ValueError) as error:
                failures.append(slug + ": " + str(error)[:180])
                if attempt < 2:
                    time.sleep(1 + attempt)
        time.sleep(0.5)
    raise ValueError("; ".join(failures))


def refresh(existing):
    result, provenance, errors = {}, {}, {}
    for index, school in enumerate(sorted(existing), 1):
        try:
            history, url = fetch(school)
            result[school] = history
            provenance[school] = url
        except ValueError as error:
            errors[school] = str(error)
        print(f"{index}/{len(existing)} {school}: {len(result.get(school, {}))} years", flush=True)
        time.sleep(0.4)
    return result, provenance, errors


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--existing", type=Path, default=Path(__file__).with_name("bac_istoric_licee.json"))
    cli.add_argument("--output", type=Path, required=True)
    cli.add_argument("--provenance", type=Path, required=True)
    cli.add_argument("--errors", type=Path, required=True)
    args = cli.parse_args()
    existing = json.loads(args.existing.read_text(encoding="utf-8"))
    result, sources, errors = refresh(existing)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.provenance.write_text(json.dumps({"checked_on": date.today().isoformat(), "source": "PlusEdu/BacPlus public school-level BAC tables", "schools": sources}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.errors.write_text(json.dumps(errors, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Verified {len(result)}/{len(existing)} schools; {len(errors)} unresolved")
    if errors:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
