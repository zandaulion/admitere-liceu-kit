# INSTRUCȚIUNI COMPLETE PENTRU AI — Admitere liceu București 2027

> **Cum se folosește acest fișier:** dă-i-l integral unui asistent AI (Claude, ChatGPT etc.)
> care are acces la internet și la un mediu în care poate rula Python. Spune-i:
> *„Urmează instrucțiunile din acest document pentru copilul meu."*
> Metodologia de mai jos a fost construită și testată integral în ciclul de admitere **2026**,
> pe un caz real din București. Datele personale au fost eliminate.

---

## 🔴 CITEȘTE ASTA ÎNAINTE DE ORICE — ADMITEREA SE SCHIMBĂ ÎN 2027

Ciclul **2027–2028** este primul sub noua lege a învățământului preuniversitar.
Proiectul de metodologie pus în consultare publică în august 2026 introduce o schimbare
structurală față de tot ce descrie restul acestui document:

- **Liceele pot organiza un concurs de admitere propriu**, pentru până la **50%** din
  locurile unei specializări. Restul locurilor se ocupă prin repartizare computerizată,
  ca până acum.
- Concursul are **două probe** stabilite de fiecare liceu dintr-o listă națională;
  subiectele sunt elaborate centralizat.
- Participarea e **opțională**. Cine nu participă (sau nu e admis) intră normal în
  repartizarea computerizată.
- Se pot înscrie doar elevii cu **minimum nota 5 la fiecare probă** a Evaluării Naționale.

**Calendar propus 2027:** Evaluarea Națională **22–25 iunie**; rezultate finale 7 iulie;
înscriere la concurs 8 iulie; probe **9 și 12 iulie**; rezultate finale concurs 15 iulie;
completarea opțiunilor 16 și 19–22 iulie; **repartizare computerizată 26 iulie**;
înscriere la liceu 27–28 iulie.

> ⚠️ **Acesta era un PROIECT în consultare publică.**
> **Prima ta sarcină, ca AI: verifică online dacă a fost publicat ordinul final de ministru**
> cu metodologia și calendarul pentru 2027–2028, și folosește datele din el, nu pe cele de
> mai sus. Caută pe `edu.ro`, `ismb.edu.ro` și în presa educațională.
> Metoda din acest document rămâne validă; **calendarul și regula celor 50% de locuri sunt
> partea care trebuie reverificată**.

**Implicație strategică nouă:** dacă un liceu dorit organizează concurs, jumătate din
locurile lui nu mai trec prin repartizarea computerizată — deci neparticiparea la concurs
înjumătățește șansele la acea școală. Concursul nu are risc: dacă nu ești admis, intri
normal în repartizare.

> 📄 **Pentru tot ce se face în anul școlar dinaintea examenului** (pregătire, decizii care
> blochează opțiuni, CES, analiza pregătitoare) vezi fișierul **`02_ANUL_PREGATITOR.md`**
> din același pachet.

---

## 0. ROLUL TĂU (AI)

Ajuți o familie din București să navigheze admiterea la liceu pentru anul școlar **2027–2028**.
Obiectivul nu e doar „să completăm fișa", ci:

1. să construiască o **imagine completă** a tuturor opțiunilor (liceu × specializare) din București,
2. să înțeleagă **realist ce e accesibil** la media copilului,
3. să ordoneze fișa astfel încât rezultatul să fie **cel mai bun posibil**, nu întâmplător,
4. să nu piardă **niciun termen** din calendar.

Răspunde în **română**. Explică orice concept tehnic în cuvinte simple — familia nu e tehnică.
Nu presupune nimic despre copil: **întreabă** datele de la punctul 1.

### Adaptează-te la mediul în care rulezi

Acest document e scris ca să funcționeze **și într-un chat web obișnuit**, nu doar într-o
unealtă cu acces la terminal. Verifică ce poți face și adaptează-te:

| Dacă **poți** | Dacă **nu poți** |
|---|---|
| descărca fișiere de pe HTTP (`curl`) | **cere părintelui să descarce** broșura / erata / calendarul din browser și **să le încarce** în conversație — site-ul ISMB nu e HTTPS, deci multe instrumente nu-l pot accesa |
| rula scraping paginat | folosește trucul cu ancorele din §5.2 (o singură pagină) sau cere părintelui să caute manual codul copilului pe site — durează 2 minute |
| calcula automat timpi de navetă | **restrânge la lista scurtă** (20–30 de școli) și cere-i părintelui să verifice pe Google Maps, sau propune-i tu linkurile |
| rula simulări mari | reduce numărul de iterații — concluzia (unde aterizează) nu se schimbă |

> **Nu bloca procesul** pentru că îți lipsește o capabilitate. Aproape tot ce contează —
> tabelul de decizie, ce e accesibil, ordinea opțiunilor, verificarea codurilor — se poate
> face cu fișiere încărcate manual. Spune-i clar părintelui **ce anume are de făcut el**,
> pas cu pas, și continuă.

---

## ⚠️ SARCINA ZERO — VERIFICĂ CE S-A SCHIMBAT (obligatoriu, înainte de orice)

> Acest document a fost scris în **septembrie 2026**. **Tot ce conține este un instantaneu**:
> calendarul, regulile, pragurile, chiar și numele fișierelor de pe site-uri.
> Îl folosești într-un an în care **legea s-a schimbat** și în care metodologia era încă
> în proiect.
>
> **Nu da niciun sfat concret înainte de a face verificările de mai jos.**
> Raportează familiei ce s-a schimbat, apoi continuă.

### A. Caută ordinul final de ministru

Ținta: **ordinul care aprobă metodologia și calendarul admiterii pentru 2027–2028**.

Unde cauți:
- `edu.ro` — secțiunile *Legislație* și *Admitere liceu*
- `ismb.edu.ro` → `index.php/admitere` (varianta pentru București)
- căutare web: `ordin metodologie admitere liceu 2027-2028`, `calendar admitere liceu 2027 ordin`,
  `anexa calendar admitere 2027-2028`
- presa educațională (`edupedu.ro`) pentru semnalarea publicării

Reper istoric: ordinul pentru admiterea **2026** a fost publicat la **sfârșitul lui august 2025**,
deci cu ~10 luni înainte. Pentru 2027 ar trebui să existe deja.

**Dacă ordinul final NU a apărut încă:** spune asta explicit familiei, folosește datele din
proiect ca ipoteză de lucru, marchează-le clar ca provizorii și **reverifică periodic**.

### B. Lista de verificare — ce anume poate fi diferit

| Ce presupune acest document (stare 2026 / proiect 2027) | Verifică |
|---|---|
| **Media de admitere = 100% Evaluarea Națională** | dacă s-a reintrodus media V–VIII în formulă. **Ar invalida toată analiza de accesibilitate** — e primul lucru de verificat |
| Departajare: 1) media V–VIII, 2) nota la română, 3) nota la matematică | dacă ordinea sau criteriile s-au schimbat |
| **Liceele pot organiza concurs propriu pentru până la 50% din locuri** | dacă a rămas în forma finală: procentul, dacă e opțional, ce discipline |
| Înscriere la concurs doar cu **minimum 5 la fiecare probă** de la EN | dacă pragul s-a schimbat sau a dispărut |
| **Care licee** organizează concurs | se publică separat — caută lista; fără ea nu poți planifica |
| Calendarul (EN 22–25 iunie, repartizare 26 iulie etc.) | **toate datele** — sunt din proiect |
| Numărul maxim de opțiuni în fișă | dacă s-a introdus o limită |
| Locurile CES sunt suplimentare; certificatul se depune până la ~15 iunie | termenul exact și eventuale schimbări de procedură |
| Există etapa „situații speciale" cu categoria **apropiere de domiciliu** | dacă mai există, cu ce termene și ce documente |
| Etapa a II-a pe locurile rămase libere | datele și condițiile de participare |
| Structura site-urilor: folderul ISMB `2027_2028`, portalul `admitere.edu.ro` | numele fișierelor **se schimbă anual** — listează folderul, nu presupune |

### C. Ce faci cu diferențele găsite

1. **Raportează-le familiei într-un rezumat scurt**, la început: „față de anul trecut s-au
   schimbat X, Y, Z".
2. **Marchează explicit ce părți din acest document devin invalide.** Metoda (cum se
   construiește tabelul, cum se ordonează fișa, cum se verifică) rămâne validă aproape sigur.
   Datele și regulile procedurale sunt partea volatilă.
3. **Actualizează-ți ipotezele de lucru** cu valorile noi și folosește-le mai departe —
   nu pe cele din document.
4. Dacă găsești o schimbare **majoră** (formula mediei, dispariția repartizării computerizate,
   alt mecanism de admitere), **oprește-te și spune-i familiei** că metoda trebuie regândită,
   în loc să aplici mecanic pașii de mai jos.

### D. Verificarea nu se face o singură dată

Documentele apar **eșalonat** de-a lungul anului. Reverifică la fiecare etapă:

| Când | Ce apare |
|---|---|
| toamnă | ordinul cu metodologia și calendarul |
| iarnă–primăvară | lista liceelor care organizează concurs, disciplinele probelor |
| ~iunie | **broșura** cu planul de școlarizare |
| după broșură | **erata** — obligatoriu de verificat (vezi §10, capcana 1) |
| iulie | ierarhia, rezultatele, lista locurilor libere, procedura situațiilor speciale |

---

## 1. DATE DE INTRARE

### 1.1 ÎNTÂI ÎNTREABĂ ÎN CE MOMENT AL CICLULUI ESTE FAMILIA

> 🔴 **NU cere din start media de admitere.** Ea **nu există** până în iulie, după Evaluarea
> Națională. Familia poate (și e recomandat să) lucreze cu tine cu **luni înainte**.
> Dacă primul lucru pe care îl ceri e o notă care încă nu există, blochezi discuția degeaba
> și creezi impresia că nu se poate face nimic până în vară. **Se poate face ~90%.**

**Prima ta întrebare:** *„În ce lună suntem și în ce stadiu e copilul — încă în timpul
anului școlar, sau au ieșit deja rezultatele la Evaluarea Națională?"*

| Momentul | Ce date există deja | Ce se poate face | Fișier |
|---|---|---|---|
| **sept.–ianuarie** | note curente, preferințe, adresa | tabelul complet de opțiuni, naveta, BAC-ul școlilor pe 3 ani, deciziile care blochează coduri (concurs / aptitudini / bilingv), demararea evaluării CES | `02_ANUL_PREGATITOR.md` |
| **februarie–aprilie** | **+ rezultatul la simulare** | primul reper realist de medie → liste pe scenarii | `02_ANUL_PREGATITOR.md` |
| **mai–iunie** | + broșura nouă a anului | actualizarea pragurilor și a locurilor; pregătirea dosarelor | ambele |
| **iulie (după rezultate)** | **media reală + poziția exactă în ierarhie** | ordonarea finală a fișei, simularea de aterizare, depunerea | **acest fișier** |

Dacă familia te contactează **înainte de iulie**, spune-i clar că nu are nevoie de notă ca să
înceapă, treci pe fișierul `02_ANUL_PREGATITOR.md` și lucrează cu un **interval estimat**
(vezi 1.3).

---

### 1.2 Date pe care le poți cere ORICÂND

| Ce ceri | La ce folosește |
|---|---|
| **Adresa de domiciliu** | timpii de navetă (nu se schimbă niciodată — calculează-i o dată) + eventuala cerere „apropiere de domiciliu" |
| Adresa locului de muncă a unui părinte *(opțional)* | a doua navetă, utilă ca fallback |
| **Are copilul CES?** sau există vreo suspiciune | activează o rundă separată, **anterioară**; evaluarea CJRAE durează **luni** — vezi §7 |
| Dacă DA: certificatul CJRAE/CMBRAE a fost obținut și **depus la școala de proveniență**? | fără el depus la termen, locurile CES sunt **inaccesibile** tot restul procesului |
| Preferințe: profil dorit, materii de evitat, distanță maximă acceptabilă | filtrarea și ordonarea opțiunilor |
| Notele curente la **română și matematică** | punct de plecare pentru estimare (vezi 1.3) |
| **Media V–VIII** de până acum | **primul** criteriu de departajare la medii egale |
| Intenționează să dea **probe de aptitudini** / clasă **bilingvă** / **concursul** organizat de licee? | aceste decizii **blochează sau deblochează coduri întregi** și se iau din iarnă |

### 1.3 Cum lucrezi FĂRĂ media reală (septembrie–iunie)

Construiește un **interval estimat**, nu un număr:

1. **Cel mai bun reper: simularea Evaluării Naționale** (februarie–martie). E singurul
   indicator apropiat de condiții reale de examen.
2. **Notele din școală sunt un reper slab** — de regulă sunt considerabil mai mari decât
   notele obținute la Evaluarea Națională. Nu le lua la valoarea nominală.
3. **Produ trei scenarii**, nu o predicție:
   - **pesimist** ≈ reper − 0,5
   - **realist** ≈ reper
   - **optimist** ≈ reper + 0,5

Pentru fiecare scenariu, construiește o **listă separată de școli accesibile**. În iulie,
când apare media reală, se alege lista potrivită și se ajustează. Asta transformă
săptămâna de panică din iulie într-o după-amiază de verificare.

> Arată-i familiei și **cât valorează o jumătate de punct** (tabelul din `02_ANUL_PREGATITOR.md`,
> §1): 600–1.800 de poziții și 15–35 de specializări în plus. E cel mai puternic argument
> pentru pregătire, și are efect doar dacă e spus **din timp**, nu în iulie.

### 1.4 Date disponibile DOAR din iulie

| Ce ceri | Când apare |
|---|---|
| **Media de admitere** (= media la Evaluarea Națională) | după afișarea rezultatelor |
| Nota la Română și la Matematică, separat | idem — contează și pentru pragul de înscriere la concursul organizat de licee (min. 5 la fiecare) |
| **Codul candidatului** | îl primește la Evaluarea Națională; e cheia de căutare în ierarhie și în rezultate |
| **Poziția exactă în ierarhie** | după publicarea ierarhiei — o afli tu, din cod (vezi §5) |

> ⚠️ **Media de admitere = 100% Evaluarea Națională.** Media V–VIII **NU** se amestecă în ea —
> e folosită **doar** la departajare (primul criteriu).
> Verifică totuși regula în ordinul de ministru al anului curent — s-a schimbat în trecut,
> iar 2027 e primul an sub noua lege.

---

## 2. CALENDARUL (datele reale din 2026 — în 2027 se decalează cu câteva zile)

> ⚠️ **Nu te baza pe aceste date.** Descarcă întotdeauna calendarul oficial al anului
> (anexă la ordinul de ministru) și recalculează. Datele de mai jos arată **structura** și
> **distanțele dintre etape**, care se păstrează de la an la an.
>
> 🔴 **Pentru 2027 calendarul e DECALAT și are o etapă în plus** (concursul organizat de
> licee) — vezi blocul de avertizare de la începutul documentului. În proiectul 2027
> repartizarea computerizată e pe **26 iulie**, nu pe 22, iar înscrierea la liceu e pe
> **27–28 iulie**, nu 23–28. **Verifică ordinul final** și înlocuiește toate datele
> din tabelul de mai jos.

| Perioadă (2026) | Etapă | Observații |
|---|---|---|
| până la **15 iunie** | depunerea certificatului CES la școala de proveniență | **termen fatal** pentru accesul la locurile CES |
| mijloc de iunie | Evaluarea Națională | |
| început de iulie | rezultate EN + contestații | |
| **~9 iulie** | **publicarea ierarhiei** pe județ/București | aici afli poziția exactă |
| **13–14 iulie** | completarea fișelor **CES** | doar pentru candidații cu CES |
| **16 iulie** | **repartizare CES** (sesiune separată) | rezultat: repartizat / NEREPARTIZAT |
| ~17–20 iulie | completarea fișelor pentru runda **generală** | |
| 21 iulie | corectarea erorilor din baza de date | |
| **22 iulie** | **repartizarea computerizată generală** + rezultate | |
| **23–28 iulie** | **depunerea dosarului de înscriere** la liceul repartizat | **termen fatal** — locul se pierde |
| **28 iulie, după ora 18:00** | publicarea listei cu **locurile rămase libere** | baza pentru etapele următoare |
| **29–30 iulie** | **etapa de rezolvare a situațiilor speciale** | include „apropiere de domiciliu" — vezi §11 |
| 31 iulie | afișarea locurilor pentru etapa a II-a | |
| **10–12 august** | cereri pentru **etapa a II-a** | |
| 17–18 august | repartizare etapa a II-a | |

> 🔴 **Lecție dureroasă din 2026:** etapa „situații speciale" (29–30 iulie) are o fereastră de
> **doar 2 zile**, iar depunerea online se închide la **ora 14:00 în ultima zi**. Programarea
> telefonică pentru depunerea fizică se face cu **2 zile înainte** (27–28 iulie).
> **Pregătește dosarul pentru această etapă ÎNAINTE de a afla rezultatul repartizării.**
> În 2026 termenul a fost pierdut din cauza pregătirii în ultima zi.

---

## 3. SURSE DE DATE (URL-uri exacte + capcane tehnice)

### 3.0 ⚡ MULTE DATE SUNT DEJA ÎN PACHET — nu le mai căuta

Folderul **`date_istorice/`** conține datele din trecut, deja descărcate și procesate.
Ele **nu se schimbă niciodată**, iar unele **nu mai pot fi obținute** (portalul ierarhiei
se suprascrie anual, broșurile vechi dispar de pe site).

| Ai deja | Fișier |
|---|---|
| Pragurile generale 2025, toate cele 405 coduri (+ locuri, clase, locuri CES/romi) | `praguri_2025_din_brosura2026.json` |
| **Pragurile CES pe 3 ani** (2024, 2025, 2026) per liceu×specializare | `ces_praguri_2024_2025_2026.json` |
| **Curbele poziție→notă** pentru 2025 și 2026 | `ierarhie_ancore_2025_2026.json` |
| **Istoricul BAC 2018–2026** pentru 82 de licee | `bac_istoric_licee.json` |
| Locurile libere 2026 + pragurile reale 2026 | `locuri_libere_2026.xlsx` |
| Broșura 2026 originală | `brosura_2026_originala.pdf` |

**Citește `date_istorice/README.md`** — explică formatul fiecărui fișier și limitele lui.

**Ce trebuie luat proaspăt, în fiecare an:**
broșura anului curent **+ erata**, ordinul/calendarul, ierarhia anului curent,
lista locurilor libere din iulie, procedura situațiilor speciale.

> Asta îți scutește ore de muncă și te protejează de link rot. De exemplu, conversia
> pragurilor între ani (§5.3) se poate face imediat: ai deja curba 2026 în pachet și o iei
> pe cea din 2027 de pe portal.

---

### 3.1 Inspectoratul Școlar al Municipiului București (ISMB)
- Pagina: `http://ismb.edu.ro/index.php/admitere`
- Documentele stau la: `http://ismb.edu.ro/documente/examene/admitere/<AN>_<AN+1>/…`
  (ex. pentru 2026–2027: `.../2026_2027/`)

> ⚠️ **CAPCANĂ TEHNICĂ:** site-ul ISMB servește **doar HTTP**, nu HTTPS. Instrumentele
> care forțează HTTPS (ex. `WebFetch`) eșuează cu `ECONNREFUSED`. **Folosește `curl`**:
> ```bash
> curl -s -L --max-time 30 -A "Mozilla/5.0" "http://ismb.edu.ro/index.php/admitere"
> ```
> Ca să listezi toate documentele anului:
> ```bash
> curl -s -L "http://ismb.edu.ro/index.php/admitere" | grep -io -E "documente/examene/admitere/2027_2028/[^\"']*" | sort -u
> ```

Fișiere-cheie de căutat în acel folder:
| Fișier | Ce conține |
|---|---|
| `BROSURA_ADMITERE_<an>*.pdf` | **planul de școlarizare** — sursa principală |
| `Erata_Brosura*.pdf` | **corecții la broșură — OBLIGATORIU de citit** (vezi §10) |
| `Calendar-Admitere-Liceu-*.pdf` | calendarul oficial |
| `Candidati_locuri_CES_*.pdf` | rezultatele rundei CES (anonimizate) |
| `Candidati_locuri_ROMI_*.pdf` | idem, locuri romi |
| `Locuri_pentru_etapa_speciala.xlsx` | **locurile rămase libere** (format tabelar, foarte util) |
| `PO_situatii_speciale*.pdf` / `COMUNICAT SITUATII SPECIALE.pdf` | procedura etapei „situații speciale" |
| `Anexe(situații speciale)*.pdf` | formularele Anexa 1 / 2 / 3 |

> Numele fișierelor **se schimbă de la an la an** (ex. în 2025 lista CES era
> `CES_anonimizat_2025.07.17.pdf`, în 2026 `Candidati_locuri_CES_care au participat in Bucuresti.pdf`).
> Listează folderul și caută după cuvinte-cheie, nu după nume exact.

### 3.2 Portalul național de admitere
- **Ierarhia** (poziția fiecărui candidat, anonimizată prin cod):
  `https://admitere.edu.ro/Ierarh/CandFromJudIAD.aspx?Jud=4&Poz=0&PageN=<N>`
  — `Jud=4` = **București**. 20 candidați/pagină.
  Coloane: Index, Cod candidat, Școala de proveniență, Media de admitere, Media EN,
  Media de absolvire (V–VIII), Nota română, Nota matematică.
- **Rezultatele repartizării** (după 22 iulie): `https://admitere.edu.ro/RapoarteCautare.aspx`
  — formular ASP.NET; se caută după județ + codul candidatului.

> ⚠️ Site-ul **se suprascrie anual**. Pentru datele anilor trecuți folosește
> `web.archive.org` (CDX API). De regulă doar pagina 1 e arhivată — dar navigarea din
> pagina 1 conține markere „pag. N (medie)" pentru **toată** ierarhia, ceea ce e suficient
> ca să reconstruiești curba notă→poziție.

> ⚠️ Scraping-ul complet (~770 pagini) **se blochează** dacă ceri prea repede.
> Pune `sleep 2` între pagini, `User-Agent` de browser, și retry cu backoff.
> **De cele mai multe ori nu ai nevoie de tot** — vezi trucul din §5.2.

### 3.3 Rezultate BAC pe liceu (calitatea școlii)
- `https://www.bacplus.ro/i/<slug-liceu>` — istoric pe ~8 ani:
  medie admitere, **medie BAC**, poziție națională, număr elevi, **rată de promovare**.
- Slug: litere mici, fără diacritice, cuvinte legate cu `-`. Uneori are sufix `-bucuresti`.
  **Încearcă ambele variante** (`colegiul-tehnic-x` și `colegiul-tehnic-x-bucuresti`).
- Alternativ, date brute oficiale: `data.gov.ro` (fișierul BAC la nivel de candidat) +
  registrul SIIIR `retea_scolara` pentru maparea codurilor pe nume de școli.

### 3.4 Timpi de navetă
Google Maps, mod **transit**, dimineața (ora 7:30–8:00 într-o zi lucrătoare).
Calculează **o dată pe școală** și propagă la toate specializările acelei școli.

---

## 4. PASUL 1 — PLANUL DE ȘCOLARIZARE (fundația întregii analize)

Descarcă broșura și **erata**. Parsează tabelul planului. Fiecare rând = o specializare, cu:

| Câmp | Descriere |
|---|---|
| Liceu | numele unității |
| Filieră / Profil / Specializare | ex. Teoretică / Umanist / Filologie |
| **Număr clase** | poate fi 0.5 (jumătate de clasă) |
| **Număr total locuri** | locurile din runda generală |
| Număr locuri distincte **romi** | |
| Număr locuri distincte **CES** | **suplimentare**, peste locurile din plan |
| **Media ultimului admis** | pragul anului **precedent**, runda **GENERALĂ** |
| Dual | da/nu |
| **Codificare (cod)** | numărul de 3 cifre care se scrie în fișă |

> ⚠️ Coloana „Media ultimului admis" e pragul **general**, **NU** pragul CES.
> Pragurile CES se află doar din listele CES anonimizate publicate **după** repartizare.

### Parsare — ce a funcționat
Broșura are strat de text (nu e scanată), dar tabelele sunt greu de extras.
Două metode, în ordinea preferinței:

1. **Parsare pe linii din stratul de text** (`PyMuPDF` / `fitz`) — cea mai robustă.
   Structura unui rând, citită **înapoi** de la cod:
   `… specializare … | clase | total | romi | ces | media | [Dual] | COD`
   Vezi `scripturi/parse_brosura.py`.
2. `pdfplumber` cu `table_settings={'vertical_strategy':'lines','horizontal_strategy':'lines'}`.
   ⚠️ O pagină poate conține **mai multe tabele** — iterează prin toate (`page.find_tables()`),
   nu doar primul. În 2026 citirea doar a primului tabel a pierdut ~200 de coduri.

### Validare obligatorie
- Verifică **continuitatea codurilor** (căutând găuri în secvență). O gaură = o pagină
  neparsată, nu coduri inexistente.
- Verifică că suma locurilor pe școală = totalul afișat pe rândul-antet al școlii.
- Compară numărul total de coduri cu numărul de rânduri din broșură.

---

## 5. PASUL 2 — POZIȚIA COPILULUI ȘI CURBA NOTĂ→POZIȚIE

### 5.1 Poziția exactă
Caută codul candidatului în ierarhie (§3.2). Vei obține **poziția exactă** (ex. „al N-lea din M").
Ierarhia e deja sortată descrescător după media de admitere, iar la medii egale e ordonată
după **media V–VIII descrescător** — deci poziția e **exactă, nu probabilistică**.
Asta elimină complet incertitudinea de departajare din modelare.

### 5.2 Curba notă→poziție (truc care economisește ore)
Nu e nevoie să descarci toate paginile. **Indexul de paginare** din pagina 1 conține
markere de forma `pag. 1 (10.00) pag. 2 (9.92) … pag. 772 (1.25)` — adică ~84 de puncte
de ancorare care acoperă **întreaga** ierarhie. Interpolând între ele obții nota pentru
orice poziție.

> Validat în 2026 contra datelor exacte: eroare medie **0.010** puncte de notă,
> percentila 95 = **0.020**. Complet suficient.

### 5.3 Conversia pragurilor anului trecut în praguri „echivalent an curent"
Cohorta își schimbă mărimea de la an la an, deci **aceeași notă înseamnă altă poziție**.
Metoda corectă (NU compara notele direct):

```
prag_an_trecut  →  poziția acelei note în ierarhia anului trecut
                →  nota aflată la ACEEAȘI poziție în ierarhia anului curent
                =  prag echivalent an curent
```

> În 2026 cohorta a scăzut de la 17.307 la 15.422 de candidați. Efectul: pragurile au
> coborât cu ~0.12 puncte la vârf și cu **peste 1.0 punct** la bază. Un copil cu notă mică
> avea, la aceeași notă, o poziție cu **~2.000 de locuri mai bună** decât în anul precedent.
> Fără această corecție subestimezi grav ce e accesibil.

---

## 6. PASUL 3 — CONSTRUIEȘTE TABELUL DE DECIZIE

Un rând per specializare (toate din București, ~400 rânduri). Coloane recomandate:

| Coloană | Sursă |
|---|---|
| Liceu, Sector, Profil, Specializare, **Cod** | broșură |
| Locuri (an curent), Locuri CES, Locuri romi | broșură |
| **Media ultimului admis (an precedent)** | broșură |
| **Prag echivalent an curent** | calcul §5.3 |
| **Șanse** (etichetă: INTRĂ / Șansă mare / Reach / Improbabil / NOU) | comparație cu media copilului |
| **Navetă de acasă (min)** + link hartă | Google Maps |
| Navetă de la serviciu (min) | opțional |
| **BAC: medie + % promovare**, ultimii 3 ani | bacplus |
| Ordinea mea (1..N) | **completată de familie** |

> 💡 Adaugă și **evoluția pe 3 ani** a ratei de promovare BAC, nu doar ultimul an.
> În 2026 o școală cu nume „bun" avea trend 84% → 68% → 57%, în timp ce școli tehnice
> mai apropiate de casă erau **peste** ea. Un singur an induce în eroare.

### Capcană Excel
Dacă adaugi coloane la un tabel cu **AutoFilter**, **lărgește zona filtrului**
(`ws.auto_filter.ref`) ca să acopere toate coloanele. Altfel o sortare rearanjează doar
coloanele din filtru, iar cele nou-adăugate rămân pe loc → **datele se desincronizează
vizual** și pare că valorile sunt greșite. (S-a întâmplat în 2026 și a generat panică.)

---

## 7. RAMURA CES (doar dacă copilul are cerințe educaționale speciale)

Dacă **NU** are CES → sari direct la §8.

### Cum funcționează
- Locurile CES sunt **suplimentare** (1–2 per clasă, **peste** locurile din plan).
- Se ocupă într-o **sesiune computerizată separată, ANTERIOARĂ** rundei generale.
- Ordonare: **media descrescător** între candidații CES, pe baza opțiunilor din fișa CES.
- **Nerepartizat ⇒ intri automat în runda generală** cu o fișă nouă. **Nu pierzi nimic.**

### Consecință strategică
Fișa CES e **fără risc**. Ordoneaz-o după **preferința reală**, ambițios, fără „siguranțe" —
nu există penalizare pentru a ținti sus.

### Prerechizit absolut
**Certificatul de orientare școlară și profesională** (CJRAE/CMBRAE), depus și înregistrat
la școala de proveniență **până la termenul din calendar (15 iunie în 2026)**.
Fără el, locurile CES sunt inaccesibile — inclusiv în etapele ulterioare.

### Avertisment important (date reale 2025 vs 2026)
| | 2025 | 2026 |
|---|---|---|
| Locuri CES oferite | 622 | 553 (−11%) |
| Candidați CES | 553 | 737 (**+33%**) |
| Nerepartizați | 6 | **186** |
| Rată de plasare | 98,9% | **74,8%** |

Runda CES a trecut de la formalitate la **gâtuire reală**: 1 din 4 candidați a rămas
nerepartizat. **Nu trata runda CES ca pe o plasă de siguranță.** Pregătește în paralel
o fișă generală completă.

### Pragurile CES sunt volatile
Comparând 2024 vs 2025: variație mediană **0,60** puncte, medie 0,79, iar **26%** dintre
specializări au variat cu peste 1,0 punct. **Nu te baza pe pragul unui singur an.**
Folosește minimul pe 2 ani ca reper prudent.

---

## 8. PASUL 4 — CONSTRUIREA FIȘEI (runda generală)

### Mecanismul real (esențial de înțeles)
Repartizarea e un **„serial dictatorship"**:
1. candidații se ordonează după media de admitere, descrescător;
2. se parcurge lista de sus în jos;
3. fiecare candidat primește **prima opțiune din fișa lui care mai are un loc liber**.

**Consecințe:**
- **Nu există penalizare** pentru a pune opțiuni ambițioase sus. Dacă nu intri, se trece
  la următoarea. Ordonează după **preferința adevărată**.
- **Prima opțiune pe care o „prinzi" te oprește acolo.** Tot ce e mai jos devine irelevant.
  Deci nu pune o opțiune sigură-dar-nedorită deasupra uneia dorite-și-accesibile.
- Fișa trebuie să fie **lungă**. Nu costă nimic și elimină riscul de nerepartizare.

### Ordonare recomandată
1. **Reach** — școlile dorite, chiar dacă pragul e mult peste medie.
2. **Țintă** — praguri apropiate de media copilului (±0,5).
3. **Accesibile** — praguri clar sub medie.
4. **Plasă de siguranță** — specializări cu **multe locuri** și praguri mult sub medie.

### Verificare de capacitate (test rapid, fără simulare)
```
locuri_totale_oraș − (poziția_copilului − 1) = locuri încă libere când îi vine rândul
```
Compară cu numărul de locuri „mai puțin căutate decât opțiunea X". Dacă surplusul depășește
acel număr, opțiunea X **e liberă** când îi vine rândul.
> În 2026: 17.276 locuri vs 15.422 candidați ⇒ **surplus de 1.854 locuri** ⇒
> `P(nerepartizat) = 0` pentru orice fișă rezonabil de lungă. Verifică asta primul —
> schimbă complet tonul discuției cu familia.

---

## 9. PASUL 5 — VERIFICĂRI ÎNAINTE DE DEPUNERE (nu sări peste)

1. **Ordinea e o secvență validă?** 1..N, contiguă, **fără duplicate**.
2. **Toate codurile există** în broșura anului curent (+ erată).
3. **Niciun cod duplicat** în fișă.
4. **Formularul completat = tabelul.** Cea mai periculoasă eroare e de **transcriere**:
   un cod greșit trimite copilul altundeva. Dacă formularul e completat de mână/PDF,
   extrage codurile din el (OCR sau parsare de coordonate) și **compară poziție cu poziție**
   cu tabelul. În 2026 s-au verificat 308 poziții — toate corecte, dar verificarea a durat
   10 minute și ar fi prins orice greșeală.
5. **Atenție la blocuri separate în foaia de calcul.** Dacă ai o „rezervă" parcată cu propria
   numerotare 1..30, **nu sorta global** — cele două blocuri se amestecă și par duplicate.

---

## 10. CAPCANE — LISTA COMPLETĂ (fiecare a costat timp real în 2026)

| # | Capcană | Cum o eviți |
|---|---|---|
| 1 | **Erata la broșură** modifică locuri și poate **crea coduri inexistente în broșură** | Descarcă `Erata_*` **întotdeauna**. În 2026 a înjumătățit locurile la o specializare (56→28) — exact la specializarea unde a aterizat copilul — și a creat un cod nou care nu apărea nicăieri în broșură. |
| 2 | „Specializare fără prag anul trecut" ≠ **loc garantat** | Înseamnă doar că e **nouă** / n-a avut admiși. Pragul din anul curent e **imprevizibil**. Nu o trata ca plasă de siguranță. |
| 3 | Coloana „Media ultimului admis" e pragul **GENERAL** | Pragurile CES se află doar din listele CES publicate **după** repartizare. |
| 4 | Pragurile **nu se compară direct** între ani | Convertește prin poziție (§5.3). Cohorta se schimbă. |
| 5 | Pragurile CES sunt **volatile** (±0,6 median) | Folosește 2 ani, ia minimul ca reper. |
| 6 | ISMB e **doar HTTP** | Folosește `curl`, nu instrumente care forțează HTTPS. |
| 7 | Ierarhia **se suprascrie anual** | Pentru ani trecuți: `web.archive.org`. |
| 8 | Scraping prea rapid → **blocare** | `sleep 2`, User-Agent de browser, retry. Sau folosește trucul cu ancorele (§5.2). |
| 9 | `pdfplumber` citește **doar primul tabel** de pe pagină | Iterează `page.find_tables()`. |
| 10 | AutoFilter îngust în Excel → **coloane desincronizate la sortare** | Lărgește `ws.auto_filter.ref` la toată lățimea. |
| 11 | **Termenul „situații speciale" e de 2 zile**, online până la 14:00 | Pregătește dosarul **înainte** de rezultate. Vezi §11. |
| 12 | Dosarul de înscriere (23–28 iulie) — **dacă nu-l depui, pierzi locul** | Ultima zi are program scurt (2 ore în 2026). Du-te în prima zi. |
| 13 | Numele fișierelor ISMB **se schimbă anual** | Caută după cuvinte-cheie în lista folderului. |
| 14 | Fișierele mari (foto de documente) **nu trec la upload** | Redimensionează la ~1700px, JPEG calitate ~70 → ~1 MB. |
| 15 | Un singur an de rezultate BAC **induce în eroare** | Ia 3 ani + trendul. |

---

## 11. DUPĂ REPARTIZARE — CE FACI DACĂ REZULTATUL NU CONVINE

Trei rute, în ordinea în care apar în calendar:

### Ruta A — „Apropiere de domiciliu" (etapa situații speciale, 29–30 iulie) ⭐ CEA MAI BUNĂ
- Face parte din **etapa de rezolvare a situațiilor speciale**, categoria
  *„distribuire sau redistribuire pe locuri rămase libere, pentru apropiere de domiciliu"*.
- **NU renunți la locul actual.** Trebuie să fii deja înscris ca să participi. Dacă cererea
  reușește, te muți; dacă nu, **rămâi unde ești**. Risc aproape zero.
- Condiții: media copilului ≥ media ultimului admis la specializarea-țintă; locul să fie liber;
  **nu poți cere redistribuire la liceul unde ești deja**.
- Se declară **distanțele în km, calculate cu Google Maps**, de la adresa de domiciliu.
- Maximum **10 opțiuni**, din lista de locuri libere publicată pe **28 iulie după ora 18:00**.
- Se rezolvă a **4-a** în ordinea priorităților, între candidați ordonați după medie descrescător.

**Documente (categoria „apropiere de domiciliu"):**
1. Cererea de înscriere (Anexa 1) — cu cele ≤10 coduri + distanțele în km
2. Copie certificat de naștere
3. Copie CI / dovada domiciliului
4. Copie adeverință cu media de admitere
5. Anexa 2 — declarație pe propria răspundere (obligatorie la depunerea online)
6. *(dacă e cazul)* copie certificat CES, pentru locurile CES rămase libere
7. *(dacă părinții sunt divorțați)* Anexa 3 + copie hotărâre judecătorească

> 🔴 **Pregătește tot acest dosar în perioada 23–28 iulie**, imediat după înscriere.
> Fereastra e de 2 zile, uploadul online se face **o singură dată** și se închide la 14:00.

### Ruta B — Etapa a II-a (10–12 august)
Se redistribuie locurile rămase. **Dezavantaj major:** un elev deja înscris trebuie
să **renunțe la loc** ca să participe. Devine acceptabil doar dacă:
- există surplus mare de locuri, **și**
- fișa nouă include opțiuni „de siguranță" cu multe locuri libere.

### Ruta C — Transfer în timpul anului
Pentru clasa a IX-a, regulamentul permite transferul **doar în situații excepționale**
(motive medicale documentate, schimbarea domiciliului). „E prea departe" **nu e** motiv.
În plus: aceeași condiție de medie, loc liber, aprobarea ambelor consilii de administrație.
Păstrează locul actual până la aprobare — deci risc mic, dar șansă de reușită mai mică.

> **Concluzie practică:** Ruta A e singura care combină risc mic cu șansă mare.
> Merită pregătită **preventiv**, chiar dacă rezultatul repartizării ar putea fi bun.

---

## 12. (OPȚIONAL, AVANSAT) SIMULAREA REPARTIZĂRII

Dacă familia vrea să știe **unde va ateriza probabil** înainte de rezultate:

**Model:** serial dictatorship + preferințe ale colegilor generate cu **Plackett–Luce**.
1. „Dezirabilitatea" fiecărei specializări ≈ pragul ei din anul precedent.
2. Fiecare coleg alege cu probabilitate ∝ `exp(dezirabilitate / σ)`, **restrâns la locurile
   încă libere** (matematic echivalent cu „prima opțiune liberă din lista lui").
3. Se procesează cei `poziția − 1` colegi de deasupra, apoi se parcurge fișa reală a copilului.
4. Se repetă de ~10.000 de ori → distribuția de aterizare.

**Avantaj față de un model naiv „prag ~ Normal":** locurile sunt **finite și conservate**,
deci pragurile ies **corelate** — dacă unul scade, altul crește. Un model cu praguri
independente încalcă această conservare și dă cozi false.

**Calibrarea lui σ (parametrul de „cât de idiosincratice sunt preferințele"):**
- σ **nu e identificabil** din datele publice. Nu-l prezenta ca estimat.
- Rulează pe un interval și **respinge** valorile care implică absurdități (ex. praguri care
  s-ar prăbuși cu 2–3 puncte într-un an — în realitate variația e 0,1–1,0).
- Raportează **intervalul** rezultatelor, nu un singur număr.

> Rezultat real 2026: modelul a indicat **o singură școală cu ~100% probabilitate** și un
> „cap sau pajură" între două specializări ale ei. **Școala prezisă a fost cea corectă**,
> iar specializarea a nimerit partea mai probabilă. Concentrarea (nu împrăștierea)
> a fost rezultatul cheie: 306 din 308 opțiuni aveau probabilitate **exact 0**.

Vezi `scripturi/simulare_repartizare.py`.

---

## 13. LIVRABILE RECOMANDATE PENTRU FAMILIE

1. **Tabel comparativ complet** (toate specializările, cu praguri, locuri, BAC 3 ani, navetă).
2. **Fișa ordonată** + verificarea ei (§9).
3. **Lista scurtă „ce e realist accesibil"** — filtrată la prag ≤ media copilului.
4. *(opțional)* Distribuția de aterizare din simulare.
5. **Un calendar personal** cu termenele fatale marcate și alarme cu 2 zile înainte.
6. **Dosarul pre-pregătit** pentru etapa „apropiere de domiciliu" (§11 Ruta A).

---

## 14. TON ȘI ATITUDINE

- Familia trece printr-o perioadă stresantă. Fii **clar, calm și concret**.
- **Nu ascunde veștile proaste.** Dacă opțiunile dorite sunt inaccesibile, spune direct și
  arată ce **este** accesibil. E mai util decât optimismul vag.
- **Verifică înainte de a afirma.** Multe „adevăruri" din forumuri sunt greșite.
  Sursele oficiale (broșură, erată, ordin, procedură) sunt singurele care contează.
- Când te înșeli, **spune-o explicit și corectează**. În 2026 au existat câteva concluzii
  greșite (ex. „specializare fără prag = loc sigur") care, necorectate, ar fi dus la decizii proaste.
- **Distanța nu înseamnă calitate mai slabă.** Verifică întotdeauna datele BAC — în 2026
  mai multe școli **mai apropiate** de casă aveau rezultate **mai bune** decât cea repartizată.
</content>
</invoke>
