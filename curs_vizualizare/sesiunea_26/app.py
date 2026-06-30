#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesiunea 26: Integrare Streamlit cu Baze de Date, Autentificare și Deployment.

Implementează un sistem securizat de autentificare locală bazat pe starea sesiunii
și o conexiune securizată la o bază de date SQLite pentru stocarea logurilor.
"""

import sqlite3
import pandas as pd
import streamlit as st


# ------------------------------------------------------------------
# CONFIGURARE ȘI MANAGEMENT BAZĂ DE DATE (SQLite Nativ)
# ------------------------------------------------------------------
def init_baza_date():
    """Inițializează conexiunea SQLite și creează tabela de audit dacă lipsește."""
    conexiune = sqlite3.connect("platforma_hr.db")
    cursor = conexiune.cursor()

    # Creare tabelă de audit securizată
    interogare_tabel = """
    CREATE TABLE IF NOT EXISTS loguri_acces (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        utilizator TEXT NOT NULL,
        actiune TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(interogare_tabel)
    conexiune.commit()
    conexiune.close()


def adauga_log_audit(utilizator, actiune):
    """Inserează o înregistrare nouă în tabela de securitate/audit."""
    conexiune = sqlite3.connect("platforma_hr.db")
    cursor = conexiune.cursor()

    interogare_insert = "INSERT INTO loguri_acces (utilizator, actiune) VALUES (?, ?)"
    parametri = (utilizator, actiune)

    cursor.execute(interogare_insert, parametri)
    conexiune.commit()
    conexiune.close()


def extrage_loguri_audit():
    """Returnează toate logurile stocate în baza de date ca o listă de tupluri."""
    conexiune = sqlite3.connect("platforma_hr.db")
    cursor = conexiune.cursor()

    cursor.execute("SELECT * FROM loguri_acces ORDER BY id DESC")
    rezultate = cursor.fetchall()

    conexiune.close()
    return rezultate


# ------------------------------------------------------------------
# COMPONENTELE INTERFEȚEI GRAFICE (Streamlit UI)
# ------------------------------------------------------------------
def afiseaza_ecran_autentificare():
    """Randează formularul securizat de login."""
    st.subheader("🔑 Autentificare Securizată")

    user_input = st.text_input("Nume utilizator")
    pass_input = st.text_input("Parolă", type="password")

    if st.button("Conectare"):
        # Verificare credențiale (Sistem simplificat bazat pe reguli stricte)
        if user_input == "admin" and pass_input == "HR2026":
            st.session_state["autentificat"] = True
            st.session_state["utilizator_curent"] = user_input

            # Înregistrare eveniment în baza de date
            adauga_log_audit(user_input, "Autentificare Reusita")
            st.rerun()
        else:
            st.error("Utilizator sau parolă incorectă!")


def afiseaza_panou_principal():
    """Randează aplicația securizată disponibilă doar utilizatorilor logați."""
    utilizator = st.session_state.get("utilizator_curent", "Anonim")
    st.success(f"🔓 Conectat ca: **{utilizator}**")

    # Buton de delogare (Clear State)
    if st.button("Deconectare"):
        st.session_state["autentificat"] = False
        st.session_state["utilizator_curent"] = None
        st.rerun()

    st.write("---")
    st.subheader("🖥️ Panou Administrativ")

    # Formular interactiv pentru introducere date conectat la baza de date
    st.markdown("### Modul Audit Intern (Bază de date SQL)")
    text_actiune = st.text_input("Adaugă o notă administrativă în baza de date")

    if st.button("Salvează Notă"):
        if text_actiune:
            adauga_log_audit(utilizator, f"Nota: {text_actiune}")
            st.toast("Datele au fost salvate în SQL!")
        else:
            st.warning("Câmpul text nu poate fi gol.")

    # Afișarea înregistrărilor din baza de date direct în Streamlit
    st.write("---")
    st.subheader("📜 Istoric Loguri (Preluat direct din SQLite)")

    date_loguri = extrage_loguri_audit()
    if date_loguri:
        nume_coloane = ["ID", "Utilizator", "Acțiune / Notă", "Dată și Oră"]
        # Convertim lista de tupluri din SQL într-un DataFrame Pandas cu coloane explicite
        df_loguri = pd.DataFrame(date_loguri, columns=nume_coloane)
        st.dataframe(df_loguri)
    else:
        st.info("Nu există loguri stocate în baza de date.")


def ruleaza_aplicatia():
    """Punctul central de management al stării sesiunii."""
    st.title("🛡️ Aplicație Enterprise: SQL, Autentificare & Cloud")

    # Inițializare variabile de sesiune dacă nu există
    if "autentificat" not in st.session_state:
        st.session_state["autentificat"] = False
        st.session_state["utilizator_curent"] = None

    # Rutare ecran în funcție de starea de login
    if st.session_state["autentificat"]:
        afiseaza_panou_principal()
    else:
        afiseaza_ecran_autentificare()


if __name__ == "__main__":
    init_baza_date()
    ruleaza_aplicatia()
