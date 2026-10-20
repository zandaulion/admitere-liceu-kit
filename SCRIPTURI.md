# Folosirea scripturilor / Python tools

Ghidurile pentru familii nu cer rularea scripturilor. Pentru reproducerea unei
analize, folosește Python 3.12 sau mai nou și un mediu virtual:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install pymupdf
python scripturi/parse_brosura.py date_istorice/brosura_2026_originala.pdf coduri-demo.json
```

Extractorul cere un PDF cu strat de text. Verifică numărul de coduri și totalurile
față de documentul sursă; formatul broșurii se poate schimba de la an la an.
`scripturi/ierarhie.py` și `scripturi/simulare_repartizare.py` explică în docstring
intrările și exemplele lor de folosire. Scripturile `date_istorice/generare_*.py`
descriu propriile surse și dependențe; nu sunt necesare pentru citirea agregatelor
deja incluse. Vezi [proveniența și perioadele datelor](date_istorice/README.md).

Folosește date fictive pentru exemple și rapoarte de eroare. Nu publica adrese,
nume de copii, rezultate individuale, documente CES sau conversații personale.
Nu încărca documente personale într-un serviciu AI fără să-i verifici condițiile
și fără să limitezi datele la ceea ce este necesar.
