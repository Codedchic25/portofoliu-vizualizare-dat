"""
Sesiunea 21: Seaborn Avansat pentru Mediul Corporate.

Acest script generează un set de date sintetic despre angajați (departament, salariu, sex)
și rulează vizualizări avansate de agregare statistică și grile de tip FacetGrid.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def genereaza_dataset_angajati():
    """Creează artificial un tabel de date realist pentru analize HR."""
    # Setăm seed-ul global pentru consistența rezultatelor la rulări repetate
    np.random.seed(42)
    df = pd.DataFrame(
        {
            "sex": np.random.choice(["Male", "Female"], size=100),
            "age": np.random.normal(35, 10, size=100),
            "salary": np.random.normal(5000, 1500, size=100),
            "department": np.random.choice(
                ["IT", "HR", "Marketing", "Sales"], size=100
            ),
            "experience": np.random.randint(1, 15, 100),
        }
    )
    return df


def boxplot_si_violinplot_avansat(df):
    """Rulează grafice comparative avansate pentru structura salarială."""
    plt.figure(figsize=(10, 6))
    # Boxplot complet separat pe culorile paletei Set2
    sns.boxplot(x="department", y="salary", hue="sex", data=df, palette="Set2")
    plt.title("Distribuția salariilor pe departamente, pe sexe")
    plt.show()

    plt.figure(figsize=(10, 6))
    # Reprezentarea sub formă de violoncel cu observarea asimetriilor
    sns.violinplot(
        x="department",
        y="salary",
        hue="sex",
        data=df,
        split=True,
        palette="muted",
    )
    plt.title("Distribuția salariilor cu formă de violoncel")
    plt.show()


def heatmap_si_pairplot_corporate(df):
    """Analizează interacțiunile dintre toate metricile numerice ale angajaților."""
    plt.figure(figsize=(8, 6))
    # Calcul corect excluzând erorile text
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matricea de corelație între variabile")
    plt.show()

    # Matricea automată de corelații vizuale cu densități pe diagonală
    sns.pairplot(df, hue="sex", diag_kind="kde", palette="husl")
    plt.show()


def lineplot_evolutiv(df):
    """Agregă datele pe luni și desenează evoluția trendului."""
    df["luna"] = np.random.choice(["Ian", "Feb", "Mar", "Apr", "Mai"], size=100)
    # Calculăm media salariilor grupate după axa temporală creată
    graf = df.groupby("luna")["salary"].mean().sort_index()

    sns.lineplot(x=graf.index, y=graf.values, marker="o")
    plt.title("Evoluția salariului mediu pe lună")
    plt.ylabel("Salariu mediu")
    plt.show()


def distributie_granulara_puncte(df):
    """Combină două tipuri de plotări de puncte pentru o vizualizare optimă."""
    plt.figure(figsize=(10, 6))
    # Fundal estetic cu dispersie simplă gri semitransparentă
    sns.stripplot(
        x="department", y="salary", data=df, jitter=True, color="gray", alpha=0.6
    )
    # Swarmplot ordonează punctele ca fagurele fără suprapuneri disruptive
    sns.swarmplot(x="department", y="salary", data=df, hue="sex", palette="Set1")
    plt.title("Distribuție granulară a salariilor")
    plt.show()


def barplot_si_countplot_hr(df):
    """Generează grafice de frecvență și medii cu indicatori de eroare standard."""
    plt.figure(figsize=(8, 5))
    # ATENȚIE: errorbar="sd" înlocuiește parametrul vechi ci="sd"
    sns.barplot(x="department", y="salary", data=df, errorbar="sd", palette="Blues")
    plt.title("Salariu mediu și deviație standard pe departament")
    plt.show()

    plt.figure(figsize=(8, 5))
    # Numărarea simplă a capetelor de locuitori pe structuri calitative
    sns.countplot(x="department", hue="sex", data=df, palette="cool")
    plt.title("Numărul de angajați pe departamente și sexe")
    plt.show()


def utilizare_facet_grid(df):
    """Creează un grid masiv de subploturi bazat pe combinații unice de categorii."""
    # Segmentăm rețeaua: pe coloane punem Sexul, pe rânduri punem Departamentele
    g = sns.FacetGrid(df, col="sex", row="department", margin_titles=True)
    # În fiecare celulă mapăm o histogramă cu curbă de densitate orange
    g.map_dataframe(sns.histplot, x="salary", kde=True, color="orange")
    plt.subplots_adjust(top=0.9)
    g.fig.suptitle("Distribuția salariilor pe sexe și departamente")
    plt.show()


if __name__ == "__main__":
    sns.set_theme(style="whitegrid")
    date_firma = genereaza_dataset_angajati()
    boxplot_si_violinplot_avansat(date_firma)
    heatmap_si_pairplot_corporate(date_firma)
    lineplot_evolutiv(date_firma)
    distributie_granulara_puncte(date_firma)
    barplot_si_countplot_hr(date_firma)
    utilizare_facet_grid(date_firma)
