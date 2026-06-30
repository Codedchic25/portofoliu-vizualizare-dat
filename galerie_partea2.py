#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Panoul Absolut - Partea 2 (Graficele 13 - 24).

Include restul colecției din Seaborn, modulele web interactive Plotly și suitele speciale.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(42)


def g13_s20_kde():
    """13. S20: Kdeplot de densitate pură umplută."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.kdeplot(data=df_tips, x="tip", fill=True, color="red")
    plt.title("13. S20: Densitatea bacșișului")
    plt.show()


def g14_s20_scatter_hue():
    """14. S20: Scatter plot cu segmentare cromatică pe sexe."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.scatterplot(x="total_bill", y="tip", data=df_tips, hue="sex")
    plt.title("14. S20: Corelație nota totală vs bacșiș")
    plt.show()


def g15_s20_boxplot():
    """15. S20: Boxplot statistic repartizat pe zile."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.boxplot(x="day", y="total_bill", data=df_tips)
    plt.title("15. S20: Boxplot pe zile")
    plt.show()


def g16_s21_violin_split():
    """16. S21: Violin plot cu formă divizată (split=True)."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.violinplot(
        x="day", y="tip", data=df_tips, hue="sex", split=True, palette="muted"
    )
    plt.title("16. S21: Distribuția bacșișului")
    plt.show()


def g17_s21_swarm():
    """17. S21: Swarmplot suprapus peste Stripplot."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.stripplot(x="day", y="total_bill", data=df_tips, color="gray", alpha=0.5)
    sns.swarmplot(x="day", y="total_bill", data=df_tips, hue="sex", palette="Set1")
    plt.title("17. S21: Distribuție granulară a punctelor")
    plt.show()


def g18_s21_barplot_sd():
    """18. S21: Barplot corporativ cu deviație standard."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.barplot(x="day", y="total_bill", data=df_tips, errorbar="sd", palette="Blues")
    plt.title("18. S21: Total bill mediu pe zile")
    plt.show()


def g19_s22_plotly_line():
    """19. S22: Grafic liniar interactiv în browser."""
    luni = ["Ian", "Feb", "Mar", "Apr"]
    valori_vanzari = np.array()

    structura = {"Luna": luni, "Vanzari": valori_vanzari}
    df = pd.DataFrame(structura)
    fig = px.line(
        df,
        x="Luna",
        y="Vanzari",
        title="19. S22: Evoluția Vânzărilor (Interactiv)",
    )
    fig.show()


def g20_s22_plotly_heatmap():
    """20. S22: Heatmap interactivă prin Graph Objects."""
    z = np.random.rand(5, 5)
    fig = go.Figure(data=go.Heatmap(z=z, colorscale="Viridis"))
    fig.update_layout(title="20. S22: Heatmap Random (Interactive)")
    fig.show()


def g21_spec_donut():
    """21. Spectacular: Diagramă Gogoașă dublă stratificată."""
    fig, ax = plt.subplots(figsize=(5, 5))

    valori_ext = np.array()
    valori_int = np.array()

    ax.pie(
        valori_ext,
        radius=1.3,
        colors=["#ff9999", "#66b3ff"],
        wedgeprops=dict(width=0.3, edgecolor="white"),
    )
    ax.pie(
        valori_int,
        radius=1.0,
        colors=["#ffcccc", "#ffb3b3", "#99ccff", "#80bfff"],
        wedgeprops=dict(width=0.3, edgecolor="white"),
    )
    ax.add_artist(plt.Circle((0, 0), 0.7, color="white"))
    plt.title("21. Spectacular: Donut Chart Ierarhic", y=1.1)
    plt.show()


def g22_spec_radar():
    """22. Spectacular: Grafic Păianjen pe axe polare cercuri."""
    atribute = ["Viteză", "Fiabilitate", "Design", "Preț", "Baterie"]
    unghiuri = np.linspace(0, 2 * np.pi, len(atribute), endpoint=False).tolist()
    unghiuri += unghiuri[:1]

    val_a = np.array().tolist()
    val_a += val_a[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    plt.xticks(unghiuri[:-1], atribute)
    ax.plot(unghiuri, val_a, color="red", linewidth=2)
    ax.fill(unghiuri, val_a, color="red", alpha=0.25)
    plt.title("22. Spectacular: Radar Spider Chart", y=1.1)
    plt.show()


def g23_spec_3d():
    """23. Spectacular: Suprafață continuă 3D Wave."""
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    x = y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    ax.plot_surface(x, y, z, cmap="coolwarm", antialiased=True)
    plt.title("23. Spectacular: Relief Topografic 3D")
    plt.show()


def g24_extra_hexbin():
    """24. Extra: Fagure hexagonal de densitate masivă Big Data."""
    x, y = np.random.standard_normal(4000), np.random.standard_normal(4000)
    plt.figure()
    plt.hexbin(x, y, gridsize=25, cmap="YlGnBu")
    plt.colorbar(label="Concentrație")
    plt.title("24. Extra: Fagure Hexagonal de Densitate")
    plt.show()


def afiseaza_meniu_p2():
    """Afișează meniul interactiv pentru Partea 2."""
    toate_graficele = {
        "13": ("S20: Densitate KDE", g13_s20_kde),
        "14": ("S20: Scatter cu Hue", g14_s20_scatter_hue),
        "15": ("S20: Boxplot pe Zile", g15_s20_boxplot),
        "16": ("S21: Violin Plot Split", g16_s21_violin_split),
        "17": ("S21: Swarmplot Granular", g17_s21_swarm),
        "18": ("S21: Barplot cu Deviație SD", g18_s21_barplot_sd),
        "19": ("S22: Plotly Linie", g19_s22_plotly_line),
        "20": ("S22: Plotly Heatmap", g20_s22_plotly_heatmap),
        "21": ("Spec: Gogoașă Stratificată", g21_spec_donut),
        "22": ("Spec: Radar Spider Chart", g22_spec_radar),
        "23": ("Spec: Suprafață 3D Wave", g23_spec_3d),
        "24": ("Extra: Fagure Hexbin BigData", g24_extra_hexbin),
    }

    while True:
        print("\n" + "=" * 60)
        print("🖥️  PANOUL DE CONTROL ABSOLUT: PARTEA 2 (GRAFICELE 13 - 24)")
        print("=" * 60)
        for numar, date_grafic in toate_graficele.items():
            print(f"{numar.ljust(3)} -> {date_grafic}")
        print("all -> EXECUTĂ TOATE GRAFICELE DIN ACEASTĂ COLECȚIE")
        print("0   -> Închide Panoul")
        print("=" * 60)

        selectie = input("Introdu numărul vizualizării dorite: ").strip()

        if selectie in toate_graficele:
            toate_graficele[selectie]()
        elif selectie.lower() == "all":
            for cheie in sorted(toate_graficele.keys(), key=int):
                toate_graficele[cheie]()
        elif selectie == "0":
            break


if __name__ == "__main__":
    afiseaza_meniu_p2()
