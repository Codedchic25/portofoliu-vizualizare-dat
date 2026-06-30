# Sesiunea 24: Streamlit cu Interfețe de Machine Learning

## 1. Concepte Algoritmice Prototipate
* **Regresie Liniară (`LinearRegression`)**: Model statistic utilizat pentru a prezice o variabilă dependentă continuă (`salariu`) pe baza unei variabile independente (`experienta`).
* **Arbori de Decizie (`DecisionTreeClassifier`)**: Algoritm de învățare supervizată folosit pentru clasificare binară. Împarte setul de date pe baza unor reguli logice obținute din caracteristici (`medie`, `activități`, `recomandare`).
* **Tratarea Tipurilor de Date**: Widget-urile de tip `st.checkbox` returnează valori booleene (`True`/`False`). Algoritmii Scikit-Learn necesită conversie numerică strictă (`int()`), transformându-le în stări binare (`1`/`0`).

## 2. Arhitectura de Execuție în Streamlit
* Streamlit re-rulează scriptul de sus în jos la fiecare modificare a interfeței. Pentru a evita re-antrenarea modelelor la fiecare mișcare de slider, codul greu de Machine Learning se plasează în afara buclei UI sau se protejează prin mecanisme de caching.
