# Citește mai întâi — Admitere Liceu București

Ediția **21 octombrie 2026**. Acesta este un instrument de organizare pentru
familii, nu o publicație oficială și nici o garanție de admitere.

## 1. Deschide fișierul potrivit

| Moment | Fișier |
| --- | --- |
| În timpul anului școlar | [02_ANUL_PREGATITOR.md](02_ANUL_PREGATITOR.md) |
| Analiza opțiunilor și verificarea fișei | [01_PROMPT_COMPLET_PENTRU_AI.md](01_PROMPT_COMPLET_PENTRU_AI.md) |
| Verificarea regulilor pentru 2027 | [SURSE_2027.md](SURSE_2027.md) |
| Lucru într-un tabel | [modele/README.md](modele/README.md) |

Ghidurile sunt fișiere text Markdown (`.md`): le poți deschide într-un editor de
text sau copia într-un chat. Un asistent cu acces la web și fișiere poate ajuta
la verificări. Nu ai nevoie de Python pentru a citi sau completa șabloanele.

Poți începe conversația cu:

> „Ajută-mă să organizez opțiunile pentru admiterea la liceu în București.
> Verifică întâi sursele oficiale din SURSE_2027.md. Spune ce este confirmat,
> ce este proiect și ce lipsește. Nu cere date care încă nu există.”

## 2. Verifică sursele înainte de calendar

La data ediției am identificat o consultare ministerială din **5 octombrie 2026**.
Nu confirmăm prin ea existența unui ordin final. Nu folosi datele din proiectul
din august sau din anul precedent drept termene pentru 2027.

Descarcă din surse oficiale ordinul și anexele anului curent, broșura și erata
ISMB. Notează în [modele/termene.csv](modele/termene.csv) anul școlar, documentul,
data exactă și stadiul verificării. Cere confirmarea școlii/inspectoratului dacă
nu poți stabili o condiție de participare sau un termen.

## 3. Pregătește analiza fără date personale inutile

Începe cu profilurile dorite, materiile preferate, durata maximă a navetei și
o zonă aproximativă de plecare. Verifică rutele exacte local, în aplicația de hărți.
În timpul anului folosește scenarii de note. După rezultate poți adăuga media
și poziția în ierarhie.

Nu publica numele copilului, codul candidatului, adrese, rezultate individuale
sau documente CES. Pentru discuții despre pașii CES este suficient să precizezi
dacă dorești informații despre acea rută; nu trimite diagnostice ori certificate
unui asistent AI.

## 4. Șapte verificări utile

1. Compară opțiunile în **ordinea preferinței reale**, folosind mecanismul confirmat
   pentru anul curent. Include suficiente alternative pe care le-ai accepta.
2. Verifică fiecare cod în broșura **anului curent**, împreună cu erata.
3. Separă pragurile generale de pragurile CES și de eventualele alte rute.
4. Tratează pragurile istorice ca repere: cohorta, locurile și preferințele se schimbă.
5. Notează separat termenele de înscriere, probe, corecturi și depunere a dosarului.
6. Confirmă condițiile oricărei etape ulterioare, inclusiv efectul asupra locului
   deja obținut. Nu presupune că o cerere de redistribuire păstrează automat locul.
7. Verifică sursa indicatorilor BAC și naveta pentru lista scurtă. Istoricul BAC
   corectat din pachet are surse pe școală, dar acoperire limitată.

## 5. Ce pot spune datele și simularea

ZIP-ul include agregate istorice și ancore de ierarhie, cu limite descrise în
[date_istorice/README.md](date_istorice/README.md). Nu conține liste individuale
de candidați. Numărul total de locuri din oraș nu garantează un loc într-o listă
restrânsă de preferințe.

Simulatorul generează preferințe necunoscute după un model simplificat. Procentul
unui rezultat este frecvența lui **în model**, nu probabilitatea reală de admitere.
Nici 0%, nici 100% într-o simulare nu constituie o garanție. Nu renunța la opțiuni
doar pe baza lui.

## 6. La final

Compară fișa cu tabelul **cod cu cod și poziție cu poziție**, elimină duplicatele,
verifică eligibilitatea și confirmă depunerea prin canalul oficial. Șabloanele
din pachet sunt instrumente personale; nu înlocuiesc formularele oficiale.
