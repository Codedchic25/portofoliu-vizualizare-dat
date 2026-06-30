#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Rezolvarea Temelor de Curs - Partea 1 (Sesiunile 18, 19, 20).

Acest modul reunește scripturile funcționale pentru temele practice
propuse cursanților în primele capitole de vizualizare statică.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# ==================================================================
# TEME SESIUNEA 18: INTRODUCERE MATPLOTLIB
# ==================================================================
def tema_18_1_temperaturi_saptamanale():
    """Cerintă: Creează un grafic cu temperaturile zilnice pentru o săptămână."""
    zile = ["Lun", "Mar", "Mie", "Joi", "Vin", "Sâm", "Dum"]
    temperaturi = [18, 20, 19, 22, 25, 24, 21]

    plt.figure()
    plt.plot(zile, temperaturi, marker="o", color="orange", linestyle="-")
    plt.title("Tema 18.1: Temperaturi zilnice pe o săptămână")
    plt.xlabel("Ziua Săptămânii")
    plt.ylabel("Temperatură (°C)")
    plt.grid(True)
    plt.show()


def tema_18_2_bare_categorii():
    """Cerintă: Fă un grafic cu vânzări pe categorii (bare)."""
    categorii = ["Electro", "Fashion", "Home", "Books"]
    vanzari = [12000, 8500, 6200, 3100]

    plt.figure()
    plt.bar(categorii, vanzari, color="purple")
    plt.title("Tema 18.2: Vânzări pe categorii de produse")
    plt.xlabel("Categorie")
    plt.ylabel("Vânzări totale (RON)")
    plt.show()


def tema_18_3_scatter_aleator():
    """Cerintă: Desenează un scatter plot cu puncte aleatoare și observă distribuția."""
    np.random.seed(42)
    x = np.random.rand(100)
    y = np.random.rand(100)

    plt.figure()
    plt.scatter(x, y, color="teal", alpha=0.7)
    plt.title("Tema 18.3: Scatter plot cu 100 de puncte aleatoare")
    plt.xlabel("Axa X")
    plt.ylabel("Axa Y")
    plt.show()


def tema_18_4_subplot_combinat():
    """Cerintă: Combină două grafice diferite într-un subplot."""
    x = np.linspace(0, 10, 50)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.figure(figsize=(10, 4))

    # Primul subplot: Sinus
    plt.subplot(1, 2, 1)
    plt.plot(x, y1, color="blue")
    plt.title("Funcția Sinus")

    # Al doilea subplot: Cosinus
    plt.subplot(1, 2, 2)
    plt.plot(x, y2, color="red")
    plt.title("Funcția Cosinus")

    plt.suptitle("Tema 18.4: Subplot combinat")
    plt.tight_layout()
    plt.show()


# ==================================================================
# TEME SESIUNEA 19: MATPLOTLIB AVANSAT
# ==================================================================
def tema_19_1_fill_between_variatie():
    """Cerintă: Folosește fill_between pentru a evidenția variația dintre două serii."""
    x = np.linspace(0, 10, 50)
    limita_inferioara = np.sin(x)
    limita_superioara = np.sin(x) + 0.8

    plt.figure()
    plt.plot(x, limita_inferioara, color="black", label="Min")
    plt.plot(x, limita_superioara, color="black", label="Max")
    plt.fill_between(x, limita_inferioara, limita_superioara, color="cyan", alpha=0.4)
    plt.title("Tema 19.1: Evidențiere variație (Fill Between)")
    plt.legend()
    plt.show()


# ==================================================================
# TEME SESIUNEA 20: SEABORN MEDIU
# ==================================================================
def tema_20_1_boxplot_gen():
    """Cerintă: Creează un boxplot în funcție de gen folosind dataset-ul tips."""
    df_tips = sns.load_dataset("tips")

    plt.figure()
    sns.boxplot(x="sex", y="total_bill", data=df_tips, palette="Pastel1")
    plt.title("Tema 20.1: Distribuția notei de plată în funcție de gen")
    plt.show()


def tema_20_2_pairplot_iris():
    """Cerintă: Creează un pairplot pentru dataset-ul iris."""
    df_iris = sns.load_dataset("iris")
    # Generarea matricei de ploturi pe baza speciei de floare
    sns.pairplot(df_iris, hue="species", palette="dark")
    plt.show()


if __name__ == "__main__":
    print("=== Execuție Teme Partea 1 ===")
    tema_18_1_temperaturi_saptamanale()
    # Poti decomenta restul funcțiilor pentru a le testa pe rând
