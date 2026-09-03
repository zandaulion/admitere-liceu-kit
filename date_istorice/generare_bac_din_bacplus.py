"""Descarcă istoricul BAC (toți anii disponibili) pentru liceele din București, de pe bacplus.ro.

Sursa listei de licee: praguri_2025_din_brosura2026.json (broșura ISMB 2026).
Rezultat: bac_istoric_licee.json  ->  liceu -> an -> {medie_bac, promovare_%}

Datele sunt publice și agregate la nivel de școală. Nu conțin nimic individual.
"""
import json
import re
import time
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
DIA = str.maketrans("ăâîșşțţĂÂÎȘŞȚŢ", "aaisstt" "aaisstt")


def slugs(nume):
    s = nume.replace("„", "").replace("”", "").replace('"', "")
    s = s.replace(".", " ").replace("-", " ").replace("*", " ")
    s = s.translate(DIA).lower()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", "-", s.strip())
    return [s, s + "-bucuresti"]


def get(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8", "ignore") if r.status == 200 else None
    except Exception:
        return None


def ani(html):
    """Extrage tabelul An | Medie Admitere | Medie Bac | Poziție | Elevi | Rată."""
    t = re.sub(r"(?s)<script.*?</script>", " ", html)
    t = re.sub(r"<[^>]+>", "|", t)
    m = re.search(r"Rat[ăa] de promovare(.*?)(Statisticile|Admitere specializ)", t)
    if not m:
        return None
    seq = [x.strip() for x in m.group(1).split("|") if x.strip()]
    out, i = {}, 0
    while i < len(seq):
        if re.fullmatch(r"20\d\d", seq[i]):
            an, bloc = seq[i], seq[i + 1:i + 7]
            # Poziția națională = primul întreg >= 100 (poate avea separator de mii).
            # Medie Bac = valoarea imediat dinaintea ei.
            poz_k = None
            for k, x in enumerate(bloc):
                xi = x.replace(".", "").replace(",", "")
                if re.fullmatch(r"\d+", xi) and int(xi) >= 100 and "," not in x:
                    poz_k = k
                    break
            medie = bloc[poz_k - 1].replace(",", ".") if poz_k and poz_k >= 1 else None
            pct = None
            for k, x in enumerate(bloc):
                if x == "%" and k > 0:
                    pct = bloc[k - 1].replace(",", ".")
                    break
            out[an] = {"medie_bac": medie, "promovare_%": pct}
            i += 7
        else:
            i += 1
    return out or None


brosura = json.load(open("praguri_2025_din_brosura2026.json", encoding="utf-8"))
scoli = sorted({v["liceu"].strip() for v in brosura.values() if v.get("liceu")})
scoli = [s for s in scoli if len(s) > 6]
print("Licee de căutat: %d" % len(scoli))

date, gasite = {}, 0
for n, nume in enumerate(scoli, 1):
    rez = None
    for sl in slugs(nume):
        h = get("https://www.bacplus.ro/i/" + sl)
        if h and "promovare" in h:
            rez = ani(h)
            if rez:
                break
        time.sleep(0.3)
    if rez:
        date[nume] = rez
        gasite += 1
    if n % 20 == 0:
        print("  ... %d/%d (găsite %d)" % (n, len(scoli), gasite))
    time.sleep(0.3)

with open("bac_istoric_licee.json", "w", encoding="utf-8") as f:
    json.dump(date, f, ensure_ascii=False, indent=1)

anii = sorted({a for v in date.values() for a in v})
print("\nSalvat bac_istoric_licee.json")
print("Licee cu date: %d / %d" % (gasite, len(scoli)))
print("Ani acoperiți: %s" % ", ".join(anii))
