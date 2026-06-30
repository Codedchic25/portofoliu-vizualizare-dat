# Sesiunea 26: Integrare Baze de Date, Autentificare și Deployment Cloud

## 1. Concepte de Arhitectură Web și Securitate
* **Managementul Stării Sesiunii (`st.session_state`)**: Deoarece Streamlit re-rulează scriptul complet de la zero la fiecare click sau input, variabilele standard locale se resetează. `st.session_state` acționează ca un dicționar global persistent pe durata vizitei utilizatorului, fiind esențial pentru stocarea stării de login (`True`/`False`).
* **Integrare SQL Securizată**: Utilizarea bazelor de date relaționale presupune programare defensivă prin parametrizarea interogărilor (folosirea caracterului `?` în loc de formatarea clasică de string-uri). Acest mecanism blochează complet atacurile de tip **SQL Injection**.
* **Pregătirea pentru Cloud Deployment**: Pentru publicarea unei aplicații Streamlit pe platforme cloud (ex: Streamlit Community Cloud), este obligatorie crearea unui fișier numit `requirements.txt` în rădăcina proiectului, care să conțină toate dependențele externe codificate exact.

## 2. Ghid rapid pentru Deployment Cloud
1. Salvați codul într-un depozit privat sau public de **GitHub**.
2. Asigurați-vă că structura conține modulele standard în rădăcină.
3. Accesați `share.streamlit.io`, conectați contul de GitHub și selectați fișierul principal `app.py` pentru compilarea automată în cloud.
