#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rezolvarea Temelor de Curs - Partea 2 (Sesiunile 21, 22, 24, 25).

Contine rezolvările algoritmice și logice pentru cerințele
avansate, interfețele predictive și configurările dinamice.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns


# ==================================================================
# TEME SESIUNEA 21: SEABORN AVANSAT
# ==================================================================
def tema_21_1_barplot_varsta():
    """Cerintă: Barplot care compară salariul mediu sub 30 și peste 30 de ani."""
    np.random.seed(42)
    df_angajati = pd.DataFrame(
        {
            "age": np.random.randint(22, 60, 50),
            "salary": np.random.randint(3000, 12000, 50),
        }
    )

    # Adăugăm o coloană de segmentare logică pe baza vârstei de 30 de ani
    df_angajati["Grup Vârstă"] = np.where(
        df_angajati["age"] < 30, "Sub 30 ani", "Peste 30 ani"
    )

    plt.figure()
    sns.barplot(
        x="Grup Vârstă", y="salary", data=df_angajati, errorbar="sd", palette="muted"
    )
    plt.title("Tema 21.1: Salariul mediu în funcție de pragul de vârstă")
    plt.ylabel("Salariu Mediu (RON)")
    plt.show()


# ==================================================================
# TEME SESIUNEA 22: PLOTLY INTERACTIV
# ==================================================================
def tema_22_1_heatmap_zece():
    """Cerintă: Creează o heatmap interactivă cu date generate random (10x10)."""
    matrice_date = np.random.rand(10, 10)

    # Crearea graficului de densitate interactiv
    fig = px.imshow(
        matrice_date,
        color_continuous_scale="Viridis",
        title="Tema 22.1: Heatmap Interactivă 10x10",
    )
    fig.show()


# ==================================================================
# TEME SESIUNEA 24 & 25: PROIECTE COMBINATE / TEME STRUCUTURATE
# ==================================================================
def tema_25_1_corelatie_performanta():
    """Cerintă: Fă un grafic care arată corelația dintre vârstă și performanță."""
    np.random.seed(42)
    df_hr = pd.DataFrame(
        {
            "varsta": np.random.randint(20, 65, 100),
            "performanta": np.random.uniform(1.0, 10.0, 100),
        }
    )

    plt.figure()
    sns.scatterplot(x="varsta", y="performanta", data=df_hr, color="darkred")
    # Adăugarea unei linii de trend statistic pentru o mai bună interpretare
    sns.regplot(x="varsta", y="performanta", data=df_hr, scatter=False, color="blue")
    plt.title("Tema 25.1: Corelația dintre Vârsta Angajaților și Performanță")
    plt.xlabel("Vârstă (Ani)")
    plt.ylabel("Scor Performanță (1-10)")
    plt.show()


if __name__ == "__main__":
    print("=== Execuție Teme Partea 2 ===")
    tema_21_1_barplot_varsta()
    # Poti decomenta restul funcțiilor pentru a le testa pe rând
