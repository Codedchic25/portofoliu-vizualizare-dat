#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea Extra: Explorarea Graficelor Avansate și Specializate în Python.

Acest modul acoperă tipuri complexe de vizualizări din Matplotlib și Seaborn,
utile în analiza avansată de date, big data, fizică sau semnale discrete.
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# ==================================================================
# EXEMPLUL 1: GRAFICUL MARGINAL COMUN (sns.jointplot)
# ==================================================================
# CE ESTE: O vizualizare hibridă care combină un grafic de dispersie (bivariat)
#          în centru cu grafice de distribuție univariate (histograme sau KDE)
#          pe marginile axelor.
# LA CE FOLOSEȘTE: Permite analizarea simultană a două lucruri: corelația directă
#                  dintre două variabile ȘI modul în care fiecare variabilă se
#                  distribuie individual pe axa ei.
# SCENARIU REAL: Analiza corelației dintre înălțimea și greutatea pacienților dintr-un
#                spital, observând pe margini care este înălțimea cea mai comună și
#                care este greutatea cea mai frecventă în rândul populației.
# ==================================================================
def rulare_jointplot_marginal():
    """Generează un sns.jointplot folosind setul de date predefinit 'penguins'."""
    print("\n[Rulare] Vizualizare: Grafic Marginal Comun (sns.jointplot)...")

    # Încărcăm un dataset nativ din Seaborn despre pinguini
    df_pinguini = sns.load_dataset("penguins")

    # Eliminăm rândurile cu valori lipsă pentru a evita avertizările la plotare
    df_pinguini = df_pinguini.dropna()

    # Randerăm graficul combinat central + marginale
    # Parametrul 'hue' împarte automat datele pe culori în funcție de specie
    sns.jointplot(
        data=df_pinguini, x="flipper_length_mm", y="bill_length_mm", hue="species"
    )
    plt.suptitle("Explorare Corelație și Distribuție Marginală", y=1.02)
    plt.show()


# ==================================================================
# EXEMPLUL 2: GRAFICUL DE TIP TULPINĂ ȘI FRUNZĂ DIGITALĂ (plt.stem)
# ==================================================================
# CE ESTE: Un grafic discret care randează linii verticale subțiri pornind
#          de la o axă de referință (de obicei zero) până la valoarea punctului,
#          unde plasează un marcator geometric clar.
# LA CE FOLOSEȘTE: Ideal pentru a afișa date discrete, secvențiale sau impulsuri,
#                  evitând iluzia unei linii continue. Scoate în evidență
#                  amplitudinea exactă a fiecărei valori individuale.
# SCENARIU REAL: Monitorizarea erorilor zilnice de sistem într-un server cloud sau
#                afișarea semnalelor audio digitale eșantionate în inginerie.
# ==================================================================
def rulare_stem_discret():
    """Creează un grafic discret de tip Stem pentru o funcție trigonometrică cosinus."""
    print("\n[Rulare] Vizualizare: Grafic de tip Stem (plt.stem)...")

    # Generăm 31 de puncte discrete pe o curbă trigonometrică
    x_date = np.linspace(0.1, 2 * np.pi, 31)
    y_date = np.cos(x_date)

    plt.figure(figsize=(8, 4))

    # Randerăm tulpinile discrete
    # linefmt stabilește culoarea liniei, markerfmt design-ul punctului din vârf
    plt.stem(x_date, y_date, linefmt="gray", markerfmt="D", bottom=0)

    plt.title("Analiză de Semnal: Grafic Discret de tip Stem")
    plt.xlabel("Eșantion (Timp / Spațiu)")
    plt.ylabel("Amplitudine Semnal")
    plt.grid(True, linestyle=":")
    plt.show()


# ==================================================================
# EXEMPLUL 3: DIAGRAMELE DE DENSITATE HEXAGONALĂ (plt.hexbin)
# ==================================================================
# CE ESTE: O vizualizare bidimensională care împarte spațiul graficului într-un
#          fagure format din hexagoane egale, colorând fiecare hexagon mai intens
#          sau mai palid în funcție de volumul de puncte acumulate în el.
# LA CE FOLOSEȘTE: Rezolvă problema aglomerării excesive (overplotting). Atunci când
#                  ai zeci de mii de puncte, un scatter plot clasic devine o pată
#                  solidă de cercuri suprapuse. Hexbin arată exact densitatea lor.
# SCENARIU REAL: Analiza Big Data a coordonatelor GPS pentru 10.000 de taxiuri dintr-un
#                oraș mare pentru a descoperi care sunt intersecțiile cele mai blocate.
# ==================================================================
def rulare_hexbin_densitate():
    """Generează o diagramă hexagonală cu 10.000 de puncte distribuite normal."""
    print(
        "\n[Rulare] Vizualizare: Densitate Hexagonală pentru Big Data (plt.hexbin)..."
    )

    np.random.seed(42)
    # Generăm o populație masivă de date (10.000 de înregistrări)
    x_masiv = np.random.standard_normal(10000)
    y_masiv = np.random.standard_normal(10000)

    plt.figure(figsize=(8, 5))

    # gridsize determină dimensiunea și numărul de hexagoane din fagure
    plt.hexbin(x_masiv, y_masiv, gridsize=30, cmap="Blues")

    # Adăugăm o bară cromatică laterală ca legendă pentru interpretarea densității
    plt.colorbar(label="Număr de puncte concentrate în hexagon")

    plt.title("Fagure de Densitate: Soluție Big Data împotriva Suprapunerii")
    plt.xlabel("Variabila X")
    plt.ylabel("Variabila Y")
    plt.show()


# ==================================================================
# EXEMPLUL 4: GRAFICUL DE VECTORI / CÂMPURI DE FORȚE (plt.quiver)
# ==================================================================
# CE ESTE: O reprezentare bidimensională formată dintr-o matrice de săgeți direcționale.
#          Fiecare săgeată indică o orientare geometrică, iar lungimea ei arată intensitatea.
# LA CE FOLOSEȘTE: Vizualizarea mărimilor fizice vectoriale care dețin simultan o
#                  valoare numerică (intensitate) și o direcție în spațiu.
# SCENARIU REAL: Hărțile meteorologice profesionale care indică direcția curentului de aer
#                și viteza vântului pe teritoriul unei țări în timp real.
# ==================================================================
def rulare_quiver_vectorial():
    """Generează un câmp bidimensional de vectori direcționali cu plt.quiver."""
    print("\n[Rulare] Vizualizare: Câmp de Vectori Direcționali (plt.quiver)...")

    # Creăm o grilă bidimensională de coordonate de tip meshgrid (spațiere de 0.5)
    componenta_ax = np.arange(0, 2 * np.pi, 0.5)
    componenta_ay = np.arange(0, 2 * np.pi, 0.5)
    x_grila, y_grila = np.meshgrid(componenta_ax, componenta_ay)

    # Calculăm direcțiile matematice ale săgeților (vectorii u și v)
    u_directie = np.sin(x_grila)
    v_directie = np.cos(y_grila)

    plt.figure(figsize=(7, 6))

    # Desenăm câmpul vectorial de săgeți profesionale
    plt.quiver(x_grila, y_grila, u_directie, v_directie, color="darkblue")

    plt.title("Harta de Dinamică: Câmp de Vectori Direcționali")
    plt.xlabel("Coordonata Spațială X")
    plt.ylabel("Coordonata Spațială Y")
    plt.grid(True, alpha=0.3)
    plt.show()


# ==================================================================
# BLOCUL PRINCIPAL DE EXECUȚIE SECVENȚIALĂ
# ==================================================================
if __name__ == "__main__":
    print("=== Lansare Aplicație: Sesiunea Extra (Grafice Specializate) ===")

    # Poți lăsa active sau dezactiva prin comentare oricare dintre funcții
    rulare_jointplot_marginal()
    rulare_stem_discret()
    rulare_hexbin_densitate()
    rulare_quiver_vectorial()
