# Sesiunea 23: Crearea unui Dashboard Interactiv cu Streamlit

## 1. Concepte Fundamentale
* **Paradigma Streamlit**: Biblioteca elimină necesitatea scrierii de cod de tip arhitectură Client-Server (Frontend/Backend separado). Orice modificare a unui widget (slider, multiselect) determină reexecutarea de sus în jos a întregului script Python cu noile valori preluate automat.
* **Sistemul de Widget-uri**: Elementele precum `st.multiselect` sau `st.slider` acționează dublu: ca element de interfață grafică și ca variabilă Python ce stochează inputul curent al utilizatorului.
* **Randarea Graficelor Externe**: Pentru biblioteci bazate pe Matplotlib/Seaborn, Streamlit necesită transmiterea explicită a obiectului figură (`plt.subplots()`) prin intermediul funcției dedicate `st.pyplot(fig)`. Pentru grafice native, se folosesc funcții optimizate rapid ca `st.bar_chart()`.
* **Afișarea KPI-urilor**: Componenta `st.metric` oferă un layout curat și pre-stilizat corporativ pentru afișarea indicatorilor cheie de performanță (valoare principală, etichetă și indicator opțional de creștere/scădere).

## 2. Comenzi de Terminal Esențiale
* Instalați pachetul în mediu: `pip install streamlit`
* Rulați serverul local de dezvoltare: `streamlit run app.py`
