
---

### 📘 Fișierul de sinteză teoretică `curs_vizualizare/sesiunea_27/notiuni.md`

Adăugă următorul text explicativ în fișierul teoretic dedicat acestei sesiuni:

```markdown
# Sesiunea 27: Algoritmi Fundamentali (LeetCode) în Python

## 1. Concepte de Analiză și Optimizare Asimptotică
* **Complexitatea Temporală și Spațială (Notația Big O)**: Reprezintă instrumentul matematic prin care măsurăm eficiența unui algoritm pe măsură ce dimensiunea datelor de intrare ($N$) crește la infinit.
* **Tehnica Două Indicatoare (Two Pointers)**: Utilizată pentru optimizarea algoritmilor pe tablouri sortate (ex: *Remove Duplicates* sau *Binary Search*). Permite parcurgerea și modificarea datelor in-place, reducând complexitatea spațială la $O(1)$.
* **Structura de Date Hash Map (Dicționare în Python)**: Permite operații de căutare, inserare și ștergere în timp constant ($O(1)$) în medie. Este esențială pentru reducerea timpului de rulare de la abordări brute de tip pătratic $O(N^2)$ la abordări liniare $O(N)$ (ex: *Two Sum*).
* **Structura de Date Stivă (Stack)**: Funcționează pe principiul LIFO (*Last In, First Out*). Este utilizată nativ în evaluarea expresiilor matematice sau verificarea structurilor imbricate (ex: *Valid Parentheses*).

## 2. Abordarea Problemelor la Interviuri Tehnice
1. **Clarificarea cerinței**: Înțelegerea cazurilor limită (liste goale, numere negative, valori uriașe).
2. **Abordarea Brută (Brute Force)**: Propunerea unei soluții rapide, chiar dacă nu este optimă, pentru a valida logica.
3. **Optimizarea**: Identificarea pașilor redundanți și utilizarea structurilor 