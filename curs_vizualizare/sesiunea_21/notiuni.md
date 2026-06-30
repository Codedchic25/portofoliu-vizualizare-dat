# Sesiunea 21 - Seaborn Avansat: Vizualizări Profesionale (Arbore Conceptual)

- 📌 Sesiunea 21: Seaborn Expert
  ├── 🎯 Obiectiv Core: Generare dashboard-uri statice, analize de resurse umane și segmentări multiple
  ├── 🎲 Pregătire și Simulare Date
  │   └── Generare set sintetic complex (`pd.DataFrame` corporativ cu vârste, salarii și departamente)
  ├── 📊 Grafice Avansate Segmentate
  │   ├── Boxplot multi-variabil (`x=dept`, `y=salary`, `hue=sex`)
  │   └── Violinplot de densitate simetrică splitat pe categorii
  ├── 🧬 Analiză Granulară la Nivel de Punct (Punctuală)
  │   ├── `sns.stripplot(jitter=True)` -> Împrăștiere controlată a punctelor pe categorii
  │   └── `sns.swarmplot` -> Ordonare matematică a punctelor fără nicio suprapunere directă
  ├── 📈 Agregări și Trenduri Temporale
  │   ├── `sns.lineplot` -> Vizualizarea evoluțiilor mediilor pe luni calendaristice
  │   └── `sns.barplot(errorbar="sd")` -> Reprezentarea mediilor cu bare de eroare standard / deviație
  ├── 🧮 Numărare Categorii Directă
  │   └── `sns.countplot` -> Histograma directă a variabilelor pur calitative
  └── 🪟 Segmentare Multi-Fereastră (Grid de Subploturi)
      └── `sns.FacetGrid` -> Generarea automată a unei rețele de grafice pe subgrupuri (Ex: Rând=Dept, Coloană=Sex)
