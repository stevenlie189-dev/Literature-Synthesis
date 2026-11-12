"""Membangun dist/Laporan_Sintesis_Literatur.docx (+ PDF bila LibreOffice tersedia).

Alur: report/*.md + data/*.json  ->  Markdown gabungan  ->  pandoc (reference.docx bergaya)  ->  pasca-proses python-docx
(tabel, bagian lanskap untuk literature matrix, nomor halaman).
"""
import copy, json, re, shutil, subprocess, sys
from pathlib import Path
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"; BUILD.mkdir(exist_ok=True)
DIST = ROOT / "dist"; DIST.mkdir(exist_ok=True)
NAVY = RGBColor(0x1F, 0x38, 0x64)
FONT = "Times New Roman"

# ---------- 1. Markdown gabungan ----------
refs = json.loads((ROOT / "data/references.json").read_text(encoding="utf-8"))
matrix = json.loads((ROOT / "data/literature_matrix.json").read_text(encoding="utf-8"))
md = (ROOT / "report/laporan_sintesis_literatur.md").read_text(encoding="utf-8")

cols = ["Penulis dan Tahun", "Judul Penelitian", "Tujuan Penelitian", "Metodologi", "Variabel atau Aspek yang Dikaji",
        "Temuan Utama", "Keterbatasan Penelitian", "Relevansi terhadap UMKM Kuliner", "DOI atau Link Sumber"]
widths = [3, 11, 13, 13, 11, 22, 14, 13, 8]  # bobot relatif lebar kolom (setelah kolom No.)
esc = lambda t: t.replace("|", "\\|")
tbl = ["**Tabel 1.** Literature matrix", "", "| No. | " + " | ".join(cols) + " |",
       "|" + "-" * 3 + "|" + "|".join("-" * w for w in widths) + "|"]
for i, r in enumerate(matrix, 1):
    cells = [f"{r['Penulis dan Tahun']} [{r['Dasar Analisis'].lower()}]", r["Judul Penelitian"]] + [r["ringkas"][c] if c in r["ringkas"] else r[c] for c in cols[2:]]
    cells[-1] = cells[-1].replace("https://doi.org/", "doi:")
    tbl.append(f"| {i} | " + " | ".join(esc(c) for c in cells) + " |")
tbl_md = "\n".join(tbl)
md = md.replace("<!-- MATRIX -->", '::: {custom-style="TableCaption"}\nTabel 1. Literature matrix (landscape)\n:::\n\n' + tbl_md.split("\n", 2)[2])
ref_md = "\n\n".join('::: {custom-style="Reference"}\n' + r["apa"] + "\n:::" for r in sorted(refs, key=lambda x: x["apa"]))
md = md.replace("<!-- REFERENCES -->", ref_md)
md_path = BUILD / "laporan_gabungan.md"; md_path.write_text(md, encoding="utf-8")
(ROOT / "report" / "figures").mkdir(exist_ok=True)

# ---------- 2. reference.docx ----------
ref_docx = BUILD / "reference.docx"
with open(ref_docx, "wb") as f:
    f.write(subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], capture_output=True, check=True).stdout)
d = Document(ref_docx)

def setfont(style, size=None, bold=None, italic=None, color=None, name=FONT):
    f = style.font; f.name = name
    rpr = style.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"): rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
    if size: f.size = Pt(size)
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
    if color is not None: f.color.rgb = color

def para(style, before=0, after=6, line=1.15, align=None, left=None, hanging=None, keep_next=None):
    pf = style.paragraph_format
    pf.space_before, pf.space_after, pf.line_spacing = Pt(before), Pt(after), line
    if align is not None: pf.alignment = align
    if left is not None: pf.left_indent = Cm(left)
    if hanging is not None: pf.first_line_indent = Cm(-hanging)
    if keep_next is not None: pf.keep_with_next = keep_next

class _S:
    def __init__(self, styles): self.styles = styles
    def __getitem__(self, n):
        for st in self.styles:
            if st.name == n: return st
        raise KeyError(n)
    def __iter__(self): return iter(self.styles)
    def add_style(self, *a, **k): return self.styles.add_style(*a, **k)
S = _S(d.styles)
for n in ("Normal", "Body Text", "First Paragraph", "Compact"):
    setfont(S[n], 10)
for n in ("Body Text", "First Paragraph"):
    para(S[n], 0, 4, 1.04, WD_ALIGN_PARAGRAPH.JUSTIFY)
para(S["Compact"], 0, 2, 1.1)
setfont(S["Heading 1"], 13, True, False, NAVY); para(S["Heading 1"], 10, 4, 1.0, keep_next=True)
setfont(S["Heading 2"], 11, True, False, NAVY); para(S["Heading 2"], 6, 2, 1.0, keep_next=True)
setfont(S["Heading 3"], 11, True, True, NAVY); para(S["Heading 3"], 8, 3, 1.1, keep_next=True)
setfont(S["Block Text"], 9.5); para(S["Block Text"], 2, 4, 1.1, WD_ALIGN_PARAGRAPH.JUSTIFY, left=0.8)
setfont(S["Image Caption"], 9.5, False, True); para(S["Image Caption"], 2, 10, 1.0, WD_ALIGN_PARAGRAPH.CENTER)
for nm in ("Captioned Figure", "Figure"):
    if nm in [x.name for x in S]: para(S[nm], 6, 2, 1.0, WD_ALIGN_PARAGRAPH.CENTER)

def add(name, **kw):
    st = S.add_style(name, WD_STYLE_TYPE.PARAGRAPH); st.base_style = S["Normal"]
    setfont(st, kw.pop("size", 11), kw.pop("bold", None), kw.pop("italic", None), kw.pop("color", None))
    para(st, **kw); return st
add("CoverTop", size=11, bold=True, color=RGBColor(0x59, 0x59, 0x59), before=90, after=24, align=WD_ALIGN_PARAGRAPH.CENTER)
add("CoverTitle", size=22, bold=True, color=NAVY, before=0, after=18, line=1.2, align=WD_ALIGN_PARAGRAPH.CENTER)
add("CoverSub", size=13, before=0, after=8, align=WD_ALIGN_PARAGRAPH.CENTER)
add("CoverMeta", size=11, before=60, after=30, line=1.5, align=WD_ALIGN_PARAGRAPH.CENTER)
add("CoverNote", size=9.5, italic=True, before=30, after=0, line=1.15, align=WD_ALIGN_PARAGRAPH.JUSTIFY, left=1.0)
add("TableCaption", size=10, bold=True, before=6, after=4, line=1.0, keep_next=True)
add("Reference", size=9.5, before=0, after=3, line=1.05, align=WD_ALIGN_PARAGRAPH.LEFT, left=1.0, hanging=1.0)
d.save(ref_docx)

# ---------- 3. pandoc ----------
out = BUILD / "raw.docx"
subprocess.run(["pandoc", str(md_path), "-f", "markdown+pipe_tables+fenced_divs+raw_attribute-smart",
                "-o", str(out), "--reference-doc", str(ref_docx), "--resource-path", str(ROOT / "report")], check=True)

# ---------- 4. pasca-proses ----------
doc = Document(out)
body = doc.element.body
lang = OxmlElement("w:lang"); lang.set(qn("w:val"), "id-ID"); lang.set(qn("w:eastAsia"), "id-ID")
dd = doc.styles.element.find(qn("w:docDefaults")); rpr = dd.find(".//" + qn("w:rPr")) if dd is not None else None
if rpr is not None: rpr.append(lang)

sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.0); sec.top_margin = sec.bottom_margin = Cm(1.9)

def set_cell_bg(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement("w:shd")
    sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hexcolor); tcPr.append(sh)

def set_borders(tbl):
    tblPr = tbl._tbl.tblPr
    for e in tblPr.findall(qn("w:tblBorders")): tblPr.remove(e)
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "4"); e.set(qn("w:space"), "0"); e.set(qn("w:color"), "A6A6A6"); b.append(e)
    tblPr.append(b)

def cell_margins(tbl, tw=60):
    tblPr = tbl._tbl.tblPr; m = OxmlElement("w:tblCellMar")
    for side, v in (("top", 30), ("left", tw), ("bottom", 30), ("right", tw)):
        e = OxmlElement(f"w:{side}"); e.set(qn("w:w"), str(v)); e.set(qn("w:type"), "dxa"); m.append(e)
    tblPr.append(m)

def repeat_header(row):
    trPr = row._tr.get_or_add_trPr(); h = OxmlElement("w:tblHeader"); h.set(qn("w:val"), "true"); trPr.append(h)

def no_split(row):
    trPr = row._tr.get_or_add_trPr(); c = OxmlElement("w:cantSplit"); c.set(qn("w:val"), "true"); trPr.append(c)

tables = doc.tables
for ti, t in enumerate(tables):
    set_borders(t); cell_margins(t)
    ncols = len(t.columns)
    is_matrix = ncols == 10
    is_kv = ncols == 2
    size = 6.5 if is_matrix else (9 if is_kv else 8)
    for ri, row in enumerate(t.rows):
        no_split(row) if not is_matrix else None
        for c in row.cells:
            for p in c.paragraphs:
                p.paragraph_format.space_after = Pt(1); p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.line_spacing = 1.0; p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.size = Pt(size); r.font.name = FONT
                    if ri == 0 and not is_kv: r.font.bold = True; r.font.color.rgb = RGBColor(255, 255, 255)
            if ri == 0 and not is_kv: set_cell_bg(c, "1F3864")
            elif is_kv and c is row.cells[0]: set_cell_bg(c, "EAF1FB")
            elif ri % 2 == 0 and not is_kv: set_cell_bg(c, "F2F6FC")
    if not is_kv: repeat_header(t.rows[0])
    t.autofit = False
    tblPr = t._tbl.tblPr
    w = tblPr.find(qn("w:tblW"))
    if w is None: w = OxmlElement("w:tblW"); tblPr.append(w)
    w.set(qn("w:type"), "pct"); w.set(qn("w:w"), "5000")
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)

# lebar kolom tabel non-matrix (area cetak 16.6 cm)
def set_widths(t, ws):
    grid = t._tbl.tblGrid
    for gc, wd in zip(grid.findall(qn("w:gridCol")), ws): gc.set(qn("w:w"), str(int(wd / 2.54 * 1440)))
    for row in t.rows:
        for c, wd in zip(row.cells, ws): c.width = Cm(wd)
for t in tables:
    n = len(t.columns)
    if n == 3: set_widths(t, [3.9, 3.9, 9.2])
    elif n == 4: set_widths(t, [3.4, 5.4, 4.1, 4.2])
    elif n == 2: set_widths(t, [3.2, 13.4])
# kolom tabel kv: 3.2 cm + sisa
for t in tables:
    if len(t.columns) == 2:
        for row in t.rows:
            pass
        # buang baris header kosong dari pandoc
        first = t.rows[0]
        if not "".join(c.text for c in first.cells).strip(): t._tbl.remove(first._tr)

# lebar kolom matrix (cm), total 24.6 untuk A4 lanskap dengan margin 2.54... gunakan margin 1.8 -> 26.1
mw = [0.8, 2.0, 2.9, 2.8, 3.0, 2.4, 4.6, 2.9, 2.9, 2.5]
scale = 27.3 / sum(mw)
for t in tables:
    if len(t.columns) == 10:
        grid = t._tbl.tblGrid
        for gc, wd in zip(grid.findall(qn("w:gridCol")), mw): gc.set(qn("w:w"), str(int(wd * scale / 2.54 * 1440)))
        for row in t.rows:
            for c, wd in zip(row.cells, mw): c.width = Cm(wd * scale)

# ---- footer nomor halaman pada seksi akhir ----
def add_field(par, instr):
    for kind, txt in (("begin", None), (None, instr), ("end", None)):
        r = par.add_run(); r.font.size = Pt(9); r.font.name = FONT
        if kind:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), kind); r._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; r._r.append(it)

last = doc.sections[-1]
fp = last.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r0 = fp.add_run("Sintesis Literatur: Persediaan Bahan Baku dan Food Waste UMKM Kuliner  |  Halaman "); r0.font.size = Pt(9); r0.font.name = FONT
add_field(fp, "PAGE")
last.footer.is_linked_to_previous = False

# ---- bagian lanskap untuk Literature Matrix ----
def find_heading(prefix):
    for p in doc.paragraphs:
        if p.style.name.startswith("Heading 1") and p.text.strip().startswith(prefix): return p
h4, h5 = find_heading("4. LITERATURE MATRIX"), find_heading("5. HASIL SINTESIS")
final = body.find(qn("w:sectPr"))
def sect_para(orient, titlepg=False):
    sp = copy.deepcopy(final)
    for e in sp.findall(qn("w:titlePg")): sp.remove(e)
    pg = sp.find(qn("w:pgSz")); mar = sp.find(qn("w:pgMar"))
    if orient == "land":
        pg.set(qn("w:w"), "16838"); pg.set(qn("w:h"), "11906"); pg.set(qn("w:orient"), "landscape")
        for k in ("top", "bottom"): mar.set(qn(f"w:{k}"), "850")
        for k in ("left", "right"): mar.set(qn(f"w:{k}"), "850")
    else:
        pg.set(qn("w:w"), "11906"); pg.set(qn("w:h"), "16838")
        if pg.get(qn("w:orient")): del pg.attrib[qn("w:orient")]
    if titlepg:
        sp.append(OxmlElement("w:titlePg"))
    p = OxmlElement("w:p"); ppr = OxmlElement("w:pPr"); ppr.append(sp); p.append(ppr); return p
# pgSz/pgMar pada final harus portrait + margin tepat
fp_ = final.find(qn("w:pgSz")); fp_.set(qn("w:w"), "11906"); fp_.set(qn("w:h"), "16838")
fm = final.find(qn("w:pgMar"))
for k in ("top", "bottom", "left", "right"): fm.set(qn(f"w:{k}"), "1134")
for k in ("header", "footer"): fm.set(qn(f"w:{k}"), "708")
h4._p.addprevious(sect_para("port", titlepg=True))
h5._p.addprevious(sect_para("land"))
doc.core_properties.title = "Pengendalian Persediaan Bahan Baku dan Pengurangan Food Waste pada UMKM Kuliner"
doc.core_properties.subject = "Sintesis literatur dan terjemahan teknis (portofolio mandiri)"
doc.core_properties.author = ""
doc.core_properties.language = "id-ID"
target = DIST / "Laporan_Sintesis_Literatur.docx"
doc.save(target); print("DOCX:", target)

# ---------- 5. PDF ----------
soffice = shutil.which("soffice") or shutil.which("libreoffice")
if soffice:
    subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(DIST), str(target)], check=True, capture_output=True)
    print("PDF :", DIST / "Laporan_Sintesis_Literatur.pdf")
