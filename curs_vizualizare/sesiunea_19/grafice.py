#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 19: Matplotlib Avansat.

Modul dedicat tehnicilor profesionale de personalizare pentru grafice statice.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Date globale pentru functii
x_global = np.linspace(0, 10, 100)
y_global = np.sin(x_global)


def exemplul_1_axe():
    """Configurează limitele și etichetele axelor."""
    plt.figure()
    plt.plot(x_global, y_global)
    plt.title("Sinusul lui x")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.xlim(0, 12)
    plt.ylim(-2, 2)
    plt.xticks(np.arange(0, 11, 2))
    plt.yticks([-1, 0, 1])
    plt.grid(True)
    plt.show()


def exemplul_2_adnotari():
    """Adaugă linii de referință și marcaje text structurate."""
    plt.figure()
    plt.plot(x_global, y_global)
    plt.axhline(0, color="gray", linestyle="--")
    plt.axvline(5, color="red", linestyle=":")
    plt.annotate(
        "Maxim",
        xy=(np.pi / 2, 1),
        xytext=(2, 1.5),
        arrowprops=dict(facecolor="black", arrowstyle="->"),
    )
    plt.show()


def exemplul_3_pandas():
    """Generează grafice direct din structuri de date Pandas."""
    # Definim listele separat pentru a preveni eliminarea lor din text
    lista_luni = ["Ian", "Feb", "Mar", "Apr"]
    date_an_2023 = [1000, 1200, 900, 1500]
    date_an_2024 = [1100, 1250, 1000, 1700]

    structura_date = {"Luna": lista_luni, "2023": date_an_2023, "2024": date_an_2024}

    vanzari = pd.DataFrame(structura_date)
    vanzari.set_index("Luna").plot(kind="bar")
    plt.title("Comparatie Vanzari 2023 vs 2024")
    plt.ylabel("Valoare RON")
    plt.show()


def exemplul_4_heatmap():
    """Afișează o matrice de corelație bidimensională colorată."""
    data = np.random.rand(5, 5)
    plt.imshow(data, cmap="viridis", interpolation="nearest")
    plt.colorbar()
    plt.title("Heatmap aleatoare")
    plt.show()


def exemplul_5_pie():
    """Construiește o diagramă circulară clasică."""
    etichete = ["Mere", "Pere", "Banane"]
    procente_fructe = [40, 30, 30]

    plt.pie(procente_fructe, labels=etichete, autopct="%1.1f%%")
    plt.title("Distributie fructe")
    plt.show()


def exemplul_6_fill():
    """Colorează aria delimitată dintre două funcții diferite."""
    x_fill = np.linspace(0, 10, 100)
    y1 = np.sin(x_fill)
    y2 = np.sin(x_fill) + 0.5
    plt.fill_between(x_fill, y1, y2, color="orange", alpha=0.5)
    plt.title("Zona dintre sin(x) și sin(x)+0.5")
    plt.show()


if __name__ == "__main__":
    exemplul_1_axe()
    exemplul_2_adnotari()
    exemplul_3_pandas()
    exemplul_4_heatmap()
    exemplul_5_pie()
    exemplul_6_fill()
