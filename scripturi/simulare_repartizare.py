#!/usr/bin/env python3
"""
Simulează repartizarea computerizată ca să estimezi UNDE va ateriza copilul.

MODELUL
-------
Repartizarea reală e un "serial dictatorship":
  candidații se ordonează după medie descrescător; fiecare primește PRIMA opțiune
  din fișa lui care mai are un loc liber.

Colegii de deasupra nu au preferințe cunoscute, deci se generează cu un model
Plackett–Luce:
  utilitate(specializare) = dezirabilitate + zgomot Gumbel(sigma)
  dezirabilitate ≈ pragul specializării din anul precedent

Matematic, "prima opțiune liberă din ordonarea Plackett–Luce" este echivalentă cu
o singură extragere softmax RESTRÂNSĂ la specializările care mai au locuri — de aceea
simularea e rapidă.

DE CE E MAI BUN decât "prag ~ Normal(prag_anul_trecut, sigma)":
  locurile sunt FINITE și CONSERVATE. Dacă o specializare se umple, cererea se mută
  în altă parte și acolo pragul CREȘTE. Un model cu praguri independente încalcă
  această conservare și produce cozi false de probabilitate.

DESPRE SIGMA (parametrul de idiosincrazie a preferințelor)
  NU e identificabil din date publice. NU-l prezenta ca estimat.
  Rulează pe un interval și RESPINGE valorile care implică absurdități — de exemplu
  praguri care s-ar prăbuși cu 2–3 puncte într-un an (în realitate 0,1–1,0).
  Raportează INTERVALUL rezultatelor, nu un singur număr.

Dependențe: numpy
"""
import json
import sys
from collections import Counter

import numpy as np


def pregateste(locuri, dezirabilitate, este_nou):
    """dict-uri cod->valoare  =>  array-uri aliniate."""
    coduri = list(locuri.keys())
    cap = np.array([locuri[c] for c in coduri], dtype=np.int64)
    baza = np.array([dezirabilitate[c] for c in coduri], dtype=float)
    nou = np.array([este_nou[c] for c in coduri], dtype=bool)
    return coduri, cap, baza, nou


def construieste_dezirabilitate(date_brosura, dispersie_nou=0.6):
    """
    Dezirabilitatea ≈ pragul anului precedent.
    Specializările NOI (fără prag) primesc media școlii lor, marcate ca incerte.
    """
    d, nou = {}, {}
    pe_scoala = {}
    for cod, v in date_brosura.items():
        if v.get("media") is not None:
            pe_scoala.setdefault(v["scoala"], []).append(v["media"])
    global_mean = (np.mean([m for ms in pe_scoala.values() for m in ms])
                   if pe_scoala else 7.0)
    for cod, v in date_brosura.items():
        if v.get("media") is not None:
            d[cod], nou[cod] = float(v["media"]), False
        else:
            colegi = pe_scoala.get(v["scoala"])
            d[cod] = float(np.mean(colegi)) if colegi else float(global_mean)
            nou[cod] = True
    return d, nou


def o_simulare(cap, baza, nou, pozitie_copil, indici_fisa, sigma, rng,
               dispersie_nou=0.6):
    """
    O extragere completă. Returnează indicele opțiunii primite, sau -1 dacă nerepartizat.

    pozitie_copil : poziția în ierarhie (1 = primul). Deasupra lui sunt pozitie-1 colegi.
    indici_fisa   : indicii opțiunilor din fișa copilului, ÎN ORDINEA LUI.
    """
    util = baza.copy()
    if nou.any():   # specializările noi: dezirabilitate necunoscută, șoc per simulare
        util[nou] += rng.normal(0.0, dispersie_nou, size=int(nou.sum()))

    w = np.exp((util - util.max()) / sigma)
    ramase = cap.copy()
    greutati = np.where(ramase > 0, w, 0.0)
    cumul = np.cumsum(greutati)
    total = cumul[-1]

    for _ in range(pozitie_copil - 1):          # colegii de deasupra
        if total <= 0:
            break
        j = int(np.searchsorted(cumul, rng.random() * total))
        j = min(j, greutati.size - 1)
        ramase[j] -= 1
        if ramase[j] <= 0:                       # s-a umplut → iese din bazin
            greutati[j] = 0.0
            cumul = np.cumsum(greutati)
            total = cumul[-1]

    for j in indici_fisa:                        # fișa copilului, în ordinea lui
        if ramase[j] > 0:
            return j
    return -1


def ruleaza(date_brosura, fisa_coduri, pozitie_copil,
            sigme=(0.15, 0.20, 0.30), extrageri=4000, seed=2027):
    """
    fisa_coduri : lista de coduri, în ordinea din fișă (opțiunea 1 prima).
    Returnează {cod sau None: probabilitate_%}.
    """
    locuri = {c: int(v["total"]) for c, v in date_brosura.items() if v.get("total")}
    dez, nou = construieste_dezirabilitate(date_brosura)
    coduri, cap, baza, nou_arr = pregateste(locuri, dez, nou)
    idx = {c: i for i, c in enumerate(coduri)}
    indici_fisa = [idx[c] for c in fisa_coduri if c in idx]

    lipsa = [c for c in fisa_coduri if c not in idx]
    if lipsa:
        print("⚠️  Coduri din fișă inexistente în broșură: %s" % lipsa)

    print("Opțiuni: %d | Locuri totale: %d | Poziția copilului: %d | Fișă: %d opțiuni"
          % (len(coduri), cap.sum(), pozitie_copil, len(indici_fisa)))
    print("Surplus locuri față de candidații de deasupra: %d\n"
          % (cap.sum() - (pozitie_copil - 1)))

    total_cnt = Counter()
    for s in sigme:
        rng = np.random.default_rng(seed)
        c = Counter()
        for _ in range(extrageri):
            c[o_simulare(cap, baza, nou_arr, pozitie_copil, indici_fisa, s, rng)] += 1
        total_cnt.update(c)
        top = c.most_common(3)
        print("sigma=%.2f -> %s" % (s, "  ".join(
            "%s:%.0f%%" % ("NEREPARTIZAT" if j < 0 else coduri[j], 100 * n / extrageri)
            for j, n in top)))

    n = sum(total_cnt.values())
    rez = {}
    for j, cnt in total_cnt.most_common():
        cheie = None if j < 0 else coduri[j]
        rez[cheie] = round(100.0 * cnt / n, 2)
    return rez


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        print("\nUtilizare:")
        print("  python simulare_repartizare.py coduri.json fisa.json POZITIE")
        print("\n  coduri.json = ieșirea de la parse_brosura.py")
        print("  fisa.json   = listă JSON de coduri, în ordinea din fișă")
        sys.exit(1)

    brosura = json.load(open(sys.argv[1], encoding="utf-8"))
    fisa = json.load(open(sys.argv[2], encoding="utf-8"))
    pozitie = int(sys.argv[3])

    rezultat = ruleaza(brosura, [str(c) for c in fisa], pozitie)

    print("\n=== DISTRIBUȚIA DE ATERIZARE ===")
    for cod, p in list(rezultat.items())[:15]:
        if p < 0.05:
            break
        if cod is None:
            print("  %-6s NEREPARTIZAT" % ("%.1f%%" % p))
        else:
            v = brosura[cod]
            print("  %-6s cod %-5s %-38s %s"
                  % ("%.1f%%" % p, cod, v["scoala"][:38], v["specializare"][:30]))

    print("\n⚠️  Raportează un INTERVAL, nu un singur număr. Sigma nu e identificabil.")
