# Scripturi Python opționale

Citirea ghidurilor și completarea CSV-urilor nu cer Python. Pentru scripturi:
Python **3.12+**, mediu virtual și dependențele fixate în `requirements.txt`.
Comenzile se rulează din folderul pachetului dezarhivat.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripturi/simulare_repartizare.py modele/coduri-demo.json modele/fisa-demo.json 2
```

Pe Windows, activează mediul cu `.venv\Scripts\Activate.ps1` în PowerShell.
Exemplul folosește doar școli fictive și poziția 2. Procentul afișat este o
frecvență în model, nu o probabilitate reală de admitere. `sigma` nu este estimat;
compară rezultatele pe scenarii, nu doar media lor.

## Extragerea unei broșuri

Descarcă separat PDF-ul public pentru anul dorit de la ISMB. Folosește un PDF
cu strat de text și, de exemplu, salvează-l drept `brosura.pdf`:

```bash
python scripturi/parse_brosura.py brosura.pdf coduri.json
```

Compară codurile, numărul de rânduri și totalurile cu PDF-ul. Formatul poate fi
diferit de cel testat; aplică erata separat. Ieșirea extractorului folosește
câmpurile `scoala`, `total`, `media`; agregatul istoric folosește `liceu`, `locuri`,
`prag_2025` și **nu este direct interschimbabil** cu ieșirea extractorului.

## Ierarhie

`scripturi/ierarhie.py` include funcțiile offline `nota_la_pozitie` și
`pozitie_la_nota`, care pot folosi ancorele istorice. Interpolarea este aproximativă.
Comenzile `curba` și `cauta` accesează portalul online al anului afișat acolo;
formatul și disponibilitatea lui se pot schimba. `cauta` poate traversa multe
pagini și afișează rezultate individuale: preferă căutarea manuală locală și nu
publica ieșirea. Testele pachetului folosesc exclusiv date sintetice, fără rețea.

## Date istorice excluse

Generatoarele istorice, PDF-ul și XLSX-ul originale și setul BAC vechi nu sunt în
ZIP. Generatorul BAC și datele sale din depozit au erori cunoscute; simpla
rerulare nu garantează corectitudinea. Vezi [date_istorice/README.md](date_istorice/README.md).
