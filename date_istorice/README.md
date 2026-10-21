# Date istorice — proveniență și limite

Aceste agregate acoperă Bucureștiul și anii indicați, nu oferta curentă 2027.
Păstrează anul și ruta lângă fiecare prag. Verificările structurale ale ediției
2026-10-21 nu reprezintă verificarea independentă a fiecărei valori față de sursă.

| Fișier inclus în ZIP | Conținut și origine declarată |
| --- | --- |
| `praguri_2025_din_brosura2026.json` | 405 coduri, locuri și praguri generale 2025, extrase din broșura ISMB 2026 |
| `ierarhie_ancore_2025_2026.json` | Ancore poziție–notă: 93 pentru 2025 și 84 pentru 2026, din indexul portalului de ierarhie |
| `ces_praguri_2024_2025_2026.json` | Praguri și numărători per școală × specializare din listele CES ISMB; numai agregate |

Puncte de pornire pentru surse: [ISMB](http://ismb.edu.ro/index.php/admitere)
și [portalul de admitere](https://admitere.edu.ro/). Căile și documentele se pot
schimba. Datele istorice provin din depozitul existent; ediția nu le reface și nu
pretinde că fiecare valoare a fost reconfirmată online.

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

## Fișiere păstrate numai în depozit, excluse din starter ZIP

- `bac_istoric_licee.json`: **nefiabil, nu folosi pentru decizii**. La verificarea
  ediției, 96 din 654 de rânduri au `medie_bac` în afara intervalului 0–10.
  Alte valori aparent valide pot fi tot câmpuri parsate greșit. Datele provin
  din bacplus.ro, iar generatorul existent trebuie reparat și rezultatele
  reverificate înainte de orice reutilizare.
- `brosura_2026_originala.pdf` și `locuri_libere_2026.xlsx`: documente istorice
  sursă; nu sunt incluse în pachetul destinat familiilor. Obține documentele
  curente direct din sursele oficiale.
- `generare_*.py`: unelte istorice de reproducere; nu fac parte din pachet.

Datele și documentele surselor terțe își păstrează drepturile aplicabile.
Licența GPL a codului original nu relicențiază automat materialele terților.
