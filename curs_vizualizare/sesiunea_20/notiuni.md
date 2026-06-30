# Sesiunea 20 - Vizualizare Statistică cu Seaborn (Arbore Conceptual)

- 📌 Sesiunea 20: Introducere Seaborn
  ├── 🎯 Obiectiv Core: Automatizarea vizualizărilor statistice complexe și design modern
  ├── 🏗️ Structură și Conectivitate
  │   ├── Dependent: Construit direct peste fundația Matplotlib
  │   └── Set de date nativ: Încărcare automată din cloud (`sns.load_dataset`)
  ├── 📊 Analiza Distribuțiilor Monetare/Numerice
  │   ├── Histogramă + KDE combinat (`sns.histplot(kde=True)`)
  │   └── Grafic de densitate pur (`sns.kdeplot(fill=True)`)
  ├── 📈 Relații și Analize de Regresie
  │   ├── Scatter avansat colorat pe clase (`sns.scatterplot(hue=...)`)
  │   └── Regresie liniară automată cu interval de încredere (`sns.lmplot`)
  ├── 🍱 Vizualizări Categorice și Multidimensionale
  │   ├── Boxplot statistic clasic (`sns.boxplot`) -> Cvartile și outlieri clari
  │   └── Violin plot combinat splitat pe genuri (`sns.violinplot(split=True)`)
  ├── 🧩 Matrice Exploratorii Automate
  │   ├── Toate corelațiile posibile perechi-perechi (`sns.pairplot`)
  │   └── Corelație tabelară vizuală (`sns.heatmap` + `numeric_only=True`)
  └── 🎨 Setări Stilistice Rapide
      ├── Schimbare fundal grid (`sns.set_style("whitegrid")`)
      └── Palete cromatice gata definite (`sns.set_palette("pastel")`)
