# Admitere Liceu Kit 🎓

> **Metodă completă, date istorice, scripturi de analiză și prompturi AI pentru admiterea la liceu și Evaluarea Națională (București — 2027).**

Acest depozit conține **metoda completă** folosită de o familie din București în ciclul de admitere 2026, structurată astfel încât să poată fi preluată de orice familie cu ajutorul unui asistent AI pentru ciclul de admitere 2027.

Nu trebuie să știi programare. Trebuie doar să încarci fișierul potrivit într-un asistent AI (ChatGPT, Claude, Gemini etc.) și să-i răspunzi la câteva întrebări.

---



[Optional Python setup / configurarea scripturilor](SCRIPTURI.md) · [Historical data provenance](date_istorice/README.md)

## In English

Romanian-language guides, historical aggregate data and optional Python tools for
Bucharest high-school admissions planning. Families can start with the linked
Romanian guide without programming. Historical cutoffs are context, not a promise
of admission; current official rules and calendars take precedence.
[Public overview](https://zandaulion.com/admitere.html).

## 📂 Structura pachetului

| Fișier / Folder | Descriere | Când se folosește |
|---|---|---|
| [**`00_CITESTE_MAI_INTAI.md`**](00_CITESTE_MAI_INTAI.md) | Ghidul introductiv esențial și cele 7 reguli de aur | **Acum** |
| [**`02_ANUL_PREGATITOR.md`**](02_ANUL_PREGATITOR.md) | ⭐ Tot ce se pregătește în timpul anului școlar, înainte de examen | **Septembrie 2026 – Iunie 2027** |
| [**`01_PROMPT_COMPLET_PENTRU_AI.md`**](01_PROMPT_COMPLET_PENTRU_AI.md) | Playbook-ul detaliat pentru asistentul AI | **Iulie 2027 (după examen)** |
| [**`date_istorice/`**](date_istorice/) | Date gata extrase: praguri 2024–2026, curbe de ierarhie, BAC 2018–2026, statistici CES | Oricând |
| [**`scripturi/`**](scripturi/) | Programe Python reutilizabile pentru procesare de broșuri, ierarhii și simularea repartizării | Oricând |

---

## 🔴 Reguli pentru 2027: verifică sursa și stadiul

**Notă de verificare — 20 octombrie 2026:** Ministerul a publicat la 14 august
2026 [proiectul metodologiei pentru 2027–2028, în consultare publică](https://edu.ro/press_rel_60_2026_consultare_publica_proiect_metodologie_calendar_AdLic_27_28).
Sursa citată aici este un proiect; acest depozit nu confirmă prin acea pagină că
toate prevederile au fost adoptate în forma finală. Înaintea unei decizii, verifică
ordinul final, calendarul, broșura și erata anului curent pe site-urile oficiale.

Proiectul descrie următoarea posibilitate pentru 2027:
- **Liceele pot organiza concurs propriu de admitere** pentru până la **50%** din locuri.
- Participarea este **opțională și fără risc** — dacă nu ești admis, intri normal în repartizarea computerizată.
- Condiție de înscriere: **minimum nota 5 la fiecare probă** de la Evaluarea Națională.
- Dacă un liceu organizează concurs, verifică numărul efectiv de locuri rămas
  pentru fiecare rută. O cotă de locuri nu măsoară probabilitatea individuală de admitere.

---

## 🚀 Cum se folosește (în 3 pași)

1. **Alege un asistent AI:**
   - Orice chat web cu suport pentru upload de fișiere, rulare de cod și căutare web este suficient.
   - Singura acțiune manuală: descarcă broșura ISMB + erata de pe site-ul inspectoratului și încarcă-le în chat.
2. **Furnizează documentul potrivit momentului:**
   - În timpul clasei a VIII-a: trimite `02_ANUL_PREGATITOR.md` cu mesajul:
     > *„Suntem la începutul clasei a VIII-a. Ajută-mă să parcurg ce scrie în acest document pentru copilul meu.”*
   - În iulie (după afișarea notelor): trimite `01_PROMPT_COMPLET_PENTRU_AI.md` cu mesajul:
     > *„Urmează instrucțiunile din acest document pentru copilul meu. Începe prin a-mi cere datele de care ai nevoie.”*
3. **Pregătește datele din timp:**
   - Adresa de domiciliu (pentru calcularea timpilor de navetă către licee).
   - Profilul dorit și materiile preferate / de evitat.
   - Rezultatul la **simularea** din februarie–martie (reperul cel mai apropiat de realitate).
   - Documentația CES (dacă este cazul — evaluarea la CJRAE/CMBRAE durează luni de zile).

---

## 🧠 Cele 7 principii de bază

1. **Nota de la Evaluarea Națională dictează spațiul de opțiuni:** O jumătate de punct în plus poate muta un elev cu 600–1.800 de poziții în ierarhie.
2. **Fișa lungă nu costă nimic:** Pune opțiunile în ordinea reală a preferințelor, oricât de ambițioase ar fi cele de sus. Repartizarea acordă prima opțiune disponibilă.
3. **Verifică întotdeauna ERATA la broșură:** În fiecare an apar modificări neanunțate sau reduceri de locuri.
4. **Pragurile de anul trecut nu se compară brut:** Variația numărului de elevi dintr-o generație deplasează pragurile (ex. în 2026 pragurile au coborât cu până la 1 punct).
5. **Termenele fatale sunt stricte:** Depunerea dosarului se face în câteva zile; depășirea termenului duce la pierderea locului.
6. **Ruta „apropiere de domiciliu” nu pierde locul obținut:** Spre deosebire de etapa a II-a, permite cererea de transfer fără a risca locul deja repartizat.
7. **Verifică evoluția la BAC pe ultimii 3 ani:** Nu te baza pe reputația istorică a liceului sau pe un singur an.

---

## 🛠️ Date istorice și Scripturi

În folderul [`date_istorice/`](date_istorice/) se găsesc:
- `praguri_2025_din_brosura2026.json` — 405 specializări cu locuri și praguri
- `ces_praguri_2024_2025_2026.json` — analiză pe 3 ani a locurilor și pragurilor CES
- `ierarhie_ancore_2025_2026.json` — curbe poziție-notă pentru calibrarea pragurilor
- `bac_istoric_licee.json` — rate de promovare și medii BAC (2018–2026)
- `brosura_2026_originala.pdf` și `locuri_libere_2026.xlsx`

În folderul [`scripturi/`](scripturi/):
- `parse_brosura.py` — extractor de date din broșura oficială
- `ierarhie.py` — interpolare și conversie note/poziții
- `simulare_repartizare.py` — algoritm de simulare a repartizării pe baza preferințelor

---

## 📄 Licență

Acest proiect este licențiat sub licența [MIT](LICENSE) — liber de utilizat, modificat și distribuit de către oricine dorește să-și ajute copilul sau comunitatea.


## Support and contributions

Use this repository’s Issues for reproducible bugs and focused feature requests. Include the version, relevant runtime/browser, expected behavior and a minimal synthetic example. Remove credentials, personal records, device identifiers and deployment-specific values before sharing logs or screenshots.

For a correction to admissions guidance or data, include the official source URL, year and the exact aggregate field or paragraph affected. Do not submit individual applicant records.

Keep changes focused and update the affected documentation. Security-sensitive reports should follow [SECURITY.md](SECURITY.md).
