"""Menggambar kerangka konseptual (report/figures/kerangka_konseptual.png)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parent.parent
plt.rcParams["font.family"] = "DejaVu Sans"
fig, ax = plt.subplots(figsize=(8.4, 7.4), dpi=200)
ax.set_xlim(0, 100); ax.set_ylim(-21, 102); ax.axis("off")

NAVY, TEAL, GREY = "#1F3864", "#2E75B6", "#595959"
ys = [88, 70, 52, 34, 16]
names = ["1. Peramalan Permintaan\n(Demand Forecasting)",
         "2. Perencanaan Persediaan\n(Inventory Planning)",
         "3. Pengendalian Persediaan\nBahan Baku (Raw Material\nInventory Control)",
         "4. Pengurangan Food Waste\n(Food Waste Reduction)",
         "5. Efisiensi Operasional\n(Operational Efficiency)"]
x0, w, h = 3, 38, 10.5
for y, t in zip(ys, names):
    ax.add_patch(FancyBboxPatch((x0, y - h / 2), w, h, boxstyle="round,pad=0.3,rounding_size=1.5",
                                fc="#EAF1FB", ec=NAVY, lw=1.6))
    ax.text(x0 + w / 2, y, t, ha="center", va="center", fontsize=8.6, color=NAVY, fontweight="bold", linespacing=1.3)

labels = [
    "Didukung sebagian: akurasi model ML diuji, tetapi tanpa\nhasil langsung pada persediaan atau waste\n(Schmidt et al., 2022; Tanizaki et al., 2019)",
    "Bukti kasus terbatas: EOQ dan Newsvendor pada\ndua toko roti (Lipnik & Čepar, 2025)",
    "Asosiatif/teoretis: manajemen pasokan sebagai determinan\nwaste; model numerik (Santos Silva & Florêncio de Almeida,\n2024; Fajriah et al., 2025; Barto et al., 2024)",
    "Belum diuji langsung; penghematan biaya dilaporkan\npada kasus tunggal (Lipnik & Čepar, 2025)",
]
for i, t in enumerate(labels):
    ytop, ybot = ys[i] - h / 2 - 0.3, ys[i + 1] + h / 2 + 0.3
    ax.add_patch(FancyArrowPatch((x0 + w / 2, ytop), (x0 + w / 2, ybot), arrowstyle="-|>",
                                 mutation_scale=16, color=TEAL, lw=2))
    ax.text(x0 + w + 3, (ytop + ybot) / 2, t, ha="left", va="center", fontsize=6.9, color=GREY, style="italic", linespacing=1.35)

ax.add_patch(FancyBboxPatch((3, -16), 94, 15, boxstyle="round,pad=0.3,rounding_size=1.5",
                            fc="#FFF4E0", ec="#C55A11", lw=1.3, ls="--"))
ax.text(50, -3.5, "Faktor kontekstual UMKM yang diduga memoderasi hubungan 1-5", ha="center", fontsize=8.4,
        fontweight="bold", color="#C55A11")
ax.text(6, -6.5, "• Umur simpan bahan baku\n• Kualitas pencatatan data penjualan dan permintaan\n• Kompetensi dan pelatihan staf",
        ha="left", va="top", fontsize=7.6, color="#7F3F0B", linespacing=1.4)
ax.text(52, -6.5, "• Biaya investasi awal\n• Waktu tunggu pemasok\n• Kapasitas penyimpanan",
        ha="left", va="top", fontsize=7.6, color="#7F3F0B", linespacing=1.4)
ax.annotate("", xy=(22, 10.5), xytext=(22, -1), arrowprops=dict(arrowstyle="-|>", color="#C55A11", ls="--", lw=1.3))

ax.text(50, 99, "Kerangka Konseptual (hipotetis, berbasis literatur)", ha="center", fontsize=11, fontweight="bold", color=NAVY)
ax.text(50, -19.5, "Panah = hubungan yang dihipotesiskan, bukan hubungan kausal yang telah terbukti. Teks miring = tingkat dukungan bukti.",
        ha="center", fontsize=6.6, color=GREY)
fig.savefig(ROOT / "report/figures/kerangka_konseptual.png", bbox_inches="tight", facecolor="white")
print("OK")
