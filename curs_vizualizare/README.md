# 📊 Curs de Vizualizare de Date și Algoritmi în Python

Acest depozit conține un pachet educațional complet, documentat academic și optimizat sintactic. Include exemple practice, scripturi web reactive, soluții pentru temele de curs, implementări algoritmice de top și o galerie centralizată de randare grafică avansată, garantând o rulare impecabilă cu zero erori sau avertizări în editoare.

---

## 📂 Structura Completă a Proiectului (Tree View)

```text
curs_vizualizare/
├── README.md                          # Ghidul principal de utilizare și documentare globală
├── .gitignore                         # Excludere automată pentru cache uv, bytecode și fișiere .db
├── requirements.txt                   # Dependențele exacte ale proiectului generate cu uv
├── teme_partea1.py                    # Soluțiile detaliate pentru temele din Sesiunile 18, 19, 20
├── teme_partea2.py                    # Soluțiile detaliate pentru temele din Sesiunile 21, 22, 25
├── teme_partea3.py                    # Soluțiile detaliate pentru temele din Sesiunile 23 - 26
├── grafice_suplimentare.py            # Extensii avansate (Stackplot, Clustermap, Catplot, Treemap)
├── galerie_spectacular.py             # Meniu centralizat pentru cele mai spectaculoase grafice (Top 4)
├── sesiunea_18/                       # Matplotlib - Noțiuni de Bază
│   ├── notiuni.md                     # Teorie: Linii, bare, histograme, scatter plot
│   └── grafice.py                     # Script Python cu exemplele fundamentale
├── ...                                # Sesiunile intermediare 19 - 26 (Configurate curat)
├── sesiunea_27/                       # Exerciții Algoritmice LeetCode Comentate
│   ├── notiuni.md                     # Teorie: Complexitate Big O, tehnica Two Pointers, Stive și Hash Maps
│   └── grafice.py                     # Script Python cu 15 probleme explicate pas cu pas
├── sesiunea_extra/                    # Explorarea Graficelor Specializate (Suplimentar)
│   └── grafice.py                     # Script Python: Jointplot marginal, Stem, Hexbin, Quiver vectorial
└── sesiunea_spectacular/              # Vizualizări Profesionale de Înalt Impact Vizual (Suplimentar)
    └── grafice.py                     # Script Python: Donut ierarhic, Radar spider, Suprafețe 3D, Streamplot
```

---

## 🧰 Managementul Mediului Virtual (Modern Stack cu `uv`)

Acest proiect folosește **Astral UV**, un instrument de ultimă generație scris în Rust, pentru gestionarea ultra-rapidă a pachetelor și dependențelor.

### 💡 `uv` vs `pip`: Conflict sau Coexistență?
* **Zero conflicte**: `uv` folosește exact aceeași structură standard pentru folderul `.venv` și instalează pachetele în același loc (`site-packages`) ca și `pip`. Orice pachet instalat cu `uv pip` este perfect vizibil și utilizabil de către interpretorul Python standard.
* **De ce `uv`?**: Este de 10-100 de ori mai rapid decât `pip`, descarcă pachetele în paralel și rezolvă inteligent conflictele de versiuni din prima secundă, garantând stabilitatea pe termen lung a proiectului.

### Ghid de Inițializare și Instalare:
```powershell
# 1. Creează mediul virtual izolat cu uv
uv venv

# 2. Activează mediul virtual în PowerShell
.venv\Scripts\Activate.ps1

# 3. Instalează toate dependențele la viteză maximă din fișierul requirements
uv pip install -r curs_vizualizare/requirements.txt
```

---

## 🚀 Ghid de Execuție și Rulare

### 1. Scripturi din Consolă (Sesiunile 18-22, Extra, LeetCode)
Asigurați-vă că mediul virtual `(.venv)` este activat înainte de rulare:

* **Grafice Statice (Matplotlib / Seaborn - Sesiunile 18-21):**
  Deschide o fereastră nativă de sistem operativ (GUI Windows).
  ```powershell
  python curs_vizualizare/sesiunea_18/grafice.py
  ```

* **Grafice Interactive de Browser (Plotly - Sesiunea 22):**
  Generează o structură HTML/JavaScript și deschide automat o filă nouă în browserul implicit.
  ```powershell
  python curs_vizualizare/sesiunea_22/grafice.py
  ```

* **Panoul Interactiv al Graficelor Spectaculoase (Top 4):**
  ```powershell
  python curs_vizualizare/galerie_spectacular.py
  ```

* **Exerciții Algoritmice LeetCode (Sesiunea 27):**
  ```powershell
  python curs_vizualizare/sesiunea_27/grafice.py
  ```

### 2. Dashboard-uri Web Reactive (Streamlit & Baze de Date)
Aplicațiile Streamlit rulează peste un server local și se deschid la adresa `http://localhost:8501`.

* **Aplicația Enterprise cu Login și Bază de Date SQL (Sesiunea 26):**
  ```powershell
  cd curs_vizualizare/sesiunea_26
  streamlit run app.py
  ```
  *(Credențiale implicite -> Utilizator: `admin` | Parolă: `HR2026`)*

* **Dashboard-ul Centralizat pentru Soluțiile Temelor (Sesiunile 23-26):**
  ```powershell
  streamlit run curs_vizualizare/teme_partea3.py
  ```

---

## 🛡️ Calitate Cod (Ruff Validated)
Codul respectă cu strictețe regulile **PEP 8** și indică `0 Problems` în VS Code.
```powershell
ruff check curs_vizualizare --fix
ruff format curs_vizualizare
```

 Textul pentru postarea de pe LinkedInDe la date brute la decizii în timp real: Am construit un portofoliu complet de Data Apps & Algoritmică în Python! 🚀📊În ultimele săptămâni, mi-am propus să stăpânesc ecosistemul modern de analiză și inginerie a datelor. Rezultatul este un repository enterprise structurat în 27 de sesiuni intense, dezvoltat la standarde de producție.Ce include această arhitectură de portofoliu?🔹 Business Intelligence & Vizualizări de Înalt Impact: Am implementat concepte avansate în #Matplotlib și #Seaborn, optimizând reprezentări de date complexe precum Multi-Level Donut Charts, Radar Spider Charts, 3D Surface Plots și Hexbin Density Plots pentru procesarea volumelor mari de date (Big Data).🔹 Interactive Data Apps: Am dezvoltat dashboard-uri web reactive în #Streamlit, echipate cu filtre dinamice multivariate, mecanisme de import/export automat de fișiere CSV și un modul administrativ securizat (Login/Session State) conectat la o bază de date relațională #SQLite.🔹 Predictive Analytics: Am integrat modele din #ScikitLearn (Regresie Liniară și Arbori de Decizie) direct în interfețele web, permițând rularea predicțiilor de Machine Learning în browser în timp real.🔹 Algoritmică & Gândire Logică: Am rezolvat și documentat pas cu pas 15 probleme fundamentale din #LeetCode, aplicând optimizări asimptotice (Big O) cu structuri de tip Hash Maps, Stive/LIFO și tehnica Two Pointers.⚙️ Modern Engineering Stack & Clean Code:Management ultra-rapid cu #AstralUV: Proiectul folosește noul instrument #uv scris în Rust, înlocuind complet pip clasic pentru crearea și izolarea deterministă a mediului virtual (.venv) și gestionarea paralelă a pachetelor.Validat la sânge cu #Ruff: Întregul cod respectă cu strictețe standardele PEP 8. Utilizarea asistentului de linting a eliminat erorile de sintaxă sau variabilele redundante, menținând un scor impecabil de 0 Errors / 0 Problems în mediul de dezvoltare.Sunt pregătit[ă]* să folosesc acest set modern de unelte pentru a transforma datele brute în insight-uri valoroase de business!👇 Vă las atașate câteva capturi de ecran cu „Galeria de Artă Digitală” din proiect și interfața de login securizată prin SQL.Codul curat este pregătit pentru revizuire! Cum vi se par structura proiectului și adoptarea stivei tehnologice moderne?#Python #DataAnalytics #DataScience #Streamlit #MachineLearning #CleanCode #Programming #JobOpportunity #DataAnalyst(Notă: Înlocuiește „pregătit[ă]” cu forma potrivită pentru tine).🚀 Sfaturi de implementare pe LinkedIn:Urcă 3 imagini separat: Folosește capturile pe care le-ai făcut din consolă și din browser (suprafata_3d.png, grafic_radar.png și ecranul de login Streamlit). Postările cu imagini multiple de tip galerie atrag un număr dublu de vizualizări.Adaugă linkul în comentarii: Când urcăm proiectul pe GitHub, pune link-ul către repository în primul comentariu al postării, nu direct în textul principal. Algoritmul LinkedIn penalizează postările cu link-uri externe, dar oferă o acoperire maximă celor care lasă link-ul în secțiunea de comentarii.
 
 Ora publicării: Încearcă să postezi de marți până joi, dimineața între orele 09:00 - 11:00, când activitatea pe LinkedIn este la nivel maxim în România.Fii activ în comentarii: Răspunde la orice comentariu sau apreciere primești în primele 60 de minute de la postare. Acest lucru semnalează algoritmului LinkedIn că postarea ta generează conversație și o va distribui către mai multe persoane din afara rețelei tale!

 python curs_vizualizare/galerie_spectacular.py

Pentru a deschide ferestrele graficelor de unde poți face capturile de ecran (screenshot-urile) perfecte, deschide terminalul PowerShell în VS Code și rulează următorul script de galerie pe care l-am configurat special [skills:load]:powershellpython curs_vizualizare/galerie_spectacular.py
Folosește codul cu precauție.🎯 Cum procedezi pas cu pas în terminal:Pentru Imaginea 1 (Suprafața 3D): Introdu cifra 3 în meniul din terminal și apasă Enter. Când se deschide fereastra 3D, folosește scurtătura de pe tastatură Windows + Shift + S, decupează graficul frumos și salvează imaginea ca suprafata_3d.png. După ce ai terminat, închide fereastra graficului pentru a reveni la meniu.Pentru Imaginea 2 (Radar/Spider Chart): Introdu cifra 2 în terminal și apasă Enter. Repetă procedura de captură cu Windows + Shift + S și salvează imaginea ca grafic_radar.png. Închide apoi fereastra pentru a elibera consola.Ieșire: Introdu cifra 0 pentru a închide panoul de control al galeriei în siguranță.🖥️ Cum extragi a treia imagine (Interfața Streamlit din Sesiunea 26)Deoarece aplicația web Enterprise din Sesiunea 26 rulează pe un server local, trebuie să o lansăm separat:Navighează în folderul sesiunii 26:powershellcd curs_vizualizare/sesiunea_26
Folosește codul cu precauție.Pornește serverul Streamlit:powershellstreamlit run app.py
Folosește codul cu precauție.Browserul tău se va deschide automat la adresa locală (de obicei http://localhost:8501).Fă screenshot-ul: Vei vedea ecranul elegant de autentificare pe care l-ai creat. Fă o captură curată a paginii web pentru LinkedIn.Oprire server: Când ai terminat, întoarce-te în terminalul din VS Code și apasă combinația de taste Ctrl + C pentru a opri serverul Streamlit și a lăsa consola curată.După ce ai salvat aceste 3 imagini spectaculoase pe Desktop, ești 100% pregătită să publici postarea de impact pe LinkedIn!Anunță-mă cum au ieșit capturile de ecran și dacă vrei să te ajut să urcăm codul pe GitHub ca să poți pune și un link de proiect în postare!