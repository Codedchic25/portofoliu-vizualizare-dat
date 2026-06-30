#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 24: Aplicații Avansate Streamlit cu Machine Learning.

Implementează o aplicație web reactivă care utilizează algoritmi de
regresie liniară și clasificare pentru predicții în timp real.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ------------------------------------------------------------------
# CONFIGURARE STATE ȘI ANTRENARE MODELE (Se execută o singură dată)
# ------------------------------------------------------------------
np.random.seed(1)

# 1. Pregătire Model Regresie (Salarii)
exp_ani = np.random.randint(1, 15, 100)
sal_ron = np.random.randint(3000, 15000, 100)
structura_regresie = {"experienta": exp_ani, "salariu": sal_ron}
df_regresie = pd.DataFrame(structura_regresie)

X_reg = df_regresie[["experienta"]]
y_reg = df_regresie["salariu"]
model_regresie = LinearRegression()
model_regresie.fit(X_reg, y_reg)

# 2. Pregătire Model Clasificare (Admitere)
pop_medie = np.random.uniform(5, 10, 200)
pop_activ = np.random.randint(0, 2, 200)
pop_recom = np.random.randint(0, 2, 200)
pop_admis = np.random.randint(0, 2, 200)

structura_clasificare = {
    "medie": pop_medie,
    "activitati": pop_activ,
    "recomandare": pop_recom,
    "admis": pop_admis,
}
df_clasificare = pd.DataFrame(structura_clasificare)

X_clf = df_clasificare[["medie", "activitati", "recomandare"]]
y_clf = df_clasificare["admis"]
X_train, X_test, y_train, y_test = train_test_split(
    X_clf, y_clf, test_size=0.2, random_state=42
)

model_clasificare = DecisionTreeClassifier(random_state=42)
model_clasificare.fit(X_train, y_train)


# ------------------------------------------------------------------
# INTERFAȚA WEB INTERACTIVĂ (STREAMLIT UI)
# ------------------------------------------------------------------
def ruleaza_aplicatia():
    """Randează elementele vizuale și colectează inputurile în timp real."""
    st.title("🔢 Sistem Inteligent de Predicții cu Machine Learning")

    opțiuni_meniu = ["Salariu", "Admitere"]
    optiune = st.selectbox("Alege tipul de predicție:", opțiuni_meniu)

    if optiune == "Salariu":
        st.subheader("📈 Predicție Salariu după Experiență")

        # Widget-ul colectează inputul utilizatorului
        ani_experienta = st.slider("Experiență (ani)", 1, 15, 3)

        # Izolarea datelor de intrare pentru predicție
        input_regresie = [[ani_experienta]]
        predictie_salariu = model_regresie.predict(input_regresie)[0]

        st.success(f"Salariul estimat: {int(predictie_salariu)} RON")

        # Integrare grafică Matplotlib statică inter-conectată
        st.write("---")
        st.subheader("Grafic de control: Salarii vs Experiență")

        fig, ax = plt.subplots()
        ax.scatter(X_reg, y_reg, color="blue", alpha=0.5, label="Date Reale")

        linii_predictie = model_regresie.predict(X_reg)
        ax.plot(X_reg, linii_predictie, color="red", label="Linia de Regresie")

        # Afișarea punctului curent selectat pe slider
        ax.scatter(
            [ani_experienta],
            [predictie_salariu],
            color="green",
            s=150,
            zorder=5,
            label="Selecția ta",
        )

        ax.set_xlabel("Experiență (ani)")
        ax.set_ylabel("Salariu (RON)")
        ax.legend()
        st.pyplot(fig)
        plt.close(fig)

    elif optiune == "Admitere":
        st.subheader("🎓 Predicție Admitere Facultate")

        # Colectarea caracteristicilor (Features)
        valoare_medie = st.slider("Media finală", 5.0, 10.0, 8.0)
        activ_extrascolare = st.checkbox("Activități extrașcolare")
        scrisoare_recomandare = st.checkbox("Scrisoare de recomandare")

        # Conversia explicită din boolean în întreg (0 sau 1)
        int_activ = int(activ_extrascolare)
        int_recom = int(scrisoare_recomandare)

        # Formatarea structurată a datelor pentru clasificator
        input_clasificare = [[valoare_medie, int_activ, int_recom]]
        rezultat_admitere = model_clasificare.predict(input_clasificare)[0]

        if rezultat_admitere == 1:
            st.success("✅ Rezultat estimat: ADMIS!")
        else:
            st.error("❌ Rezultat estimat: RESPINS")


if __name__ == "__main__":
    ruleaza_aplicatia()
