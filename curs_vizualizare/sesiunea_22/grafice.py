#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 22: Plotly pentru Vizualizări Interactive.

Grafice web dinamice folosind Plotly Express și Graph Objects.
"""

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def exemplul_1_linie_simpla():
    """Grafic liniar interactiv."""
    seria_luni = ["Ian", "Feb", "Mar", "Apr", "Mai"]
    date_vanzari_ron = [5000, 7000, 6500, 8000, 7200]

    structura = {"Luna": seria_luni, "Vanzari": date_vanzari_ron}

    df = pd.DataFrame(structura)
    fig = px.line(
        df,
        x="Luna",
        y="Vanzari",
        title="Evolutia Vanzarilor (Interactiv)",
        markers=True,
    )
    fig.show()


def exemplul_2_bar_chart():
    """Diagramă cu bare."""
    seria_luni = ["Ian", "Feb", "Mar", "Apr", "Mai"]
    date_vanzari_ron = [5000, 7000, 6500, 8000, 7200]

    structura = {"Luna": seria_luni, "Vanzari": date_vanzari_ron}

    df = pd.DataFrame(structura)
    fig = px.bar(df, x="Luna", y="Vanzari", color="Luna", title="Vanzari pe Luni")
    fig.show()


def exemplul_3_scatter_plot():
    """Grafic de dispersie cu tooltips."""
    np.random.seed(0)
    df_scatter = pd.DataFrame(
        {
            "x": np.random.randn(100),
            "y": np.random.randn(100),
            "categorie": np.random.choice(["A", "B"], 100),
        }
    )
    fig = px.scatter(
        df_scatter, x="x", y="y", color="categorie", title="Distributie Puncte"
    )
    fig.show()


def exemplul_4_boxplot_violin():
    """Boxplot și Violinplot."""
    df_tips = px.data.tips()
    fig_box = px.box(
        df_tips, x="day", y="total_bill", color="sex", title="Nota Totală pe Zile"
    )
    fig_box.show()

    fig_violin = px.violin(
        df_tips, x="day", y="total_bill", color="sex", box=True, points="all"
    )
    fig_violin.show()


def exemplul_5_heatmap_go():
    """Heatmap cu Graph Objects."""
    z = np.random.rand(5, 5)
    fig = go.Figure(data=go.Heatmap(z=z, colorscale="Viridis"))
    fig.update_layout(title="Heatmap Random (Graph Objects)")
    fig.show()


def exemplul_6_pie_chart():
    """Diagramă circulară."""
    categorii_produse = ["Laptop", "Telefon", "Tabletă"]
    procente_distributie = [40, 35, 25]

    structura = {"Categorie": categorii_produse, "Procent": procente_distributie}

    df_pie = pd.DataFrame(structura)
    fig = px.pie(
        df_pie,
        names="Categorie",
        values="Procent",
        title="Procent Vânzări pe Categorii",
    )
    fig.show()


def exemplul_7_multi_line_chart():
    """Grafic de linii comparativ multi-anual."""
    seria_luni_repetata = ["Ian", "Feb", "Mar", "Apr", "Mai"] * 2
    seria_ani = ["2023"] * 5 + ["2024"] * 5
    toate_vanzarile = [5000, 7000, 6500, 8000, 7200, 4800, 6900, 6400, 7000, 6900]

    structura = {
        "Luna": seria_luni_repetata,
        "Vanzari": toate_vanzarile,
        "An": seria_ani,
    }

    df_comp = pd.DataFrame(structura)
    fig = px.line(
        df_comp,
        x="Luna",
        y="Vanzari",
        color="An",
        markers=True,
        title="Comparatie Vanzari 2023 vs 2024",
    )
    fig.show()


if __name__ == "__main__":
    exemplul_1_linie_simpla()
    # Poti decomenta oricare dintre functiile de mai jos pentru a le testa:
    # exemplul_2_bar_chart()
    # exemplul_3_scatter_plot()
    # exemplul_4_boxplot_violin()
    # exemplul_5_heatmap_go()
    # exemplul_6_pie_chart()
    # exemplul_7_multi_line_chart()
