# Sesiunea 22: Plotly pentru Vizualizări Interactive

## 1. Concepte Cheie și Paradigma Plotly
* **Interactivitate Nativă**: Spre deosebire de Matplotlib/Seaborn care randează imagini statice pixelate, Plotly generează grafice bazate pe tehnologii web (HTML5, JavaScript, WebGL prin biblioteca `plotly.js`).
* **Modul Hover & Tooltips**: Trecerea cursorului peste puncte activează ferestre informative care afișează dinamic coordonatele și metadatele asociate înregistrării.
* **Componentele de Control Incorporate**: Toate figurile dețin un meniu automat în colțul din dreapta sus (Modebar) ce permite operațiuni de Zoom In/Out, Pan (deplasare), Box Select, Lasso Select și auto-scalare.
* **Plotly Express vs Graph Objects**:
    * **`plotly.express` (px)**: Interfață de nivel înalt optimizată pentru structuri de date de tip Tidy DataFrame (similară cu design-ul Seaborn). Creează figuri complexe dintr-o singură linie de cod.
    * **`plotly.graph_objects` (go)**: API de nivel jos care oferă control absolut asupra fiecărui nod din dicționarul JSON al figurii. Recomandat pentru tipuri de grafice personalizate, animații complexe sau dashboard-uri structurate manual.

## 2. Structura și Tipuri de Grafice Incluse
1. **`px.line`**: Randează grafice temporale sau secvențiale, suportând argumentul `markers=True` pentru puncte de legătură evidențiate.
2. **`px.bar`**: Generează diagrame cu bare unde argumentul `color` poate mapa palete de culori direct pe categoriile axei X.
3. **`px.scatter`**: Plotare bidimensională unde fiecare punct păstrează legături interactive de hover.
4. **`px.box` & `px.violin`**: Instrumente statistice de vizualizare a distribuției; funcția de violin permite activarea parametrului `points="all"` pentru randarea transparentă a populației de date.
5. **`go.Heatmap`**: Reprezentare matriceală cromatică bazată pe scări de culoare continue (ex: *Viridis*, *Cividis*, *Coolwarm*).
6. **`px.pie`**: Diagramă circulară controlată prin parametrii structurali `names` și `values`.
