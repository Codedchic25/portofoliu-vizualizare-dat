"""
Sesiunea 18: Vizualizare de Date cu Matplotlib.

Acest script conține exemple practice de grafice fundamentale (linii, bare,
histograme, scatter plots și subploturi) utilizând biblioteca Matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np


def genereaza_grafic_liniar():
    """Generează și afișează un grafic liniar simplu."""
    # Definim datele pentru axele X și Y
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Plotăm linia pe baza coordonatelor
    plt.plot(x, y)
    # Adăugăm titlul principal al graficului
    plt.title("Grafic liniar simplu")
    # Setăm eticheta pentru axa orizontală X
    plt.xlabel("x")
    # Setăm eticheta pentru axa verticală Y
    plt.ylabel("y")
    # Afișăm fereastra cu graficul generat
    plt.show()


def genereaza_grafic_bare():
    """Generează și afișează un grafic cu bare verticale."""
    # Definirea categoriilor (criteriu discret)
    produse = ["Laptop", "Telefon", "Tabletă"]
    # Definirea valorilor asociate fiecărei categorii
    vanzari = [100, 250, 90]

    # Desenăm barele verticale și setăm culoarea verde
    plt.bar(produse, vanzari, color="green")
    # Adăugăm titlul graficului
    plt.title("Vânzări pe produs")
    # Adăugăm eticheta pe axa Y pentru unitatea de măsură
    plt.ylabel("Bucăți vândute")
    # Afișăm graficul pe ecran
    plt.show()


def genereaza_histograma():
    """Generează o histogramă bazată pe o distribuție normală artificială."""
    # Fixăm seed-ul pentru ca numerele aleatoare să fie reproductibile
    np.random.seed(42)
    # Generăm 1000 de note cu media 7 și deviația standard 1.5
    note = np.random.normal(7, 1.5, 1000)

    # Construim histograma împărțind datele în 20 de intervale (bins)
    plt.hist(note, bins=20, color="skyblue")
    # Titlul sugestiv al distribuției statistice
    plt.title("Distribuția notelor")
    # Numim axele pentru claritate interpretativă
    plt.xlabel("Notă")
    plt.ylabel("Număr de elevi")
    # Afișăm rezultatul vizualizării
    plt.show()


def genereaza_scatter_plot():
    """Generează un scatter plot pentru a analiza dispersia punctelor."""
    # Generăm 50 de coordonate aleatoare între 0 și 1 pentru axa X
    x = np.random.rand(50)
    # Generăm 50 de coordonate aleatoare pentru axa Y
    y = np.random.rand(50)

    # Plotăm punctele individuale fără a le uni cu o linie
    plt.scatter(x, y, color="purple")
    # Titlul graficului de dispersie
    plt.title("Puncte aleatoare")
    # Afișarea ecranului grafic
    plt.show()


def genereaza_subploturi():
    """Creează o figură cu două grafice separate dispuse în grilă."""
    # Set de date de bază pentru ambele ploturi
    x = [1, 2, 3, 4]
    y1 = [1, 4, 9, 16]
    y2 = [1, 2, 3, 4]

    # Inițializăm primul grafic dintr-o grilă de 1 rând și 2 coloane (index 1)
    plt.subplot(1, 2, 1)
    plt.plot(x, y1)
    plt.title("Pătrat")

    # Inițializăm al doilea grafic în aceeași grilă (index 2)
    plt.subplot(1, 2, 2)
    plt.plot(x, y2)
    plt.title("Liniar")

    # Adăugăm un titlu global deasupra întregii figuri
    plt.suptitle("Comparare funcții")
    # Ajustăm automat marginile pentru a nu se suprapune textele
    plt.tight_layout()
    # Afișăm figura completă
    plt.show()


def genereaza_grafic_personalizat():
    """Generează un grafic personalizat complex cu legende și caroiaj."""
    x = [1, 2, 3, 4]
    y1 = [1, 4, 9, 16]
    y2 = [1, 2, 3, 4]

    # Plotăm prima linie: culoare roșie, linie întreruptă, marcator cerc
    plt.plot(x, y1, color="red", linestyle="--", marker="o", label="x^2")
    # Plotăm a doua linie: culoare albastră, linie continuă, marcator pătrat
    plt.plot(x, y2, color="blue", linestyle="-", marker="s", label="x")
    # Titlu
    plt.title("Grafic personalizat")
    # Afișăm caseta cu legende (folosește argumentele 'label' setate mai sus)
    plt.legend()
    # Activăm caroiajul de fundal (grid-ul) pentru citire ușoară
    plt.grid(True)
    # Afișăm rezultatul final
    plt.show()


def genereaza_si_salveaza_aplicatie_practica():
    """Rulează un caz practic de vânzări anuale și salvează graficul."""
    luni = ["Ian", "Feb", "Mar", "Apr", "Mai"]
    an2023 = [5000, 7000, 6000, 6500, 8000]
    an2024 = [5200, 6900, 6300, 7000, 8200]

    # Plotăm evoluția ambilor ani pe aceleași axe pentru comparație directă
    plt.plot(luni, an2023, label="2023", marker="o")
    plt.plot(luni, an2024, label="2024", marker="s")
    # Titlu și detalii
    plt.title("Evoluția vânzărilor")
    plt.ylabel("RON")
    plt.legend()

    # Salvăm starea curentă a graficului ca fișier imagine PNG local
    plt.savefig("grafic_vanzari.png")
    # Afișăm graficul după salvare
    plt.show()


if __name__ == "__main__":
    # Apelarea tuturor funcțiilor din sesiune pentru execuție secvențială
    genereaza_grafic_liniar()
    genereaza_grafic_bare()
    genereaza_histograma()
    genereaza_scatter_plot()
    genereaza_subploturi()
    genereaza_grafic_personalizat()
    genereaza_si_salveaza_aplicatie_practica()
