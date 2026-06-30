#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Panoul de Control Global - Toate Graficele din Sesiunile 18-27.

Un modul centralizat care permite rularea interactivă a fiecărui grafic
studiat în cadrul cursului dintr-un singur meniu de terminal.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Setări generale de estetică
sns.set_theme(style="whitegrid")
np.random.seed(42)


# ==================================================================
# GRUPUL 1: MATPLOTLIB DE BAZĂ ȘI AVANSAT (SESIUNILE 18 - 19)
# ==================================================================
def s18_grafic_linie():
    """Sesiunea 18: Plotare liniară simplă."""
    x = np.arange(1, 6)
    y = x * 2
    plt.figure()
    plt.plot(x, y, marker="o", color="blue")
    plt.title("S18: Grafic liniar simplu")
    plt.show()


def s18_grafic_bare():
    """Sesiunea 18: Diagramă cu bare verticale pentru produse."""
    produse = ["Laptop", "Telefon", "Tabletă"]
    vanzari = np.array()
    plt.figure()
    plt.bar(produse, vanzari, color="green")
    plt.title("S18: Vânzări pe produs")
    plt.show()


def s18_histograma():
    """Sesiunea 18: Distribuția statistică a notelor."""
    note = np.random.normal(7, 1.5, 1000)
    plt.figure()
    plt.hist(note, bins=20, color="skyblue", edgecolor="black")
    plt.title("S18: Distribuția notelor (Histogramă)")
    plt.show()


def s18_scatter():
    """Sesiunea 18: Scatter plot cu puncte aleatoare."""
    x, y = np.random.rand(50), np.random.rand(50)
    plt.figure()
    plt.scatter(x, y, color="purple")
    plt.title("S18: Puncte aleatoare")
    plt.show()


def s19_axe_custom():
    """Sesiunea 19: Controlul avansat al limitelor și etichetelor axelor."""
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.plot(x, np.sin(x))
    plt.xlim(0, 12)
    plt.ylim(-2, 2)
    plt.xticks(np.arange(0, 11, 2))
    plt.title("S19: Customizare completă axe")
    plt.show()


def s19_adnotari():
    """Sesiunea 19: Adăugare linii de referință și adnotări text."""
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.plot(x, np.sin(x))
    plt.axhline(0, color="gray", linestyle="--")
    plt.annotate(
        "Maxim",
        xy=(np.pi / 2, 1),
        xytext=(3, 1.5),
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )
    plt.title("S19: Linii de referință și adnotări")
    plt.show()


# ==================================================================
# GRUPUL 2: SEABORN STATISTIC ȘI AVANSAT (SESIUNILE 20 - 21)
# ==================================================================
def s20_kde_densitate():
    """Sesiunea 20: Grafic de densitate estimată (KDE) în Seaborn."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.kdeplot(data=df_tips, x="tip", fill=True, color="red")
    plt.title("S20: Densitatea bacșișului (KDE)")
    plt.show()


def s20_boxplot_zile():
    """Sesiunea 20: Boxplot categorial distribuit pe zile."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.boxplot(data=df_tips, x="day", y="total_bill", palette="Set3")
    plt.title("S20: Boxplot total bill pe zile")
    plt.show()


def s21_violin_split():
    """Sesiunea 21: Violin plot cu distribuție divizată pe sexe."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.violinplot(
        data=df_tips, x="day", y="tip", hue="sex", split=True, palette="muted"
    )
    plt.title("S21: Violin Plot divizat pe sexe")
    plt.show()


def s21_swarm_granular():
    """Sesiunea 21: Swarmplot suprapus pentru distribuție granulară."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.stripplot(data=df_tips, x="day", y="total_bill", color="gray", alpha=0.5)
    sns.swarmplot(data=df_tips, x="day", y="total_bill", hue="sex", palette="Set1")
    plt.title("S21: Distribuție granulară cu Swarmplot")
    plt.show()


# ==================================================================
# GRUPUL 3: GRAFICE SPECTACULOASE ȘI EXTENSII AVANSATE
# ==================================================================
def extra_donut_ierarhic():
    """Gogoașă dublă stratificată ierarhic."""
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(
        np.array(),
        radius=1.3,
        colors=["#ff9999", "#66b3ff"],
        wedgeprops=dict(width=0.3, edgecolor="white"),
    )
    ax.pie(
        np.array(),
        radius=1.0,
        colors=["#ffcccc", "#ffb3b3", "#99ccff", "#80bfff"],
        wedgeprops=dict(width=0.3, edgecolor="white"),
    )
    ax.add_artist(plt.Circle((0, 0), 0.7, color="white"))
    plt.title("Spectacular: Donut Chart Dublu", y=1.1)
    plt.show()


def extra_radar_spider():
    """Grafic radar (Spider) pe coordonate polare."""
    atribute = ["Viteză", "Fiabilitate", "Design", "Preț", "Baterie"]
    unghiuri = np.linspace(0, 2 * np.pi, len(atribute), endpoint=False).tolist()
    unghiuri += unghiuri[:1]

    val_a = np.array().tolist()
    val_a += val_a[:1]
    val_b = np.array().tolist()
    val_b += val_b[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    plt.xticks(unghiuri[:-1], atribute)
    ax.plot(unghiuri, val_a, color="red", label="Premium")
    ax.fill(unghiuri, val_a, color="red", alpha=0.2)
    ax.plot(unghiuri, val_b, color="green", label="Eco")
    ax.fill(unghiuri, val_b, color="green", alpha=0.2)
    plt.title("Spectacular: Radar Spider Chart", y=1.1)
    plt.show()


def extra_relief_3d():
    """Suprafață matematică continuă 3D."""
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    x = y = np.arange(-5, 5, 0.25)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))
    ax.plot_surface(x, y, z, cmap="coolwarm", antialiased=True)
    plt.title("Spectacular: Suprafață Continuă 3D")
    plt.show()


def extra_hexbin_fagure():
    """Fagure de densitate hexagonală (Big Data)."""
    x, y = np.random.standard_normal(3000), np.random.standard_normal(3000)
    plt.figure()
    plt.hexbin(x, y, gridsize=25, cmap="YlGnBu")
    plt.colorbar(label="Concentrație")
    plt.title("Extra: Fagure Hexagonal de Densitate")
    plt.show()


# ==================================================================
# PANOU INTERACTIV DE CONTROL ȘI MENIU INTERN
# ==================================================================
def rulare_meniu():
    """Randează interfața interactivă de selecție din consolă."""
    categorii = {
        "1": ("S18: Grafic Linie", s18_grafic_linie),
        "2": ("S18: Grafic Bare", s18_grafic_bare),
        "3": ("S18: Histogramă Note", s18_histograma),
        "4": ("S18: Scatter Plot", s18_scatter),
        "5": ("S19: Customizare Axe", s19_axe_custom),
        "6": ("S19: Linii & Adnotări", s19_adnotari),
        "7": ("S20: Densitate KDE", s20_kde_densitate),
        "8": ("S20: Boxplot pe Zile", s20_boxplot_zile),
        "9": ("S21: Violin Plot Split", s21_violin_split),
        "10": ("S21: Swarmplot Detaliat", s21_swarm_granular),
        "11": ("Spec: Gogoașă Stratificată", extra_donut_ierarhic),
        "12": ("Spec: Radar Spider Chart", extra_radar_spider),
        "13": ("Spec: Suprafață 3D Wave", extra_relief_3d),
        "14": ("Spec: Fagure Hexbin BigData", extra_hexbin_fagure),
    }

    while True:
        print("\n" + "=" * 50)
        print("📊 PANOUL GLOBAL DE VIZUALIZARE (SESIUNILE 18-27)")
        print("=" * 50)
        for cheie, val in categorii.items():
            print(f"{cheie.ljust(3)} -> {val[0]}")
        print("all -> RULARE TOATĂ COLECȚIA DE GRAFICE")
        print("0   -> Ieșire din aplicație")
        print("=" * 50)

        optiune = input("Introdu numărul graficului dorit: ").strip()

        if optiune in categorii:
            categorii[optiune][1]()
        elif optiune.lower() == "all":
            print(
                "\n[INFO] Se lansează întreaga colecție. Închide fereastra curentă pentru a trece la următoarea!"
            )
            for cheie in sorted(categorii.keys(), key=int):
                categorii[cheie][1]()
        elif optiune == "0":
            print("\n🎨 Panou închis cu succes! Cod curat, 0 Problems!")
            break
        else:
            print("\n❌ Opțiune invalidă! Încearcă din nou.")


if __name__ == "__main__":
    rulare_meniu()
