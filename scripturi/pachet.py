#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Build the reviewed starter pack from an explicit list, never a directory scan."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile

EDITION = "2026-10-21"
PREFIX = "Admitere-Liceu-Kit-" + EDITION
FILES = (
    "README.md", "START.html", "00_CITESTE_MAI_INTAI.md",
    "01_PROMPT_COMPLET_PENTRU_AI.md", "02_ANUL_PREGATITOR.md",
    "SURSE_2027.md", "DISTRIBUTIE.md", "SCRIPTURI.md", "LICENSE", "SECURITY.md",
    "requirements.txt", "modele/README.md", "modele/optiuni.csv",
    "modele/termene.csv", "modele/coduri-demo.json", "modele/fisa-demo.json",
    "date_istorice/README.md", "date_istorice/praguri_2025_din_brosura2026.json",
    "date_istorice/ierarhie_ancore_2025_2026.json",
    "date_istorice/ces_praguri_2024_2025_2026.json",
    "scripturi/ierarhie.py", "scripturi/parse_brosura.py",
    "scripturi/simulare_repartizare.py", "scripturi/pachet.py",
    "tests/test_starter.py",
)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def build(root, output, revision):
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("revision must be the full lowercase Git commit SHA")
    root = Path(root).resolve()
    payload = {}
    for name in FILES:
        path = root / name
        # Reject symlinks at any level, including paths that point inside the tree.
        parts = [root.joinpath(*Path(name).parts[:i])
                 for i in range(1, len(Path(name).parts) + 1)]
        if any(part.is_symlink() for part in parts):
            raise ValueError("symlink is not a release input: " + name)
        data = path.read_bytes()
        data.decode("utf-8")
        payload[name] = data
    payload["RELEASE.json"] = (json.dumps({
        "edition": EDITION,
        "source_repository": "https://github.com/zandaulion/admitere-liceu-kit",
        "source_revision": revision,
        "original_code_and_docs_license": "GPL-3.0-or-later",
    }, indent=2, sort_keys=True) + "\n").encode()
    payload["MANIFEST.sha256"] = "".join(
        sha256(data) + "  " + name + "\n"
        for name, data in sorted(payload.items())
    ).encode()
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    archive = output / (PREFIX + ".zip")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED,
                         compresslevel=9) as z:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(PREFIX + "/" + name, (2026, 10, 21, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data, compresslevel=9)
    digest = sha256(archive.read_bytes())
    (output / "SHA256SUMS").write_text(digest + "  " + archive.name + "\n")
    return archive, digest


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True)
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    archive, digest = build(Path(__file__).resolve().parents[1], args.output,
                            args.revision)
    print(archive.name + "  " + digest)
