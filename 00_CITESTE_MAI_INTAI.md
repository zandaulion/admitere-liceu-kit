# Pachet Admitere Liceu București — 2027

Acest pachet conține **metoda completă** folosită de o familie din București în ciclul
de admitere 2026, pusă într-o formă pe care o poți da unui asistent AI ca s-o refacă
pentru copilul tău în 2027.

Nu trebuie să știi programare. Trebuie doar să dai fișierul potrivit unui AI și să-i
răspunzi la câteva întrebări.

---

## Ce conține pachetul

| Fișier | La ce folosește | Când |
|---|---|---|
| **`00_CITESTE_MAI_INTAI.md`** | acest ghid (pentru tine) | acum |
| **`02_ANUL_PREGATITOR.md`** | ⭐ **începe cu ăsta** — tot ce se face în anul școlar, înainte de examen | **septembrie 2026 – iunie 2027** |
| **`01_PROMPT_COMPLET_PENTRU_AI.md`** | playbook-ul complet pentru perioada de admitere | **iulie 2027** |
| `date_istorice/` | **date din trecut deja descărcate** (praguri, ierarhii, BAC 2018–2026, CES pe 3 ani) — AI-ul nu mai trebuie să le caute | oricând |
| `scripturi/` | programe gata făcute, pe care AI-ul le poate refolosi | oricând |

> 💡 Folderul `date_istorice/` economisește ore de muncă și conține lucruri care
> **nu mai pot fi găsite altfel** — portalul cu ierarhia se șterge și se rescrie în fiecare
> an, iar broșurile vechi dispar de pe site.

---

## 🔴 Important: admiterea se schimbă în 2027

Copilul tău prinde **primul an sub noua lege**. Proiectul de metodologie (august 2026)
introduce o schimbare majoră:

- **Liceele pot organiza un concurs de admitere propriu**, pentru până la **50%** din locuri.
- Participarea e **opțională** și **fără risc** — dacă nu ești admis, intri normal în
  repartizarea computerizată.
- Te poți înscrie doar cu **minimum nota 5 la fiecare probă** de la Evaluarea Națională.
- Evaluarea Națională: **22–25 iunie 2027**. Repartizarea computerizată: **26 iulie 2027**.

**Dacă un liceu dorit organizează concurs și nu participi, îți înjumătățești șansele acolo.**

> Erau date de proiect. **Verifică în septembrie 2026 dacă a apărut ordinul final** —
> se publică de obicei la sfârșitul lui august.

---

## Cum se folosește (3 pași)

### Pasul 1 — Alege un asistent AI

**Un chat obișnuit pe web este suficient.** Nu ai nevoie de nicio instalare pe calculator.

Ai nevoie de un asistent care poate:
- **primi fișiere încărcate** (PDF, Excel),
- **rula cod** (Python / analiză de date),
- **căuta pe web**.

> ⚠️ **Singurul lucru pe care trebuie să-l faci tu:** site-ul Inspectoratului (`ismb.edu.ro`)
> nu folosește HTTPS, așa că majoritatea chat-urilor **nu-l pot accesa direct**.
> Deschizi linkul în browser, salvezi PDF-ul (broșura, erata, calendarul) și îl **încarci
> în chat**. Durează două minute și se face o singură dată.

#### Ce faci manual, dacă folosești un chat web

| Ce | Cât durează | Când |
|---|---|---|
| Descarci broșura + **erata** + calendarul și le încarci în chat | ~10 min | iunie |
| Îți cauți copilul în ierarhie pe `admitere.edu.ro` (după cod) | ~2 min | iulie |
| Verifici pe Google Maps naveta — **doar pentru lista scurtă**, nu pentru toate școlile | ~20 min | oricând |

#### Când merită o unealtă instalată local

O unealtă de tip „AI cu acces la calculator" (Claude Code sau similar) descarcă singură,
generează fișierele Excel și rulează simulări mari. **Merită doar dacă** vrei:
- tabelul complet cu **toate** cele ~400 de specializări din București,
- naveta calculată automat pentru zeci de școli,
- simularea de aterizare cu multe iterații.

**Pentru deciziile care contează cu adevărat — ce e accesibil, în ce ordine pui opțiunile,
verificarea codurilor — chatul web e suficient.**

### Pasul 2 — Dă-i fișierul potrivit momentului

**Acum (anul școlar):** deschide `02_ANUL_PREGATITOR.md`, copiază tot conținutul și
trimite-i-l, cu mesajul:

> „Suntem la începutul clasei a VIII-a. Ajută-mă să parcurg ce scrie în acest document
> pentru copilul meu."

**În iulie 2027:** același lucru, dar cu `01_PROMPT_COMPLET_PENTRU_AI.md`:

> „Urmează instrucțiunile din acest document pentru copilul meu. Începe prin a-mi cere
> datele de care ai nevoie."

### Pasul 3 — Pregătește datele copilului

> ⚠️ **Nu ai nevoie de nota de la Evaluarea Națională ca să începi.** Ea apare abia în iulie.
> Tocmai de asta merită început din toamnă — ~90% din muncă se poate face fără ea.

**Acum (în timpul anului școlar):**

- [ ] Adresa de domiciliu *(pentru naveta — se calculează o dată și rămâne valabilă)*
- [ ] Adresa serviciului unui părinte *(opțional)*
- [ ] Notele curente la română și matematică *(orientativ)*
- [ ] Media generală din clasele V–VIII de până acum
- [ ] Dacă există **orice suspiciune de CES** — evaluarea durează luni, se începe din toamnă
- [ ] Ce profil îl interesează / ce materii ar vrea să evite
- [ ] Rezultatul la **simulare**, când apare (februarie–martie) — cel mai bun reper

**Abia în iulie:**

- [ ] Media de admitere (media de la Evaluarea Națională)
- [ ] Nota la română și la matematică, separat *(minimum 5 la fiecare, ca să te poți înscrie la concursul organizat de licee)*
- [ ] Codul candidatului *(îl primește la Evaluarea Națională)*

---

## Cele 7 lucruri care contează cel mai mult

Dacă nu citești nimic altceva, citește astea.

**0. Nota de la Evaluarea Națională contează mai mult decât toată strategia la un loc.**
Pe datele reale din 2026, o **jumătate de punct** în plus mută copilul cu **600–1.800 de
poziții** în ierarhie și îi deschide **15–35 de specializări** în plus. Nicio ordonare
inteligentă a fișei nu poate produce un asemenea efect. Restul acestui pachet optimizează
*în interiorul* spațiului pe care ți-l dă nota — nota decide spațiul.

**1. Fișa lungă nu costă nimic.**
Repartizarea îți dă **prima opțiune din listă care mai are loc liber**. Nu ești penalizat
dacă pui sus școli ambițioase. Pune-le în **ordinea preferinței reale** și fă lista lungă.

**2. Verifică ERATA la broșură.**
În fiecare an apare un document de corecții. În 2026 a **înjumătățit** locurile la exact
specializarea unde a ajuns copilul și a creat un cod care nu exista în broșură.

**3. Pragurile de anul trecut nu se compară direct.**
Numărul de candidați se schimbă de la an la an. În 2026 cohorta a scăzut cu ~11%, iar
pragurile au coborât cu până la **1 punct** la partea de jos. AI-ul știe cum să facă
conversia corect.

**4. Termenele fatale sunt scurte și se pierd ușor.**
- Depunerea dosarului la liceul repartizat: **6 zile** — dacă n-o faci, **pierzi locul**.
- Etapa „situații speciale": **2 zile**, cu upload online închis la **ora 14:00**.
- 🔴 **În 2026 acest al doilea termen a fost pierdut.** Pregătește dosarul din timp.

**5. Dacă vrei o școală mai aproape de casă, ruta corectă e „apropiere de domiciliu".**
Se depune la **29–30 iulie** și — spre deosebire de etapa a II-a — **nu renunți la locul
pe care îl ai deja**. Dacă cererea reușește te muți, dacă nu, rămâi unde ești.
Pregătește dosarul **înainte** să afli rezultatul.

**6. „Mai aproape" nu înseamnă „mai slab".**
Verifică rata de promovare la BAC pe **ultimii 3 ani**, nu pe unul singur. În 2026 mai
multe școli **mai apropiate** de casă aveau rezultate **mai bune** decât cea repartizată.

---

## Calendarul 2027 (din proiectul de ordin — de reverificat)

| Când | Ce se întâmplă |
|---|---|
| **septembrie 2026** | verifică apariția **ordinului final** cu regulile pentru 2027 |
| toamna 2026 | *(dacă e cazul)* începe evaluarea CES la CJRAE — durează luni |
| iarna 2026–2027 | decizi: concurs de admitere? aptitudini? bilingv? |
| februarie–martie | simularea Evaluării Naționale — primul reper realist |
| până la ~15 iunie | *(doar CES)* depunerea certificatului CJRAE la școală ← termen fatal |
| **22–25 iunie 2027** | **Evaluarea Națională** |
| 7 iulie | rezultate finale |
| 8 iulie · **9 și 12 iulie** | înscriere și **probele concursului organizat de licee** |
| 15 iulie | rezultate finale la concurs |
| 16 și 19–22 iulie | completarea fișei de opțiuni |
| **26 iulie** | **repartizarea computerizată** |
| **27–28 iulie** | **depunerea dosarului la liceu** ← termen fatal |
| sfârșit de iulie | lista locurilor libere → etapa „situații speciale" ← fereastră de 2 zile |
| august | etapa a II-a |

> ⚠️ Datele de mai sus sunt din **proiectul** de calendar. Descarcă întotdeauna
> ordinul final al anului și înlocuiește-le.

---

## Dacă copilul are CES — de citit neapărat

Runda CES e **separată și mai devreme** decât cea generală, iar locurile CES sunt
**suplimentare** (peste cele din plan).

Două lucruri esențiale:

1. **Certificatul CJRAE/CMBRAE trebuie depus la școala de proveniență până la termenul
   din calendar** (15 iunie în 2026). Fără el, locurile CES sunt inaccesibile — inclusiv
   în etapele de mai târziu.

2. **Nu trata runda CES ca pe o plasă de siguranță.** În 2026 s-a înfundat serios:

   | | 2025 | 2026 |
   |---|---|---|
   | Candidați CES | 553 | 737 |
   | Nerepartizați | 6 | **186** |
   | Rată de plasare | 98,9% | **74,8%** |

   Dacă rămâi nerepartizat în runda CES **nu pierzi nimic** — intri automat în runda
   generală. Dar trebuie să ai pregătită și o fișă generală completă.

---

## Întrebări frecvente

**Pot începe acum, deși copilul nu are încă nicio notă de la Evaluarea Națională?**
Da — și e cel mai bun moment. Aproximativ **90%** din analiză nu depinde de notă: lista
școlilor, timpii de navetă, rezultatele lor la BAC, deciziile despre concurs / aptitudini /
bilingv, demararea unui eventual dosar CES. Nota se folosește abia la final, ca să alegi
dintre listele deja pregătite.

**Și atunci cum știu ce școli să pun pe listă, dacă nu știu nota?**
Se lucrează pe **trei scenarii** — pesimist, realist, optimist — construite în jurul
rezultatului de la **simularea** din februarie–martie (cel mai bun reper disponibil).
În iulie alegi lista potrivită. Atenție: notele din școală sunt de regulă mai mari decât
cele obținute efectiv la Evaluarea Națională, deci nu te baza pe ele.

**Câte opțiuni pun în fișă?**
Cât mai multe. În 2026 s-au folosit 308. Nu există dezavantaj, iar riscul de a rămâne
nerepartizat scade spre zero.

**Contează media din clasele V–VIII?**
Nu la calculul mediei de admitere (aceea e 100% Evaluarea Națională). Contează doar la
**departajarea** candidaților cu medii identice — și acolo e primul criteriu.

**Pot afla dinainte unde va ajunge copilul?**
Aproximativ, da. Fișierul pentru AI conține o metodă de simulare. În 2026 a prezis
**corect școala**. Dar tratează rezultatul ca pe o orientare, nu ca pe o certitudine.

**Ce fac dacă rezultatul nu-mi convine?**
Vezi secțiunea §11 din fișierul pentru AI. Pe scurt: ruta cea mai bună e
**„apropiere de domiciliu"** (29–30 iulie), pentru că nu-ți pierzi locul actual.
</content>
