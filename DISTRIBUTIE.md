# Ediția 2026-10-21.1 — distribuție

Arhiva recomandată pentru familii este `Admitere-Liceu-Kit-2026-10-21.1.zip`, din
[ediția v2026.10.21.1](https://github.com/zandaulion/admitere-liceu-kit/releases/tag/v2026.10.21.1).
Descarcă și `SHA256SUMS`, apoi verifică înainte de dezarhivare:

```bash
sha256sum --check SHA256SUMS
```

Pe Fedora comanda este disponibilă prin coreutils. Pe Windows, compară rezultatul
`Get-FileHash .\Admitere-Liceu-Kit-2026-10-21.1.zip -Algorithm SHA256` cu `SHA256SUMS`.
Deschide `START.html` din folderul extras. Citirea locală nu cere rețea;
verificarea surselor curente și utilizarea unui serviciu AI cer acces la internet.

## Conținut și excluderi

Arhiva include numai lista explicită din `scripturi/pachet.py`: ghiduri, pagina
locală, șabloane sintetice, patru agregate JSON, proveniența BAC și patru unelte de analiză,
constructorul pachetului, teste, dependențe și licență. `RELEASE.json` indică
ediția și revizia sursă. `MANIFEST.sha256` verifică toate fișierele din arhivă,
cu excepția manifestului însuși; rulează `sha256sum --check MANIFEST.sha256`
din folderul extras.

Nu include `.git`, istoricul commiturilor, jurnale locale, medii virtuale,
fișiere personale, PDF/XLSX originale ori generatorul istoric CES. Istoricul
BAC corectat și URL-urile surselor pe școală sunt incluse. Arhivele automate
GitHub „Source code” reprezintă întregul depozit și pot include fișierele
istorice excluse din acest starter pack.

Datele istorice au limitele din [date_istorice/README.md](date_istorice/README.md).
Nu sunt un set de coduri curente de înscriere și nu sunt reverificate integral.
Codul și documentația originale: GPL-3.0-or-later; drepturile surselor terțe rămân aplicabile.

## Reproducerea arhivei

Folosește Python 3.12+ și fișierele exacte ale tagului `v2026.10.21.1`. Nu sunt
necesare dependențe externe pentru constructor. Revizia trebuie să fie SHA-ul
complet din `RELEASE.json` (sau `git rev-parse HEAD` într-un checkout al tagului):

```bash
python scripturi/pachet.py --revision REVIZIA_SHA_COMPLETA --output dist
```

Constructorul fixează ordinea, timpii și permisiunile membrilor ZIP și nu
încorporează căi locale ori identități. Compară hash-urile fișierelor din manifest;
compresia poate produce bytes diferiți între versiuni Python/zlib.
