#!/usr/bin/env python3
"""
Parsează planul de școlarizare din broșura ISMB (PDF cu strat de text).

Rezultat: un dicționar cod -> {scoala, specializare, clase, total, romi, ces, media}
salvat ca JSON.

Testat pe broșura București 2026-2027 (405 coduri extrase).
Structura tabelului se poate schimba de la an la an — VALIDEAZĂ rezultatul
(vezi funcția `valideaza`) înainte de a-l folosi.

Rulare:
    python parse_brosura.py BROSURA_ADMITERE_2027.pdf coduri_2027.json

Dependențe: PyMuPDF  (pip install pymupdf)
"""
import json
import re
import sys

import fitz  # PyMuPDF


def _num(s):
    """'6,70' -> 6.70 ; '' / None -> None"""
    s = (s or "").strip().replace(",", ".")
    if not s:
        return None
    m = re.fullmatch(r"\d+(?:\.\d+)?", s)
    return float(m.group()) if m else None


def _e_nume_scoala(s):
    """Rândurile-antet cu numele liceului sunt scrise (aproape) integral cu majuscule."""
    if not s or "Filiera" in s:
        return False
    litere = [c for c in s if c.isalpha()]
    if len(litere) < 4:
        return False
    return sum(1 for c in litere if c.isupper()) / len(litere) > 0.8


def parseaza(cale_pdf):
    """
    Citește PDF-ul linie cu linie. Un rând de specializare se termină cu codul de
    3 cifre; valorile numerice îl preced, în ordine inversă:

        ... specializare ... | clase | total | romi | ces | media | [Dual] | COD

    Coloana 'Dual' poate lipsi, de aceea se detectează prefixul 'Nu'/'Da'.
    """
    doc = fitz.open(cale_pdf)
    date = {}

    for pagina in doc:
        text = pagina.get_text()
        if "Filiera" not in text:
            continue
        linii = text.split("\n")

        scoala = ""
        bloc, ultim_idx = [], -99

        for i, linie_bruta in enumerate(linii):
            linie = linie_bruta.strip()

            # --- rând-antet cu numele liceului (poate fi rupt pe mai multe linii)
            if not re.match(r"^\s*(?:Nu|Da)?\s*\d{3}(?:\s|$)", linie_bruta) and _e_nume_scoala(linie):
                bloc = bloc + [linie] if i == ultim_idx + 1 else [linie]
                ultim_idx = i
                scoala = " ".join(bloc)
                continue

            # --- rând de specializare: se termină cu codul
            m = re.match(r"^\s*(Nu|Da)?\s*(\d{3})(?:\s|$)", linie_bruta)
            if not m:
                continue
            cod = m.group(2)
            if not (100 <= int(cod) <= 999):
                continue

            offset = 1 if m.group(1) else 2      # sare peste coloana Dual dacă există
            try:
                media = _num(linii[i - offset])
                ces = _num(linii[i - offset - 1])
                romi = _num(linii[i - offset - 2])
                total = _num(linii[i - offset - 3])
                clase = _num(linii[i - offset - 4])
            except IndexError:
                continue
            if total is None or clase is None:
                continue

            # --- numele specializării: liniile de text de dinaintea numerelor
            spec, j = "", i - offset - 5
            while j >= 0 and len(spec) < 180:
                t = linii[j].strip()
                if not t or re.fullmatch(r"[\d.,]+", t) or _e_nume_scoala(t):
                    break
                spec = (t + " " + spec).strip()
                j -= 1
            spec = re.sub(r"^(?:Nu|Da)?\s*\d{3}\s*", "", spec)

            date[cod] = {
                "scoala": scoala,
                "specializare": spec,
                "clase": clase,
                "total": total,      # locuri runda generală
                "romi": romi,
                "ces": ces,          # locuri CES (SUPLIMENTARE)
                "media": media,      # pragul anului precedent, runda GENERALĂ
                "pagina": pagina.number + 1,
            }

    doc.close()
    return date


def valideaza(date):
    """Verificări obligatorii. O 'gaură' în coduri = pagină neparsată, NU cod inexistent."""
    chei = sorted(int(k) for k in date)
    print("Coduri extrase: %d  (interval %d–%d)" % (len(chei), chei[0], chei[-1]))

    lipsa = [i for i in range(chei[0], chei[-1] + 1) if i not in chei]
    serii = []
    for g in lipsa:
        if serii and g == serii[-1][-1] + 1:
            serii[-1].append(g)
        else:
            serii.append([g])

    if serii:
        print("\n⚠️  Coduri lipsă: %d" % len(lipsa))
        for s in serii:
            print("   ", s[0] if len(s) == 1 else "%d–%d" % (s[0], s[-1]))
        print("\n   Seriile LUNGI si CONTINUE sunt aproape sigur pagini neparsate.")
        print("   Caută-le manual în PDF si adaugă-le, NU presupune că nu există.")
    else:
        print("✓ Fără găuri în secvența de coduri.")

    fara_media = [k for k, v in date.items() if v["media"] is None]
    print("\nSpecializări fără prag anul precedent (NOI): %d" % len(fara_media))
    print("Total locuri (runda generală): %d" % sum(v["total"] or 0 for v in date.values()))
    print("Total locuri CES (suplimentare): %d" % sum(v["ces"] or 0 for v in date.values()))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    rezultat = parseaza(sys.argv[1])
    valideaza(rezultat)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump(rezultat, f, ensure_ascii=False, indent=1)
    print("\nSalvat în %s" % sys.argv[2])
    print("\n⚠️  NU UITA: aplică ERATA la broșură peste aceste date!")
