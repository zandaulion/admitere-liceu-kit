# SPDX-License-Identifier: GPL-3.0-or-later
"""Offline checks using synthetic records; never fetch applicant data."""
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
import unittest
import zipfile

import fitz
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripturi" / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


pack = module("pachet")
ranking = module("ierarhie")
simulation = module("simulare_repartizare")
brochure = module("parse_brosura")


class StarterTests(unittest.TestCase):
    def test_archive_allowlist_manifest_and_reproducibility(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            src = temp / "source"
            for name in pack.FILES:
                dest = src / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, dest)
            (src / "private-notes.txt").write_text("SYNTHETIC MUST NOT SHIP")
            first, digest = pack.build(src, temp / "one", "a" * 40)
            second, other = pack.build(src, temp / "two", "a" * 40)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            self.assertEqual(digest, other)
            with zipfile.ZipFile(first) as z:
                self.assertIsNone(z.testzip())
                names = {n.removeprefix(pack.PREFIX + "/") for n in z.namelist()}
                self.assertEqual(names, set(pack.FILES) | {"RELEASE.json", "MANIFEST.sha256"})
                manifest = z.read(pack.PREFIX + "/MANIFEST.sha256").decode()
                for line in manifest.splitlines():
                    expected, name = line.split("  ", 1)
                    self.assertEqual(expected, hashlib.sha256(z.read(pack.PREFIX + "/" + name)).hexdigest())

    def test_archive_rejects_symlink_and_invalid_revision(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            (temp / "README.md").symlink_to(ROOT / "README.md")
            with self.assertRaisesRegex(ValueError, "symlink"):
                pack.build(temp, temp / "output", "a" * 40)
            with self.assertRaisesRegex(ValueError, "revision"):
                pack.build(ROOT, temp / "output", "not-a-revision")

    def test_all_local_document_links_resolve_in_pack(self):
        class Links(HTMLParser):
            def __init__(self):
                super().__init__()
                self.links = []

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                for key in ("href", "src"):
                    if key in attrs:
                        self.links.append(attrs[key])
                if tag in {"script", "iframe", "form"}:
                    raise AssertionError("unexpected active content")

        files = set(pack.FILES)
        for name in files:
            if name.endswith(".md"):
                links = re.findall(r"\]\(([^)]+)\)", (ROOT / name).read_text())
            elif name.endswith(".html"):
                parser = Links()
                parser.feed((ROOT / name).read_text())
                links = parser.links
            else:
                continue
            for link in links:
                if ":" in link or link.startswith("#"):
                    continue
                dest = ((ROOT / name).parent / link.split("#")[0]).resolve()
                relative = dest.relative_to(ROOT).as_posix()
                self.assertTrue(relative in files or any(f.startswith(relative + "/") for f in files), (name, link))

    def test_historical_aggregate_shapes_and_ranges(self):
        data = json.loads((ROOT / "date_istorice/praguri_2025_din_brosura2026.json").read_text())
        self.assertEqual(len(data), 405)
        for code, row in data.items():
            self.assertRegex(code, r"^\d{3}$")
            self.assertEqual(set(row), {"liceu", "specializare", "clase", "locuri", "locuri_romi", "locuri_ces", "prag_2025"})
            for key in ("clase", "locuri", "locuri_romi", "locuri_ces"):
                if key in {"clase", "locuri"} or row[key] is not None:
                    self.assertGreaterEqual(row[key], 0)
            if row["prag_2025"] is not None:
                self.assertTrue(0 <= row["prag_2025"] <= 10)
        anchors = json.loads((ROOT / "date_istorice/ierarhie_ancore_2025_2026.json").read_text())
        for year, count in (("2025", 93), ("2026", 84)):
            a = anchors[year]
            self.assertEqual(len(a), count)
            self.assertTrue(all(0 <= grade <= 10 and rank >= 1 for rank, grade in a))
            self.assertTrue(all(x[0] < y[0] and x[1] >= y[1] for x, y in zip(a, a[1:])))
        ces = json.loads((ROOT / "date_istorice/ces_praguri_2024_2025_2026.json").read_text())
        for row in ces.values():
            self.assertEqual(set(row), {"total_candidati", "admisi", "nerepartizati", "rata_plasare_%", "nr_scoli_x_spec", "praguri"})
            self.assertEqual(row["total_candidati"], row["admisi"] + row["nerepartizati"])
            self.assertEqual(row["nr_scoli_x_spec"], len(row["praguri"]))
            self.assertEqual(row["admisi"], sum(v["nr_admisi"] for v in row["praguri"].values()))
            for group in row["praguri"].values():
                self.assertEqual(set(group), {"liceu", "specializare", "profil", "prag_ces", "media_max", "nr_admisi"})
                self.assertTrue(0 <= group["prag_ces"] <= group["media_max"] <= 10)

    def test_interpolation_and_boundaries(self):
        anchors = [[1, 10.0], [101, 8.0], [201, 6.0]]
        self.assertEqual(ranking.nota_la_pozitie(anchors, 51), 9.0)
        self.assertEqual(ranking.pozitie_la_nota(anchors, 9.0), 51)
        self.assertEqual(ranking.nota_la_pozitie(anchors, 1000), 6.0)
        self.assertEqual(ranking.pozitie_la_nota(anchors, 11), 1)

    def test_simulation_respects_preference_capacity_and_exhaustion(self):
        cap = np.array([1, 1])
        base = np.array([8.0, 8.0])
        new = np.array([False, False])
        for seed in range(50):
            result = simulation.o_simulare(cap, base, new, 1, [1, 0], 0.2, np.random.default_rng(seed))
            self.assertEqual(result, 1)
            result = simulation.o_simulare(cap, base, new, 3, [0, 1], 0.2, np.random.default_rng(seed))
            self.assertEqual(result, -1)
        np.testing.assert_array_equal(cap, [1, 1])

    def test_pdf_extraction_on_synthetic_brochure(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "synthetic.pdf"
            with fitz.open() as doc:
                page = doc.new_page()
                page.insert_text((50, 50), "Filiera\nLICEUL DEMO ALFA\nSpecializare demonstrativa\n1\n28\n1\n1\n8,00\nNu\n101")
                doc.save(path)
            data = brochure.parseaza(path)
            self.assertEqual(set(data), {"101"})
            self.assertEqual(data["101"]["scoala"], "LICEUL DEMO ALFA")
            self.assertEqual(data["101"]["total"], 28)
            self.assertEqual(data["101"]["media"], 8.0)


if __name__ == "__main__":
    unittest.main()
