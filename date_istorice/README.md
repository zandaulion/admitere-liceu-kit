# DATE ISTORICE — deja descărcate, NU le mai căuta

> **Pentru AI:** fișierele din acest folder conțin date **din trecut**, care **nu se mai
> schimbă**. Folosește-le direct. **Nu pierde timp căutându-le online** — unele nici nu mai
> pot fi găsite (portalul ierarhiei se suprascrie în fiecare an, broșurile vechi dispar).
>
> Ce trebuie totuși luat **proaspăt** în fiecare an: broșura anului curent + **erata**,
> calendarul/ordinul, ierarhia anului curent, lista locurilor libere. Vezi „SARCINA ZERO"
> din `01_PROMPT_COMPLET_PENTRU_AI.md`.

---

## Ce conține

| Fișier | Conținut | Perioadă |
|---|---|---|
| **`praguri_2025_din_brosura2026.json`** | 405 coduri: liceu, specializare, clase, locuri, locuri romi, locuri CES, **pragul general 2025** | admiterea 2025 |
| **`ces_praguri_2024_2025_2026.json`** | praguri CES per liceu×specializare + statistici pe an | **3 ani** |
| **`ierarhie_ancore_2025_2026.json`** | curbele **poziție → notă** pentru București | 2025, 2026 |
| **`bac_istoric_licee.json`** | medie BAC + rată de promovare, per liceu | **2018–2026** |
| **`locuri_libere_2026.xlsx`** | locurile rămase libere după etapa I (cu praguri **2026** reale) | 2026 |
| `brosura_2026_originala.pdf` | broșura ISMB, sursa primară | 2026 |
| `generare_*.py` | scripturile care au produs agregatele (pentru refacere/verificare) | — |

---

## Cum se folosesc

### 1. Pragurile generale (`praguri_2025_din_brosura2026.json`)
```json
"101": { "liceu": "...", "specializare": "...", "clase": 5.0,
         "locuri": 140.0, "locuri_romi": 5.0, "locuri_ces": 5.0, "prag_2025": 9.72 }
```
Broșura fiecărui an conține pragurile **anului precedent**. Deci broșura 2027 îți va da
pragurile **2026**, iar acest fișier ți le dă pe cele din **2025** — împreună, doi ani de
istoric, suficient pentru a estima volatilitatea.

### 2. Curbele poziție→notă (`ierarhie_ancore_2025_2026.json`)
```json
{ "2026": [[1, 10.0], [21, 9.92], ...], "2025": [[1, 10.0], ...] }
```
Liste de perechi `[poziție, notă]`. Interpolează liniar între ele.
**La ce folosesc:** conversia unui prag dintr-un an în echivalentul altui an
(prag → poziție în anul vechi → nota de la aceeași poziție în anul nou).

| An | Ancore | Candidați (ultima poziție) |
|---|---|---|
| 2025 | 93 | 17.301 |
| 2026 | 84 | 15.421 |

Se vede direct contracția cohortei — mecanismul care coboară pragurile.

### 3. Pragurile CES (`ces_praguri_2024_2025_2026.json`)
```json
"2026": {
  "total_candidati": 730, "admisi": 548, "nerepartizati": 182, "rata_plasare_%": 75.1,
  "praguri": { "Liceu X || Specializare Y": { "prag_ces": 6.70, "nr_admisi": 3, ... } }
}
```
`prag_ces` = **ultima medie admisă** la acea combinație (echivalentul pragului).

**Statistici, pentru context:**

| | 2024 | 2025 | 2026 |
|---|---:|---:|---:|
| Candidați CES | 454 | 550 | **730** |
| Admiși | 451 | 544 | 548 |
| Nerepartizați | 3 | 6 | **182** |
| Rată de plasare | 99,3% | 98,9% | **75,1%** |

Aceste trei rânduri sunt cel mai important lucru din folder pentru o familie cu CES:
runda a trecut de la formalitate la gâtuire reală într-un singur an.

**Cele trei valori pe an permit și măsurarea volatilității** — pragurile CES variază mult
(median ~0,6 puncte între ani, un sfert peste 1,0). Nu te baza niciodată pe un singur an;
folosește minimul pe 2–3 ani ca reper prudent.

### 4. Istoricul BAC (`bac_istoric_licee.json`)
```json
"COLEGIUL X": { "2026": {"medie_bac": "6.36", "promovare_%": "64"}, "2025": {...} }
```
82 din 89 de licee, cu până la **8 ani** fiecare. Folosește **trendul pe 3 ani**, nu ultimul
an — o școală cu nume bun poate avea 84% → 68% → 57%, iar una modestă poate urca.

### 5. Locurile libere 2026 (`locuri_libere_2026.xlsx`)
Util din două motive: arată **formatul** listei publicate la sfârșitul lui iulie, și conține
coloana „Ultima medie admitere computerizată" cu **pragurile reale din 2026** pentru
specializările care au rămas cu locuri.

---

## Limite cunoscute (fii onest cu familia)

- **Parsarea CES acoperă ~99%** din înregistrări (ex. 2026: 730 din 737 oficiale;
  nerepartizații 2025 se potrivesc exact — 6). Câteva praguri pot fi cu puțin mai mari decât
  în realitate, dacă exact înregistrarea cea mai mică a fost ratată.
- **Nu există pragurile generale din 2024.** Broșura 2025 are alt format și nu s-a putut
  parsa automat. Nu e o pierdere mare — ai deja 2025, iar broșura 2027 îți va da 2026.
- **Nu există curba ierarhiei pentru 2024** — snapshot-urile din Wayback nu au putut fi
  descărcate. 2025 + 2026 sunt suficiente pentru conversia pragurilor.
- **7 licee lipsesc din istoricul BAC** (nu apar pe bacplus.ro cu un slug identificabil).
- Datele acoperă **doar Municipiul București**.

---

## Confidențialitate

Listele CES publicate de ISMB sunt anonimizate, dar conțin **rânduri individuale** de
candidați (cod, școală de proveniență, medii). Din acest pachet au fost păstrate **doar
agregate** — praguri și numărători per liceu×specializare. **PDF-urile brute au fost șterse
intenționat** și nu trebuie redistribuite.

Dacă vrei să refaci agregatele de la zero, `generare_ces_din_pdf.py` arată exact cum —
descarcă PDF-urile de pe `ismb.edu.ro`, rulează scriptul, apoi șterge-le.
