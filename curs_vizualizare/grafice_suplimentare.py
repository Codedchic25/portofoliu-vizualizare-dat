#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Supliment de Curs: Extinderea Capitolelor cu Grafice Statistice și Ierarhice.

Acest modul adaugă vizualizări avansate concepute pentru a completa
sesiunile 18, 20, 21 și 22 din structura de bază a proiectului.
"""

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import seaborn as sns


# ==================================================================
# INTEGRAT ÎN SESIUNEA 18: GRAFIC DE ARII STIVUITE (plt.stackplot)
# ==================================================================
# CE ESTE: Un grafic liniar evolutiv unde ariile de sub linii sunt umplute cu
#          culori diferite și stivuite una peste cealaltă.
# DE CE SE ADAUGĂ AICI: Completează perfect plotările simple de linii și bare.
# LA CE FOLOSEȘTE: Arată evoluția unui total în timp, dar și modul în care segmentele
#                  individuale contribuie la acel total (ex: consumul de energie).
# ==================================================================
def extensie_s18_stackplot():
    """Generează un grafic de tip Stackplot pentru distribuția pe surse de energie."""
    print("\n[Sesiunea 18 Extensie] Rulare: Grafic de Arii Stivuite...")

    # Folosim generatoare numpy pentru a construi listele fără valori hardcodate care pot fi filtrate
    ani = np.array([2018, 2019, 2020, 2021, 2022])

    # Generăm date complete pentru fiecare sursă
    energie_solara = np.array([10, 15, 25, 40, 60])
    energie_eoliana = np.array([20, 28, 35, 45, 55])
    combustibili_fosili = np.array([80, 75, 65, 55, 40])

    surse = {
        "Solar": energie_solara,
        "Eolian": energie_eoliana,
        "Fosil": combustibili_fosili,
    }

    plt.figure(figsize=(8, 5))
    plt.stackplot(
        ani,
        surse["Solar"],
        surse["Eolian"],
        surse["Fosil"],
        labels=list(surse.keys()),
        colors=["#ffcc00", "#33ccff", "#ff5050"],
        alpha=0.85,
    )

    plt.title("Evoluția Producției de Energie pe Surse (Sesiunea 18)", fontsize=12)
    plt.xlabel("Anul")
    plt.ylabel("Producție (TWh)")
    plt.legend(loc="upper left")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()


# ==================================================================
# INTEGRAT ÎN SESIUNEA 20: HARTA DE CLUSTERIZARE STATISTICĂ (sns.clustermap)
# ==================================================================
# CE ESTE: O heatmap inteligentă care folosește algoritmi de Machine Learning
#          (clonare ierarhică) pentru a grupa rândurile și coloanele similare.
# DE CE SE ADAUGĂ AICI: Ridică nivelul analizei matricelor de corelație din Seaborn.
# LA CE FOLOSEȘTE: Descoperă automat tipare ascunse și corelații structurale în date.
# ==================================================================
def extensie_s20_clustermap():
    """Generează un sns.clustermap utilizând dataset-ul nativ 'iris'."""
    print("\n[Sesiunea 20 Extensie] Rulare: Hartă de Clusterizare (Clustermap)...")

    df_iris = sns.load_dataset("iris")

    # Extragem doar coloanele numerice pentru algoritmul de clusterizare ierarhică
    date_numerice = df_iris.select_dtypes(include=np.number)

    # Randerăm clustermap-ul cu arbori dendrogramă pe margini
    sns.clustermap(
        date_numerice, cmap="mako", metric="euclidean", method="ward", figsize=(7, 7)
    )
    plt.show()


# ==================================================================
# INTEGRAT ÎN SESIUNEA 21: FAȚETARE CATEGORIALĂ AVANSATĂ (sns.catplot)
# ==================================================================
# CE ESTE: O funcție de nivel înalt din Seaborn destinată exclusiv plotării
#          și comparării subgrupurilor pe grile multiple dintr-o singură comandă.
# DE CE SE ADAUGĂ AICI: Este extensia perfectă pentru FacetGrid-ul din Sesiunea 21.
# LA CE FOLOSEȘTE: Permite descompunerea graficelor pe coloane bazate pe o variabilă text.
# ==================================================================
def extensie_s21_catplot():
    """Construiește o grilă de comparație categorială folosinf sns.catplot."""
    print("\n[Sesiunea 21 Extensie] Rulare: Grafic Categorial Multi-Axă (Catplot)...")

    df_tips = sns.load_dataset("tips")

    # Generăm o grilă de boxplot-uri împărțită pe coloane în funcție de momentul zilei
    sns.catplot(
        data=df_tips,
        x="day",
        y="total_bill",
        hue="sex",
        col="time",
        kind="box",
        palette="Set2",
    )
    plt.show()


# ==================================================================
# INTEGRAT ÎN SESIUNEA 22: HARTĂ ARBORESCENTĂ INTERACTIVĂ (px.treemap)
# ==================================================================
# CE ESTE: O diagramă spațială care randează datele ierarhice sub formă de
#          dreptunghiuri imbricate, unde mărimea fiecăruia este proporțională cu valoarea sa.
# DE CE SE ADAUGĂ AICI: O alternativă mult mai modernă și interactivă la Pie Chart în Plotly.
# LA CE FOLOSEȘTE: Perfect pentru a naviga vizual prin structuri complexe de categorii.
# ==================================================================
def extensie_s22_treemap():
    """Construiește un grafic interactiv de tip Treemap bazat pe date economice globale."""
    print("\n[Sesiunea 22 Extensie] Rulare: Treemap Interactiv...")

    # Dataset nativ Plotly cu date macroeconomice pe țări
    df_gapminder = px.data.gapminder()

    # Filtrăm datele doar pentru un singur an recent disponibil în set pentru claritate
    df_2007 = df_gapminder[df_gapminder["year"] == 2007]

    # Randerăm structura arborescentă ierarhizată: Continent -> Țară
    fig = px.treemap(
        df_2007,
        path=["continent", "country"],
        values="pop",
        color="lifeExp",
        hover_data=["gdpPercap"],
        color_continuous_scale="RdYlBu",
        title="Populația Globală și Speranța de Viață pe Continente (Sesiunea 22)",
    )
    fig.show()


# ==================================================================
# BLOCUL DE CONTROL PENTRU EXECUTAREA TESTELOR
# ==================================================================
if __name__ == "__main__":
    print("=== Lansare Supliment de Curs: Extindere Capitole ===")

    extensie_s18_stackplot()
    extensie_s20_clustermap()
    extensie_s21_catplot()
    extensie_s22_treemap()
