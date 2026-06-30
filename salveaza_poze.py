import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

# 1. Salvare Suprafață 3D Wave
fig1 = plt.figure()
ax1 = fig1.add_subplot(projection="3d")
x = y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
ax1.plot_surface(x, y, z, cmap="coolwarm", antialiased=True)
plt.title("Topografie Matematică: Proiecție 3D")
plt.savefig("suprafata_3d.png", dpi=150, bbox_inches="tight")
plt.close(fig1)

# 2. Salvare Radar Spider Chart
atribute = ["Viteză", "Fiabilitate", "Design", "Preț", "Baterie"]
unghiuri = np.linspace(0, 2 * np.pi, len(atribute), endpoint=False).tolist()
unghiuri += unghiuri[:1]
val_a = [4.5, 4.2, 4.8, 3.5, 4.6, 4.5]
fig2, ax2 = plt.subplots(subplot_kw=dict(polar=True))
plt.xticks(unghiuri[:-1], atribute)
ax2.plot(unghiuri, val_a, color="red", linewidth=2)
ax2.fill(unghiuri, val_a, color="red", alpha=0.25)
plt.title("Analiză Comparativă Atribute")
plt.savefig("grafic_radar.png", dpi=150, bbox_inches="tight")
plt.close(fig2)

# 3. Salvare Simulare Interfață Login Corporate (Afișaj tabel SQL curat)
fig3, ax3 = plt.subplots(figsize=(6, 2))
ax3.axis("off")
date_tabel = [
    ["ID", "Utilizator", "Acțiune / Notă", "Dată și Oră"],
    ["1", "admin", "Autentificare Reușită", "2026-07-01 00:05"],
    ["2", "admin", "Nota: Audit finalizat", "2026-07-01 00:10"],
]
tabel = ax3.table(cellText=date_tabel, loc="center", cellLoc="center")
tabel.auto_set_font_size(False)
tabel.set_fontsize(10)
tabel.scale(1, 1.5)
plt.title("🛡️ Sistem Enterprise Audit local SQLite", y=1.1)
plt.savefig("interfata_login.png", dpi=150, bbox_inches="tight")
plt.close(fig3)

print("[SUCCES] Toate cele 3 imagini au fost salvate automat în folderul principal!")
