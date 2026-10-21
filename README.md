# Admitere Liceu Kit 🎓

Ghiduri în română, agregate istorice și scripturi Python opționale pentru
organizarea opțiunilor de admitere la liceu în București. Poți citi ghidurile
fără programare și le poți folosi cu un asistent AI.

**[Descarcă pachetul de început — 21 octombrie 2026](https://github.com/zandaulion/admitere-liceu-kit/releases/download/v2026.10.21.1/Admitere-Liceu-Kit-2026-10-21.1.zip)**
· [Note și SHA-256](https://github.com/zandaulion/admitere-liceu-kit/releases/tag/v2026.10.21.1)

Dezarhivează ZIP-ul și deschide [START.html](START.html) în browser. Pagina
explică ordinea de citire și conținutul; nu încarcă date și nu cere instalare.
Ghidurile `.md` se pot citi într-un editor de text.

## Începe aici

1. Citește [00_CITESTE_MAI_INTAI.md](00_CITESTE_MAI_INTAI.md).
2. În timpul anului școlar, folosește [02_ANUL_PREGATITOR.md](02_ANUL_PREGATITOR.md).
3. Pentru analiza opțiunilor, transmite unui asistent AI
   [01_PROMPT_COMPLET_PENTRU_AI.md](01_PROMPT_COMPLET_PENTRU_AI.md).
4. Copiază șabloanele din [modele/](modele/) într-un folder privat. Sunt
   sintetice și nu reprezintă o fișă oficială de înscriere.

## Reguli și surse pentru 2027

**Verificare la 21 octombrie 2026:** pagina Ministerului din
[5 octombrie 2026](https://www.edu.ro/cons_pub_PO_83_84_26_admitere_liceu_27_28)
publică proiecte de metodologie și calendar pentru 2027–2028. Un proiect nu
confirmă adoptarea regulilor. Acest pachet nu certifică un ordin final pentru 2027.

Ghidurile nu mai folosesc calendarul și ipoteza concursului pentru 50% din locuri
din propunerea din august ca reguli curente. Verifică ordinul final, anexele,
broșura, erata și procedurile ISMB înainte de fiecare etapă.
Vezi [SURSE_2027.md](SURSE_2027.md) pentru surse și lista de verificare.

## Ce conține ZIP-ul

| Conținut | Scop și limite |
| --- | --- |
| Trei ghiduri și lista surselor | Pregătire, comparație și verificarea opțiunilor |
| [modele/](modele/) | CSV-uri pentru opțiuni și termene; JSON-uri sintetice pentru simulator |
| [date_istorice/](date_istorice/) | 405 coduri și praguri generale **2025**, ancore de ierarhie **2025–2026**, agregate CES **2024–2026** și medii/rate BAC **2018–2026** pentru 82 de licee |
| [scripturi/](scripturi/) | Extragere PDF, interpolare și simulare exploratorie |
| [SCRIPTURI.md](SCRIPTURI.md) | Instalare și exemple offline; Python 3.12+ doar pentru scripturi |
| [DISTRIBUTIE.md](DISTRIBUTIE.md) | Conținut, reproducerea arhivei și verificarea SHA-256 |

Datele istorice sunt context, nu predicții sau coduri de înscriere pentru 2027.
CES are acoperire incompletă; [proveniența și limitele](date_istorice/README.md)
fac parte din pachet. Testele structurale nu verifică independent fiecare valoare.

**Corecție BAC:** setul anterior avea 96 de medii în afara intervalului 0–10,
alte 24 greșite dar aparent valide și două valori lipsă. Această ediție a extras explicit coloana
„Medie Bac” din tabelele publice [PlusEdu](https://www.plusedu.ro/), a verificat
identitatea fiecărei școli și a adăugat 2019. Rezultatul acoperă 82 de licee ×
9 ani (738 de înregistrări). [Proveniența pe școală](date_istorice/bac_provenienta.json)
și limitele sunt documentate. Verifică din nou cifrele la sursă înainte de decizii:
site-ul poate corecta datele, iar alte licee lipsesc din acest set.

**Nu sunt incluse în ZIP:** PDF-ul și XLSX-ul originale și generatorul istoric CES.
Nu încărca fișiere cu candidați ori documente personale în Issues sau într-un chat.

## Confidențialitate

Lucrează cu o zonă aproximativă pentru navetă. Păstrează local adresele exacte,
codul candidatului, documentele de identitate și certificatele CES. Nu încărca
dosare personale în chat sau în Issues. Pentru suport, folosește exemple fictive.
Modelul de simulare nu are nevoie de nume sau de codul real al candidatului.

## Licență

Codul și documentația originale sunt distribuite sub
**GNU GPL versiunea 3 sau orice versiune ulterioară (GPL-3.0-or-later)**;
vezi [LICENSE](LICENSE). Datele și documentele provenite din surse terțe își
păstrează drepturile aplicabile; includerea lor nu le relicențiază automat.

## In English

Romanian-language starter pack for Bucharest high-school admissions planning.
Download the dated ZIP, extract it and open `START.html`. It includes guides,
synthetic templates, historical aggregates including corrected 2018–2026 school-level BAC results,
source links, and optional Python tools. Current
official rules take precedence; model results are not admission probabilities.
[Public overview](https://zandaulion.com/admitere.html).

## Support and contributions

Use Issues for reproducible bugs or corrections. Include the release date,
official source URL/year and the affected aggregate field or paragraph. Use
synthetic examples and exclude applicant records, contact details and credentials.
Keep changes focused and update the affected documentation. Security-sensitive
reports should follow [SECURITY.md](SECURITY.md).
