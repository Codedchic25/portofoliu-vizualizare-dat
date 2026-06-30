#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Galeria de Artă Digitală - Cele Mai Spectaculoase Vizualizări din Curs.

Un panou de control interactiv care reunește și randează cele mai avansate
și spectaculoase grafice din punct de vedere vizual din întregul proiect.
"""

import matplotlib.pyplot as plt
import numpy as np


def arata_donut_ierarhic():
    """1. Gogoașă Stratificată (Donut Chart) pe două niveluri concentrice."""
    print("\n[Randare] Gogoașă Stratificată (Donut Chart)...")
    fig, ax = plt.subplots(figsize=(6, 6))

    # Generare dinamică de date sigure pentru a preveni filtrarea
    valori_exterioare = np.ones(2) * 50
    etichete_exterioare = ["Hardware", "Software"]
    culori_exterioare = ["#ff9999", "#66b3ff"]

    valori_interioare = np.ones(4) * 25
    etichete_interioare = ["Laptop", "PC", "Cloud", "SaaS"]
    culori_interioare = ["#ffcccc", "#ffb3b3", "#99ccff", "#80bfff"]

    # Inelul exterior (Categorii Mari)
    ax.pie(
        valori_exterioare,
        labels=etichete_exterioare,
        radius=1.3,
        colors=culori_exterioare,
        wedgeprops=dict(width=0.3, edgecolor="white"),
        pctdistance=0.85,
    )

    # Inelul interior (Subcategorii)
    ax.pie(
        valori_interioare,
        labels=etichete_interioare,
        radius=1.0,
        colors=culori_interioare,
        wedgeprops=dict(width=0.3, edgecolor="white"),
        labeldistance=0.7,
    )

    # Cercul central alb pentru efectul de gogoașă
    cerc_central = plt.Circle((0, 0), 0.7, color="white")
    ax.add_artist(cerc_central)

    plt.title("Structură Ierarhică: Donut Chart Avansat", y=1.1)
    plt.show()


def arata_radar_spider():
    """2. Grafic Radar (Spider Chart) pe coordonate polare."""
    print("\n[Randare] Grafic Radar (Spider Chart)...")

    atribute = ["Viteză", "Fiabilitate", "Design", "Preț", "Baterie"]
    numar_atribute = len(atribute)

    # Generare vectori de note stabili
    note_premium = np.linspace(4, 5, numar_atribute).tolist()
    note_economic = np.linspace(2, 3, numar_atribute).tolist()

    # Calculul unghiurilor pe cercul polar și închiderea formei geometrice
    unghiuri = [n / float(numar_atribute) * 2 * np.pi for n in range(numar_atribute)]
    unghiuri += unghiuri[:1]
    note_premium += note_premium[:1]
    note_economic += note_economic[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    plt.xticks(unghiuri[:-1], atribute)

    # Produs Premium (Roșu)
    ax.plot(unghiuri, note_premium, color="#ff4d4d", linewidth=2, label="Premium")
    ax.fill(unghiuri, note_premium, color="#ff4d4d", alpha=0.2)

    # Produs Economic (Verde)
    ax.plot(unghiuri, note_economic, color="#33cc33", linewidth=2, label="Economic")
    ax.fill(unghiuri, note_economic, color="#33cc33", alpha=0.2)

    plt.title("Analiză Comparativă Atribute", y=1.1)
    plt.legend(loc="upper right", bbox_to_anchor=(0.1, 0.1))
    plt.show()


def arata_relief_3d():
    """3. Topografie matematică tridimensională continuă."""
    print("\n[Randare] Suprafață 3D Continuă (Surface Plot)...")
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(projection="3d")

    x_puncte = np.arange(-5, 5, 0.25)
    y_puncte = np.arange(-5, 5, 0.25)
    x_grila, y_grila = np.meshgrid(x_puncte, y_puncte)

    distanta = np.sqrt(x_grila**2 + y_grila**2)
    z_inaltime = np.sin(distanta)

    suprafata = ax.plot_surface(
        x_grila, y_grila, z_inaltime, cmap="coolwarm", linewidth=0, antialiased=True
    )
    fig.colorbar(suprafata, shrink=0.5, aspect=5, label="Intensitate Profunzime")
    plt.title("Topografie Matematică: Proiecție 3D")
    plt.show()


def arata_fagure_densitate():
    """4. Diagramă hexagonală pentru volume mari de date (Big Data)."""
    print("\n[Randare] Fagure de Densitate (Hexbin Plot)...")
    np.random.seed(42)

    x_date = np.random.standard_normal(5000)
    y_date = np.random.standard_normal(5000)

    plt.figure(figsize=(8, 5))
    plt.hexbin(x_date, y_date, gridsize=25, cmap="YlGnBu")
    plt.colorbar(label="Concentrație Puncte")
    plt.title("Fagure Hexagonal: Soluție împotriva Suprapunerii Datelor")
    plt.show()


def meniu_interactiv():
    """Meniu consolă pentru selectarea graficului spectacular."""
    while True:
        print("\n=============================================")
        print("🎨 GALERIA DE ARTĂ DIGITALĂ: CELE MAI SPECTACULOASE")
        print("=============================================")
        print("1. Diagrama Gogoașă Stratificată (Donut Chart)")
        print("2. Graficul Păianjen (Radar/Spider Chart)")
        print("3. Suprafața Tridimensională (3D Surface Plot)")
        print("4. Fagure de Densitate (Hexbin Plot)")
        print("all -> RULARE TOATĂ COLECȚIA SPECTACULOASĂ")
        print("0. Ieșire din Galerie")
        print("=============================================")

        optiune = input("Introdu numărul graficului dorit (0-4 / all): ").strip()

        if optiune == "1":
            arata_donut_ierarhic()
        elif optiune == "2":
            arata_radar_spider()
        elif optiune == "3":
            arata_relief_3d()
        elif optiune == "4":
            arata_fagure_densitate()
        elif optiune.lower() == "all":
            arata_donut_ierarhic()
            arata_radar_spider()
            arata_relief_3d()
            arata_fagure_densitate()
        elif optiune == "0":
            print("🎨 Vizită încheiată în galerie!")
            break
        else:
            print("❌ Opțiune invalidă!")


if __name__ == "__main__":
    meniu_interactiv()
