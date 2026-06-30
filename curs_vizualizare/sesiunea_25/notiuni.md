# Sesiunea 25: Dashboard-uri Profesionale și Profilare Automatizată

## 1. Concepte de Analiză și Automatizare
* **Profilare Automatizată (`ydata-profiling`)**: Instrument avansat de Data Science care înlocuiește analiza exploratorie manuală. Generează automat metrici statistice de bază, distribuții, semnalări de valori lipsă (Missing Values) și corelații multivariate printr-o singură linie de cod.
* **Filtrare Dinamică pe Tipuri de Date**: Programarea defensivă presupune separarea dinamică a coloanelor unui DataFrame încărcat la runtime:
    * Variabilele de tip text (`object`) sunt mapate pe interfețe de selecție multiplă (`st.multiselect`).
    * Variabilele numerice (`int`/`float`) sunt mapate pe intervale cu dublu selector (`st.sidebar.slider` pasat ca tuplu).
* **Securizarea Corelațiilor**: Generarea unei matrici de corelație (`.corr()`) pe un fișier CSV încărcat arbitrar de un utilizator va eșua în versiunile moderne de Pandas dacă setul conține text, făcând obligatorie utilizarea parametrului `numeric_only=True`.

## 2. Pachete Necesare (Terminal)
* Pentru instalarea extensiilor de profilare din proiect:
  ```bash
  pip install ydata-profiling streamlit-pandas-profiling
  ```
