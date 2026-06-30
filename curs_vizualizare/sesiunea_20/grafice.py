"""
Sesiunea 20: Vizualizare Statistică cu Seaborn.

Acest script folosește setul de date celebru 'tips' pentru a exemplifica
analizele de distribuții, corelații, regresii liniare și grafice avansate de tip boxplot.
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Linia cu 'import pandas as pd' a fost ștearsă deoarece Seaborn își încarcă
# seturile de date nativ prin funcția sns.load_dataset()


def incarca_si_pregateste_date():
    """Încarcă setul de date tipic și returnează DataFrame-ul."""
    # Metodă integrată în Seaborn pentru a aduce seturi de date de pe internet
    df = sns.load_dataset("tips")
    return df


def analiză_distribuții(df):
    """Generează histograme și funcții de densitate a probabilităților."""
    # Reprezentarea frecvenței notei de plată, adăugând linia continuă KDE
    sns.histplot(df["total_bill"], kde=True, bins=20, color="skyblue")
    plt.title("Distribuția notelor totale")
    plt.show()

    # Densitatea simplă a bacșișului acordat cu arie plină dedesubt (fill=True)
    sns.kdeplot(df["tip"], fill=True, color="red")
    plt.title("Densitatea bacșișului")
    plt.show()


def analiza_relatii_regresie(df):
    """Analizează corelațiile dintre consumație și valoarea bacșișului."""
    # Scatter plot unde culoarea punctelor se schimbă automat în funcție de gen
    sns.scatterplot(x="total_bill", y="tip", data=df, hue="sex")
    plt.title("Corelație nota totală vs bacșiș")
    plt.show()

    # Creează graficul scatter și desenează automat linia de regresie liniară ideală
    sns.lmplot(x="total_bill", y="tip", data=df)
    plt.show()


def analiza_categorica(df):
    """Afișează distribuția pe categorii discrete (zile ale săptămânii)."""
    # Boxplot care arată mediana, cvartilele și punctele extreme per zi
    sns.boxplot(x="day", y="total_bill", data=df)
    plt.title("Boxplot pe zile")
    plt.show()

    # Violinplot unde jumătatea stângă e pentru Male și cea dreaptă e pentru Female (split=True)
    sns.violinplot(x="day", y="tip", data=df, hue="sex", split=True)
    plt.title("Violin plot pe zile separat pe sexe")
    plt.show()


def genereaza_pairplot(df):
    """Generează automat grafice combinate pentru toate combinările numerice."""
    # Generează o matrice uriașă de corelații grafice direct pe ecran
    sns.pairplot(df, hue="sex")
    plt.show()


def genereaza_heatmap_corelatie(df):
    """Calculează matricea de corelație Pearson și o afișează colorat."""
    # IMPORTANT: numeric_only=True izolează doar coloanele numerice evitând erorile v2026
    corr = df.corr(numeric_only=True)

    # Mapăm valorile numeric în culori de la rece (negativ) la cald (pozitiv)
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Matrice de corelație")
    plt.show()


def testare_tematici_stil(df):
    """Modifică aspectul implicit folosind temele integrate Seaborn."""
    # Setăm stilul curat alb cu linii orizontale de ghidaj
    sns.set_style("whitegrid")
    sns.boxplot(x="day", y="total_bill", data=df)
    plt.title("Boxplot cu stil elegant whitegrid")
    plt.show()

    # Schimbăm paleta de culori în una pastelată moale
    sns.set_palette("pastel")
    sns.violinplot(x="day", y="tip", data=df)
    plt.title("Violin plot cu paletă pastel")
    plt.show()


if __name__ == "__main__":
    date_restaurant = incarca_si_pregateste_date()
    analiză_distribuții(date_restaurant)
    analiza_relatii_regresie(date_restaurant)
    analiza_categorica(date_restaurant)
    genereaza_pairplot(date_restaurant)
    genereaza_heatmap_corelatie(date_restaurant)
    testare_tematici_stil(date_restaurant)
