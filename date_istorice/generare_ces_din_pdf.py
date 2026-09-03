"""Extrage praguri CES agregate din listele anonimizate ISMB (2024/2025/2026).

IMPORTANT: produce DOAR agregate (prag minim, număr de admiși per școală×specializare)
și statistici pe an. NU salvează niciun rând individual de candidat.
"""
import json
import re

import fitz

ANI = {"2024": "_ces2024.pdf", "2025": "_ces2025.pdf", "2026": "_ces2026.pdf"}

RE_COD = re.compile(r"^(?:B|IF|[A-Z]{2})\d{3,}$")
RE_JUD = re.compile(r"/\s*(?:B|IF|[A-Z]{2})\s*$")
RE_NIV = re.compile(r"^(?:LIC|PRO|-)\s*/\s*")
RE_NUM = re.compile(r"^\d{1,2},\d{2}$")


def curata_spec(s):
    s = re.sub(r"\s*/\s*Limba\s+\w+\s*/\s*-?\s*$", "", s)
    s = re.sub(r"\s*/\s*-\s*$", "", s)
    return re.sub(r"\s+", " ", s).strip()


def parseaza(cale):
    doc = fitz.open(cale)
    linii = []
    for p in doc:
        linii += [l.strip() for l in p.get_text().split("\n")]
    doc.close()
    linii = [l for l in linii if l]

    # marchează începuturile de înregistrare: un număr, urmat de un cod
    start = [i for i in range(len(linii) - 1)
             if re.fullmatch(r"\d{1,4}", linii[i]) and RE_COD.match(linii[i + 1])]

    inreg = []
    for k, i in enumerate(start):
        j = start[k + 1] if k + 1 < len(start) else len(linii)
        bloc = linii[i:j]
        if len(bloc) < 6:
            continue

        # ultimele trei valori numerice = media admitere / evaluare / V-VIII
        nums = [x for x in bloc if RE_NUM.match(x)]
        if not nums:
            continue
        media_adm = float(nums[0].replace(",", "."))

        # Sfârșitul școlii de proveniență = marcajul de județ. Apare fie ca „... / B"
        # la capătul liniei, fie — când numele școlii se rupe pe rânduri — ca o linie
        # separată care conține doar „B" / „IF", precedată de o linie terminată în „/".
        i_jud = None
        for x in range(2, len(bloc)):
            if RE_JUD.search(bloc[x]):
                i_jud = x
                break
            if re.fullmatch(r"(?:B|IF|[A-Z]{2})", bloc[x]) and bloc[x - 1].rstrip().endswith("/"):
                i_jud = x
                break
        if i_jud is None:
            continue
        # câmpul Niv/formă („LIC / Z" sau „- / -")
        i_niv = next((x for x in range(i_jud + 1, len(bloc)) if RE_NIV.match(bloc[x])), None)
        if i_niv is None:
            continue

        liceu = " ".join(bloc[i_jud + 1:i_niv]).strip()
        profil = bloc[i_niv + 1] if i_niv + 1 < len(bloc) else ""
        # specializarea: între profil și prima valoare numerică
        i_num = next((x for x in range(i_niv + 2, len(bloc)) if RE_NUM.match(bloc[x])), len(bloc))
        spec = curata_spec(" ".join(bloc[i_niv + 2:i_num]))

        inreg.append({"liceu": re.sub(r"\s+", " ", liceu),
                      "profil": profil, "spec": spec, "media": media_adm})
    return inreg


rezultat = {}
for an, f in ANI.items():
    recs = parseaza(f)
    nerep = [r for r in recs if "NEREPARTIZAT" in r["liceu"].upper()]
    adm = [r for r in recs if "NEREPARTIZAT" not in r["liceu"].upper() and r["liceu"]]

    grup = {}
    for r in adm:
        cheie = "%s || %s" % (r["liceu"], r["spec"])
        g = grup.setdefault(cheie, {"liceu": r["liceu"], "specializare": r["spec"],
                                    "profil": r["profil"], "medii": []})
        g["medii"].append(r["media"])

    praguri = {}
    for cheie, g in grup.items():
        praguri[cheie] = {
            "liceu": g["liceu"], "specializare": g["specializare"], "profil": g["profil"],
            "prag_ces": round(min(g["medii"]), 2),       # ultima medie admisă
            "media_max": round(max(g["medii"]), 2),
            "nr_admisi": len(g["medii"]),
        }

    rezultat[an] = {
        "total_candidati": len(recs),
        "admisi": len(adm),
        "nerepartizati": len(nerep),
        "rata_plasare_%": round(100.0 * len(adm) / len(recs), 1) if recs else None,
        "nr_scoli_x_spec": len(praguri),
        "praguri": praguri,
    }
    print("%s: %d candidați | %d admiși | %d nerepartizați (%.1f%% plasare) | %d combinații școală×spec"
          % (an, len(recs), len(adm), len(nerep),
             100.0 * len(adm) / len(recs) if recs else 0, len(praguri)))

with open("ces_praguri_2024_2025_2026.json", "w", encoding="utf-8") as f:
    json.dump(rezultat, f, ensure_ascii=False, indent=1)
print("\nSalvat ces_praguri_2024_2025_2026.json (doar agregate, fără rânduri individuale)")
