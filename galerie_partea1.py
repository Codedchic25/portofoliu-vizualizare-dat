#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Panoul Absolut - Partea 1 (Graficele 1 - 12).

Include vizualizările fundamentale și avansate din Matplotlib și Seaborn.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.set_theme(style="whitegrid")
np.random.seed(42)


def g1_s18_linie():
    """1. S18: Grafic liniar simplu."""
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    plt.figure()
    plt.plot(x, y, marker="o", color="blue")
    plt.title("1. S18: Grafic liniar simplu")
    plt.show()


def g2_s18_bare():
    """2. S18: Bare verticale pentru vânzări produse."""
    produse = ["Laptop", "Telefon", "Tabletă"]
    vanzari = np.array([100, 250, 90])
    plt.figure()
    plt.bar(produse, vanzari, color="green")
    plt.title("2. S18: Vânzări pe produs")
    plt.show()


def g3_s18_histograma():
    """3. S18: Distribuția normală a notelor."""
    note = np.random.normal(7, 1.5, 1000)
    plt.figure()
    plt.hist(note, bins=20, color="skyblue", edgecolor="black")
    plt.title("3. S18: Distribuția notelor (Histogramă)")
    plt.show()


def g4_s18_scatter():
    """4. S18: Scatter plot cu puncte aleatoare."""
    x, y = np.random.rand(50), np.random.rand(50)
    plt.figure()
    plt.scatter(x, y, color="purple")
    plt.title("4. S18: Puncte aleatoare")
    plt.show()


def g5_s18_subplots():
    """5. S18: Subploturi în aceeași figură (Pătrat vs Liniar)."""
    x = np.array([1, 2, 3, 4])
    plt.figure(figsize=(9, 4))
    plt.subplot(1, 2, 1)
    plt.plot(x, x**2, color="red")
    plt.title("Pătrat")
    plt.subplot(1, 2, 2)
    plt.plot(x, x, color="blue")
    plt.title("Liniar")
    plt.suptitle("5. S18: Comparare funcții")
    plt.tight_layout()
    plt.show()


def g6_s19_axe():
    """6. S19: Customizare avansată a axelor (Limite și Ticks)."""
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.plot(x, np.sin(x))
    plt.xlim(0, 12)
    plt.ylim(-2, 2)
    plt.xticks(np.arange(0, 11, 2))
    plt.title("6. S19: Controlul complet al axelor")
    plt.show()


def g7_s19_adnotari():
    """7. S19: Linii de referință și adnotare cu săgeată."""
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.plot(x, np.sin(x))
    plt.axhline(0, color="gray", linestyle="--")
    plt.axvline(5, color="red", linestyle=":")
    plt.annotate(
        "Maxim",
        xy=(np.pi / 2, 1),
        xytext=(3, 1.5),
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )
    plt.title("7. S19: Adnotări pe grafic")
    plt.show()


def g8_s19_pandas():
    """8. S19: Plotare directă dintr-un DataFrame Pandas."""
    luni = ["Ian", "Feb", "Mar", "Apr"]
    date_2023 = np.array([1000, 1200, 900, 1500])
    date_2024 = np.array([1100, 1250, 1000, 1700])

    structura = {"2023": date_2023, "2024": date_2024}
    df = pd.DataFrame(structura, index=luni)
    df.plot(kind="bar")
    plt.title("8. S19: Comparație Vânzări din Pandas")
    plt.ylabel("Valoare RON")
    plt.show()


def g9_s19_heatmap_imshow():
    """9. S19: Heatmap matriceală folosinf imshow."""
    data = np.random.rand(5, 5)
    plt.figure()
    plt.imshow(data, cmap="viridis", interpolation="nearest")
    plt.colorbar()
    plt.title("9. S19: Heatmap aleatoare")
    plt.show()


def g10_s19_pie():
    """10. S19: Pie chart clasic pentru distribuție fructe."""
    valori_fructe = np.array([40, 30, 30])
    etichete_fructe = ["Mere", "Pere", "Banane"]
    plt.figure()
    plt.pie(valori_fructe, labels=etichete_fructe, autopct="%1.1f%%")
    plt.title("10. S19: Distribuție fructe")
    plt.show()


def g11_s19_fill_between():
    """11. S19: Fill Between pentru evidențierea ariei dintre curbe."""
    x = np.linspace(0, 10, 100)
    plt.figure()
    plt.fill_between(x, np.sin(x), np.sin(x) + 0.5, color="orange", alpha=0.5)
    plt.title("11. S19: Zona dintre sin(x) și sin(x)+0.5")
    plt.show()


def g12_s20_histplot():
    """12. S20: Histplot cu curbă KDE suprapusă."""
    df_tips = sns.load_dataset("tips")
    plt.figure()
    sns.histplot(df_tips["total_bill"], kde=True, bins=20, color="skyblue")
    plt.title("12. S20: Distribuția notelor totale")
    plt.show()


def afiseaza_meniu_p1():
    """Afișează meniul interactiv pentru Partea 1."""
    toate_graficele = {
        "1": ("S18: Grafic Linie", g1_s18_linie),
        "2": ("S18: Grafic Bare", g2_s18_bare),
        "3": ("S18: Histogramă Note", g3_s18_histograma),
        "4": ("S18: Scatter Plot", g4_s18_scatter),
        "5": ("S18: Subplot Combinat", g5_s18_subplots),
        "6": ("S19: Control complet Axe", g6_s19_axe),
        "7": ("S19: Adnotări & Săgeți", g7_s19_adnotari),
        "8": ("S19: Bar Chart din Pandas", g8_s19_pandas),
        "9": ("S19: Heatmap pur Imshow", g9_s19_heatmap_imshow),
        "10": ("S19: Pie Chart Fructe", g10_s19_pie),
        "11": ("S19: Evidențiere curbe Fill", g11_s19_fill_between),
        "12": ("S20: Histplot cu curbă KDE", g12_s20_histplot),
    }

    while True:
        print("\n" + "=" * 60)
        print("🖥️  PANOUL DE CONTROL ABSOLUT: PARTEA 1 (GRAFICELE 1 - 12)")
        print("=" * 60)
        for numar, date_grafic in toate_graficele.items():
            print(f"{numar.ljust(3)} -> {date_grafic[0]}")
        print("all -> EXECUTĂ TOATE GRAFICELE DIN ACEASTĂ COLECȚIE")
        print("0   -> Închide Panoul")
        print("=" * 60)

        selectie = input("Introdu numărul vizualizării dorite: ").strip()

        if selectie in toate_graficele:
            toate_graficele[selectie][1]()
        elif selectie.lower() == "all":
            for cheie in sorted(toate_graficele.keys(), key=int):
                toate_graficele[cheie][1]()
        elif selectie == "0":
            break


if __name__ == "__main__":
    afiseaza_meniu_p1()
