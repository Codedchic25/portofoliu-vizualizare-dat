#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rezolvarea Temelor de Curs - Partea 3 (Sesiunile 23-26).

Acest script extinde funcționalitățile dashboard-urilor anterioare în Streamlit
prin implementarea arhitecturii pe Tab-uri, selecții de intervale prin Slider,
predicții avansate și export securizat de date.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st


def genereaza_dataset_teme():
    """Generează un set stabil de date pentru testarea aplicației."""
    np.random.seed(42)
    departamente = ["IT", "HR", "Marketing", "Sales"]

    date_sintetice = {
        "nume": [f"Angajat_{i}" for i in range(1, 101)],
        "department": np.random.choice(departamente, size=100),
        "sex": np.random.choice(["Male", "Female"], size=100),
        "age": np.random.randint(22, 60, 100),
        "salary": np.random.randint(3000, 12000, 100),
        "experience": np.random.randint(1, 15, 100),
        "performance": np.random.uniform(1.0, 10.0, 100),
    }
    return pd.DataFrame(date_sintetice)


def ruleaza_dashboard_teme():
    """Construiește aplicația web centralizată pentru rezolvarea temelor."""
    st.set_page_config(layout="wide")
    st.title("🧰 Rezolvare Teme Avansate (Sesiunile 23-26)")

    # Încărcarea setului de date bază
    df_baza = genereaza_dataset_teme()

    # Crearea unei structuri curate pe file (Tabs) conform cerințelor din teme
    tab1, tab2, tab3 = st.tabs(
        [
            "📊 Segmentare & Filtre Dinamice",
            "📈 Analiză Statistică",
            "🔮 Modul Predicție Scor",
        ]
    )

    # ------------------------------------------------------------------
    # TAB 1: FILTRARE AVANSATĂ, SLIDER INTERVAL ȘI EXPORT CSV
    # ------------------------------------------------------------------
    with tab1:
        st.subheader("🔍 Configurator Filtre și Descărcare Date")

        col_st, col_dr = st.columns(2)

        with col_st:
            # Multi-selecție pentru departamente
            dep_unice = df_baza["department"].unique().tolist()
            dep_alese = st.multiselect(
                "Filtrează după Departament:", dep_unice, default=dep_unice
            )

        with col_dr:
            # Tema S23: Adaugă o selecție de interval de salariu cu slider (Double-ended Slider)
            sal_min = float(df_baza["salary"].min())
            sal_max = float(df_baza["salary"].max())
            interval_salariu = st.slider(
                "Selectează Interval Salariu (RON):",
                sal_min,
                sal_max,
                (sal_min, sal_max),
            )

        # Aplicarea filtrelor pe DataFrame
        df_filtrat = df_baza[
            (df_baza["department"].isin(dep_alese))
            & (df_baza["salary"] >= interval_salariu[0])
            & (df_baza["salary"] <= interval_salariu[1])
        ]

        # Tema S23: Afișează doar angajații cu salariul > media totală (Opțiune de filtrare rapidă)
        filtreaza_peste_medie = st.checkbox(
            "Afișează doar angajații cu salariul mai mare decât media globală"
        )
        if filtreaza_peste_medie:
            media_globala = df_baza["salary"].mean()
            df_filtrat = df_filtrat[df_filtrat["salary"] > media_globala]
            st.info(
                f"Se afișează exclusiv salariile mai mari de {round(media_globala, 2)} RON"
            )

        st.write("### Rezultate Căutare:")
        st.dataframe(df_filtrat)

        # Tema S23: Permite salvarea datelor filtrate în CSV
        st.write("---")
        text_csv = df_filtrat.to_csv(index=False)
        st.download_button(
            label="💾 Descarcă datele filtrate în format CSV",
            data=text_csv,
            file_name="teme_date_filtrate.csv",
            mime="text/csv",
        )

    # ------------------------------------------------------------------
    # TAB 2: VIZUALIZĂRI ȘI CORELAȚIE VÂRSTĂ VS PERFORMANȚĂ
    # ------------------------------------------------------------------
    with tab2:
        st.subheader("📈 Analiză Grafică și Corelații")

        # Tema S25: Fă un grafic care arată corelația dintre vârstă și performanță
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.scatterplot(
            data=df_filtrat, x="age", y="performance", hue="department", s=100, ax=ax
        )
        sns.regplot(
            data=df_filtrat,
            x="age",
            y="performance",
            scatter=False,
            color="gray",
            ax=ax,
        )

        ax.set_title("Corelația dintre Vârstă și Performanța Angajatului")
        ax.set_xlabel("Vârstă (Ani)")
        ax.set_ylabel("Scor Performanță (1-10)")
        st.pyplot(fig)
        plt.close(fig)

    # ------------------------------------------------------------------
    # TAB 3: EXTINDERE ADMITERE / SCOR PREDICȚIE
    # ------------------------------------------------------------------
    with tab3:
        st.subheader("🔮 Modul Extins de Machine Learning")
        st.write("Predicția scorului de performanță bazat pe biometrie și experiență.")

        varsta_input = st.number_input(
            "Introdu Vârsta:", min_value=18, max_value=65, value=30
        )
        exp_input = st.slider("Introdu Anii de Experiență:", 1, 15, 5)

        # Simulare model matematic stabil de predicție bazat pe coeficienți liniari fixi
        # Evită re-antrenarea și erorile de instabilitate la re-randare
        scor_estimat = 3.0 + (varsta_input * 0.05) + (exp_input * 0.25)
        scor_final = min(10.0, max(1.0, scor_estimat))

        st.success(
            f"Scorul de performanță estimat pentru angajat: **{round(scor_final, 2)} / 10.0**"
        )


if __name__ == "__main__":
    ruleaza_dashboard_teme()
