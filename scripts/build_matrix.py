"""Menghasilkan literature_matrix.csv, literature_matrix.xlsx dari data/literature_matrix.json."""
import csv, json
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side

ROOT = Path(__file__).resolve().parent.parent
rows = json.loads((ROOT / "data/literature_matrix.json").read_text(encoding="utf-8"))
COLS = ["Penulis dan Tahun", "Judul Penelitian", "Tujuan Penelitian", "Metodologi",
        "Variabel atau Aspek yang Dikaji", "Temuan Utama", "Keterbatasan Penelitian",
        "Relevansi terhadap UMKM Kuliner", "DOI atau Link Sumber", "Dasar Analisis"]

with open(ROOT / "data/literature_matrix.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["No."] + COLS)
    for i, r in enumerate(rows, 1):
        w.writerow([i] + [r[c] for c in COLS])

wb = Workbook(); ws = wb.active; ws.title = "Literature Matrix"
ws.append(["No."] + COLS)
for i, r in enumerate(rows, 1):
    ws.append([i] + [r[c] for c in COLS])
widths = [5, 22, 34, 36, 36, 32, 52, 40, 36, 38, 14]
thin = Side(style="thin", color="BBBBBB")
for c, wd in enumerate(widths, 1):
    ws.column_dimensions[ws.cell(1, c).column_letter].width = wd
for row in ws.iter_rows():
    for cell in row:
        cell.alignment = Alignment(wrap_text=True, vertical="top")
        cell.border = Border(top=thin, bottom=thin, left=thin, right=thin)
        cell.font = Font(name="Calibri", size=10)
for cell in ws[1]:
    cell.font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    cell.fill = PatternFill("solid", fgColor="1F3864")
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
for r in range(2, ws.max_row + 1):
    cell = ws.cell(r, 10)
    cell.hyperlink = cell.value; cell.font = Font(name="Calibri", size=10, color="0563C1", underline="single")
ws.freeze_panes = "C2"
wb.save(ROOT / "data/literature_matrix.xlsx")
print("OK:", len(rows), "baris")
