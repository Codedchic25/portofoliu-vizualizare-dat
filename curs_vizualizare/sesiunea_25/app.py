#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 25: Dashboard-uri Profesionale cu Streamlit și Profilare Automatizată.

Aplicație avansată capabilă să încarce fișiere CSV externe, să aplice filtre
multi-axă dinamice și să exporte seturile de date modificate.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# Verificare defensivă prin import dinamic pentru a fenta verificarea statică Pylance
PROFILING_DISPONIBIL = True
try:
    # type: ignore îi spune explicit analizatorului Pylance să ignore această linie
    import streamlit_pandas_profiling as st_profile  # type: ignore
    import ydata_profiling as yd_profile  # type: ignore
except ImportError:
    PROFILING_DISPONIBIL = False


def porneste_dashboard():
    """Configurează structura, layout-ul și logica reactivă a dashboard-ului."""
    st.set_page_config(layout="wide")
    st.title("📈 Dashboard Interactiv: Date Reale")

    # Componenta de încărcare fișiere din UI
    tipuri_acceptate = ["csv"]
    uploaded_file = st.file_uploader("Încarcă un fișier CSV", type=tipuri_acceptate)

    if not uploaded_file:
        st.info("Vă rugăm să încărcați un fișier CSV pentru a inițializa dashboard-ul.")
        return

    # Citirea setului de date inițial
    df_raw = pd.read_csv(uploaded_file)
    st.success("Fișier încărcat cu succes!")

    st.subheader("📋 Previzualizare date brute (Primele 5 rânduri)")
    st.dataframe(df_raw.head())

    # Generarea automată a raportului de profilare (dacă bibliotecile sunt suportate/instalate)
    st.subheader("🔍 Profilare Automată a Dataset-ului")
    with st.expander("Afișează Raportul Complet de Analiză Exploratorie"):
        if PROFILING_DISPONIBIL:
            raport_profilare = yd_profile.ProfileReport(
                df_raw, title="Raport complet de analiză", explorative=True
            )
            st_profile.st_profile_report(raport_profilare)
        else:
            st.warning(
                "Raportul de profilare automată (ydata-profiling) nu este disponibil pe această versiune de Python (necesită Python <= 3.11/3.13). Restul funcțiilor de filtrare și grafice de mai jos sunt complet operaționale!"
            )

    # ------------------------------------------------------------------
    # SISTEM DINAMIC DE FILTRARE (SIDEBAR)
    # ------------------------------------------------------------------
    st.sidebar.header("🔍 Filtre Globale")
    df_filtrat = df_raw.copy()

    # Identificarea tipurilor de coloane din DataFrame
    coloane_numerice = df_filtrat.select_dtypes(include=np.number).columns.tolist()
    coloane_categorice = df_filtrat.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # 1. Filtre pentru coloanele categorice (Multi-select)
    for col in coloane_categorice:
        toate_optiunile = df_filtrat[col].unique().tolist()
        selectie_categorica = st.sidebar.multiselect(
            f"Filtru {col}", toate_optiunile, default=toate_optiunile
        )
        df_filtrat = df_filtrat[df_filtrat[col].isin(selectie_categorica)]

    # 2. Filtre pentru coloanele numerice (Sliders de interval)
    for col in coloane_numerice:
        val_minima = float(df_filtrat[col].min())
        val_maxima = float(df_filtrat[col].max())

        # Control de siguranță în cazul în care coloana are o singură valoare unică
        if val_minima == val_maxima:
            continue

        interval_selectat = st.sidebar.slider(
            f"Interval {col}",
            val_minima,
            val_maxima,
            (val_minima, val_maxima),
        )
        limita_inf = interval_selectat
        limita_sup = interval_selectat

        df_filtrat = df_filtrat[
            (df_filtrat[col] >= limita_inf) & (df_filtrat[col] <= limita_sup)
        ]

    # Afișarea datelor după aplicarea filtrelor din Sidebar
    st.subheader("📊 Date Filtrate Rezultate")
    st.dataframe(df_filtrat)

    # ------------------------------------------------------------------
    # MODUL DE VIZUALIZARE MULTI-AXĂ ȘI TIPURI DE GRAFICE
    # ------------------------------------------------------------------
    st.subheader("🌐 Configurator de Vizualizări Avansate")

    toate_coloanele = df_filtrat.columns.tolist()
    tipuri_grafic_valide = [
        "barplot",
        "boxplot",
        "heatmap",
        "hist",
        "scatter",
    ]

    col_st_1, col_st_2, col_st_3 = st.columns(3)

    with col_st_1:
        x_col = st.selectbox("Axa X (Independentă)", toate_coloanele)
    with col_st_2:
        y_col = st.selectbox("Axa Y (Dependentă)", toate_coloanele)
    with col_st_3:
        chart_type = st.selectbox("Selectează tipul de grafic", tipuri_grafic_valide)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Control logic pentru maparea graficului selectat
    if chart_type == "barplot":
        sns.barplot(x=x_col, y=y_col, data=df_filtrat, ax=ax, palette="Blues")
    elif chart_type == "boxplot":
        sns.boxplot(x=x_col, y=y_col, data=df_filtrat, ax=ax, palette="Set3")
    elif chart_type == "heatmap":
        matrice_corr = df_filtrat.corr(numeric_only=True)
        sns.heatmap(matrice_corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
        ax.set_title("Matrice de Corelație (Doar Variabile Numerice)")
    elif chart_type == "hist":
        sns.histplot(df_filtrat[x_col], bins=30, kde=True, ax=ax, color="purple")
    elif chart_type == "scatter":
        sns.scatterplot(x=x_col, y=y_col, data=df_filtrat, ax=ax, color="red")

    st.pyplot(fig)
    plt.close(fig)

    # ------------------------------------------------------------------
    # MODUL EXPORT ȘI DESCĂRCARE DATE FILTRATE
    # ------------------------------------------------------------------
    st.write("---")
    st.subheader("💾 Exportă Rezultatele")

    csv_data = df_filtrat.to_csv(index=False)

    st.download_button(
        label="🔍 Descarcă fișierul filtrat (CSV)",
        data=csv_data,
        file_name="date_filtrate.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    porneste_dashboard()
