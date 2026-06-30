#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 23: Crearea unui Dashboard Interactiv cu Streamlit.

Această aplicație implementează o platformă web de HR Analytics,
integrând metrici dinamice, filtrare multi-selecție și randare de grafice.
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st


def asigura_existenta_datelor():
    """Verifică existența fișierului CSV și îl generează automant dacă lipsește.

    Previne erorile runtime la prima pornire a serverului Streamlit.
    """
    nume_fisier = "angajati.csv"
    if not os.path.exists(nume_fisier):
        np.random.seed(42)
        departamente_valide = ["IT", "HR", "Marketing", "Sales"]
        sexe_valide = ["Male", "Female"]

        date_sintetice = {
            "department": np.random.choice(departamente_valide, size=100),
            "sex": np.random.choice(sexe_valide, size=100),
            "age": np.random.normal(35, 10, size=100).astype(int),
            "salary": np.random.normal(5000, 1500, size=100).astype(int),
            "experience": np.random.randint(1, 15, 100),
        }

        df_nou = pd.DataFrame(date_sintetice)
        df_nou.to_csv(nume_fisier, index=False)


def construieste_dashboard():
    """Randează interfața grafică și logica dashboard-ului Streamlit."""
    # Configurare opțională a stilului Seaborn pentru ploturile din dashboard
    sns.set_theme(style="whitegrid")

    # Titlul principal al aplicației web
    st.title("Dashboard Angajati - Salarii si Departamente")

    # Înlocuitor text în absența unui fișier logo fizic
    st.markdown("### 📊 Platforma HR Analytics")

    # 1. Citirea și afișarea setului de date
    df = pd.read_csv("angajati.csv")

    st.subheader("Datele brute")
    st.dataframe(df.head())

    # 2. Filtrare dinamică folosind widget-ul multiselect
    toate_departamentele = df["department"].unique().tolist()
    departamente_selectate = st.multiselect(
        "Selectează departamente:", toate_departamentele
    )

    # Aplicarea filtrului dacă utilizatorul a selectat cel puțin o opțiune
    if departamente_selectate:
        df = df[df["department"].isin(departamente_selectate)]

    # 3. Randare grafic boxplot prin Seaborn
    st.subheader("Distribuția salariilor")
    fig1, ax1 = plt.subplots()
    sns.boxplot(x="department", y="salary", data=df, ax=ax1, palette="Set2")
    st.pyplot(fig1)
    plt.close(fig1)

    # 4. Agregări și grafic nativ Streamlit (Bar chart)
    st.subheader("Salariu mediu pe departament")
    seria_medii = df.groupby("department")["salary"].mean().sort_values(ascending=False)
    st.bar_chart(seria_medii)

    # 5. Generare KPI-uri dinamice cu widget-ul metric
    st.subheader("KPI-uri")

    # Calculare valori agregate pe baza dataset-ului (filtrat sau general)
    total_angajati = len(df)
    medie_salariu = 0.0
    medie_experienta = 0.0

    if total_angajati > 0:
        medie_salariu = round(df["salary"].mean(), 2)
        medie_experienta = round(df["experience"].mean(), 1)

    # Randare componente vizuale KPI
    st.metric("Număr angajați", total_angajati)
    st.metric("Salariu mediu (RON)", medie_salariu)
    st.metric("Experiență medie (Ani)", medie_experienta)

    # 6. Grafic suplimentar: Histograma distribuției de vârstă
    st.subheader("Distribuție vârste")
    fig2, ax2 = plt.subplots()
    sns.histplot(df["age"], kde=True, bins=20, ax=ax2, color="skyblue")
    st.pyplot(fig2)
    plt.close(fig2)

    # 7. Note de subsol și metadate UI
    st.markdown(
        """
    ---
    *Acest dashboard a fost realizat pentru analiză internă,
    folosind modulele integrate Seaborn + Streamlit.*
    """
    )


if __name__ == "__main__":
    # Inițializare fișier date
    asigura_existenta_datelor()
    # Lansare UI
    construieste_dashboard()
