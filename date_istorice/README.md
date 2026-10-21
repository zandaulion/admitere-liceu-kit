# Date istorice — proveniență și limite

Aceste agregate acoperă Bucureștiul și anii indicați, nu oferta curentă 2027.
Păstrează anul și ruta lângă fiecare prag. Verificările structurale ale ediției
2026-10-21 nu reprezintă verificarea independentă a fiecărei valori față de sursă.

| Fișier inclus în ZIP | Conținut și origine declarată |
| --- | --- |
| `praguri_2025_din_brosura2026.json` | 405 coduri, locuri și praguri generale 2025, extrase din broșura ISMB 2026 |
| `ierarhie_ancore_2025_2026.json` | Ancore poziție–notă: 93 pentru 2025 și 84 pentru 2026, din indexul portalului de ierarhie |
| `ces_praguri_2024_2025_2026.json` | Praguri și numărători per școală × specializare din listele CES ISMB; numai agregate |
| `bac_istoric_licee.json` | Medii BAC și rate de promovare agregate la nivel de liceu, 2018–2026, din tabelele publice PlusEdu/BacPlus |
| `bac_provenienta.json` | Data verificării și URL-ul paginii fiecăruia dintre cele 82 de licee |

Puncte de pornire pentru surse: [ISMB](http://ismb.edu.ro/index.php/admitere)
și [portalul de admitere](https://admitere.edu.ro/). Căile și documentele se pot
schimba. Primele trei seturi provin din depozitul existent și nu au fost reverificate
integral online. Istoricul BAC a fost refăcut în această ediție din tabelele
identificate prin antet și școală; sursa poate corecta ulterior valorile.

## Praguri generale și ancore

Broșura unui an poate conține pragurile anului precedent. În acest set pragul
este `prag_2025`, nu pragul 2026 sau 2027. Nu există un set complet de praguri
generale pentru 2024–2026. Codurile și locurile nu se transferă automat între ani.
Schema (`liceu`, `locuri`, `prag_2025`) diferă de ieșirea extractorului PDF
(`scoala`, `total`, `media`); convertește explicit dacă reutilizezi datele.
`null` marchează un câmp lipsă în extragere, nu valoarea zero: sunt 18 valori
`locuri_romi`, 55 valori `locuri_ces` și 62 valori `prag_2025` lipsă.

Ancorele sunt eșantioane de poziții, nu ierarhia completă. Ultimele ancore sunt
17.301 (2025) și 15.421 (2026); acestea **nu certifică numărul total de candidați**.
Interpolarea este aproximativă și nu rezolvă egalitățile de medii.

## Agregate CES și acoperire incompletă

| An | Rânduri parsate | Admiși parsați | Nerepartizați parsați | Rată în set |
| --- | ---: | ---: | ---: | ---: |
| 2024 | 454 | 451 | 3 | 99,3% |
| 2025 | 550 | 544 | 6 | 98,9% |
| 2026 | 730 | 548 | 182 | 75,1% |

Acestea sunt totalurile **extrase**, nu totalurile oficiale complete. De exemplu,
nota istorică a extractorului indică 730 din 737 înregistrări în 2026. Rânduri
ratate pot face pragul minim calculat prea mare. Nu combina totaluri oficiale
cu numărători parțiale pentru a calcula rate.

Nu sunt incluse coduri de candidat, școli de proveniență, diagnostice sau liste
individuale. Nu încerca să identifici candidați din grupuri mici și nu redistribui
PDF-uri cu rânduri individuale în rapoarte de eroare.

## Istoricul BAC corectat

Setul vechi avea **654** de înregistrări: 96 de medii peste 10, alte 24 medii
greșite dar între 0 și 10, două medii lipsă și niciun rând pentru 2019. Cauza
principală era identificarea coloanei după o poziție națională numerică, nu
după antetul „Medie Bac”.

La **21 octombrie 2026**, am citit tabelele publice PlusEdu/BacPlus pentru
fiecare dintre cele **82 de licee** existente în set și am verificat că titlul
paginii corespunde numelui liceului. Noul set are **738** de înregistrări
(82 × 9 ani, 2018–2026). Mediile sunt în intervalul 0–10 și ratele 0–100%;
valorile sunt cele afișate de sursă la data verificării, nu date oficiale
recalculate independent. `bac_provenienta.json` listează pagina fiecărei școli.
Statisticile sursei exclud absolvenții din promoțiile anterioare. Lipsesc
licee neidentificate în versiunea inițială. Sursa poate revizui cifrele,
iar compararea liceelor are și alte limite decât media și rata BAC.

Generatorul `generare_bac_din_bacplus.py` este inclus pentru refacere. Citește
numai tabelul istoric cu antete explicite și agregate pe școală; nu descarcă
rânduri individuale de candidați. Testele folosesc doar HTML sintetic.

## Fișiere păstrate numai în depozit, excluse din starter ZIP

- `brosura_2026_originala.pdf` și `locuri_libere_2026.xlsx`: documente istorice
  sursă; obține documentele curente direct din sursele oficiale.
- `generare_ces_din_pdf.py`: unealtă istorică pentru sursa CES, exclusă.

Datele și documentele surselor terțe își păstrează drepturile aplicabile.
Licența GPL a codului original nu relicențiază automat materialele terților.
