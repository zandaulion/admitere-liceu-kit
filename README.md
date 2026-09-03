# Admitere Liceu Kit 🎓

> **Metodă completă, date istorice, scripturi de analiză și prompturi AI pentru admiterea la liceu și Evaluarea Națională (București — 2027).**

Acest depozit conține **metoda completă** folosită de o familie din București în ciclul de admitere 2026, structurată astfel încât să poată fi preluată de orice familie cu ajutorul unui asistent AI pentru ciclul de admitere 2027.

Nu trebuie să știi programare. Trebuie doar să încarci fișierul potrivit într-un asistent AI (ChatGPT, Claude, Gemini etc.) și să-i răspunzi la câteva întrebări.

---

## 📂 Structura pachetului

| Fișier / Folder | Descriere | Când se folosește |
|---|---|---|
| [**`00_CITESTE_MAI_INTAI.md`**](00_CITESTE_MAI_INTAI.md) | Ghidul introductiv esențial și cele 7 reguli de aur | **Acum** |
| [**`02_ANUL_PREGATITOR.md`**](02_ANUL_PREGATITOR.md) | ⭐ Tot ce se pregătește în timpul anului școlar, înainte de examen | **Septembrie 2026 – Iunie 2027** |
| [**`01_PROMPT_COMPLET_PENTRU_AI.md`**](01_PROMPT_COMPLET_PENTRU_AI.md) | Playbook-ul detaliat pentru asistentul AI | **Iulie 2027 (după examen)** |
| [**`date_istorice/`**](date_istorice/) | Date gata extrase: praguri 2024–2026, curbe de ierarhie, BAC 2018–2026, statistici CES | Oricând |
| [**`scripturi/`**](scripturi/) | Programe Python reutilizabile pentru procesare de broșuri, ierarhii și simularea repartizării | Oricând |

---

## 🔴 Noutate critică: Schimbarea din 2027

Generația 2027 este **prima sub noua lege a învățământului**:
- **Liceele pot organiza concurs propriu de admitere** pentru până la **50%** din locuri.
- Participarea este **opțională și fără risc** — dacă nu ești admis, intri normal în repartizarea computerizată.
- Condiție de înscriere: **minimum nota 5 la fiecare probă** de la Evaluarea Națională.
- *Dacă un liceu dorit organizează concurs și nu participi, îți înjumătățești șansele la acel liceu.*

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
