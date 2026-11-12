"""Verifikasi referensi: (1) metadata vs Crossref, (2) konsistensi sitasi dalam teks vs daftar pustaka,
(3) opsional: pencocokan kutipan Inggris pada Bagian 8 terhadap teks PDF sumber.

Pemakaian: python3 scripts/verify_references.py [--source-txt path/ke/lipnik.txt]
Keluaran : docs/verification_report.md
"""
import argparse, html, json, re, sys, unicodedata, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
refs = json.loads((ROOT / "data/references.json").read_text(encoding="utf-8"))
body = (ROOT / "report/laporan_sintesis_literatur.md").read_text(encoding="utf-8")

def norm(t):
    t = html.unescape(t); t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()

def crossref(doi):
    req = urllib.request.Request("https://api.crossref.org/works/" + doi, headers={"User-Agent": "lit-synthesis-verify/1.0"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)["message"]

lines = ["# Laporan Verifikasi Referensi", "",
         "Dihasilkan oleh `scripts/verify_references.py`. Setiap DOI dibandingkan dengan metadata Crossref.", "",
         "| Ref | DOI | Judul | Penulis 1 | Tahun | Vol/No | Halaman | Hasil |", "|---|---|---|---|---|---|---|---|"]
ok_all = True
for r in refs:
    try:
        m = crossref(r["doi"])
    except Exception as e:
        lines.append(f"| {r['key']} | {r['doi']} | ERR | | | | | GAGAL: {e} |"); ok_all = False; continue
    title_ok = norm(m["title"][0]) == norm(r["title"])
    au_ok = norm(m["author"][0]["family"]) == norm(r["first_author"])
    years = {m.get(k, {}).get("date-parts", [[None]])[0][0] for k in ("issued", "published-print", "published-online")}
    yr_ok = r["year"] in years
    vol_ok = (m.get("volume") or "") == r["volume"] and (not r["issue"] or (m.get("issue") or "") == r["issue"])
    pg = (m.get("page") or m.get("article-number") or "").replace("-", "–")
    if not pg:  # Crossref tanpa halaman: gunakan akhiran DOI (pola OJS Univ. Primorska) dan cek manual pada PDF
        mm = re.search(r"\.(\d+)-(\d+)$", r["doi"])
        pg = f"{mm.group(1)}–{mm.group(2)}" if mm else ""
    pg_ok = pg == r["pages"]
    doi_ok = norm(m["DOI"]) == norm(r["doi"])
    res = all([title_ok, au_ok, yr_ok, vol_ok, pg_ok, doi_ok])
    ok_all &= res
    mark = lambda b: "✓" if b else "✗"
    lines.append(f"| {r['key']} | {r['doi']} {mark(doi_ok)} | {mark(title_ok)} | {mark(au_ok)} | {mark(yr_ok)} | {mark(vol_ok)} | {mark(pg_ok)} | {'LULUS' if res else 'PERIKSA'} |")

# --- konsistensi sitasi ---
main = body.split("# 11. DAFTAR PUSTAKA")[0] + body.split("# LAMPIRAN A")[-1]
main = re.sub(r"https?://\S+|DOI\s+10\.\S+", "", main)
pat = re.compile(r"([A-ZŠČ][A-Za-zÀ-ž\-]+(?: [A-Z][a-zÀ-ž]+)?)(?: et al\.|(?: (?:&|dan) [A-ZŠČ][A-Za-zÀ-ž ]+?))?,? \(?((?:19|20)\d\d)\)?")
cited = {}
for mt in pat.finditer(main):
    nm = re.sub(r"^(Hanya|Sedangkan|Pada|Studi|Model)\s+", "", mt.group(1))
    cited[(nm, mt.group(2))] = cited.get((nm, mt.group(2)), 0) + 1
known = {(r["first_author"], str(r["year"])) for r in refs}
# nama rekan penulis (dari string sitasi) juga diterima, mis. 'Lipnik dan Čepar (2025)'
known |= {(nm.strip(), str(r["year"])) for r in refs for nm in re.split(r" & | et al\.,? ?|, \d{4}", r["cite"]) if nm.strip() and not nm.strip().isdigit()}
STOP = {"Hanya", "November"}
unknown = sorted(k for k in cited if k[0] not in STOP and k[0].split()[-1] not in STOP and not any(k[1] == y and (k[0].startswith(a) or a.startswith(k[0])) for a, y in known))
unused = sorted(r["key"] for r in refs if (r["first_author"] not in main) or str(r["year"]) not in main)
lines += ["", "## Konsistensi sitasi", "",
          f"- Referensi yang tidak dikutip di teks: {unused or 'tidak ada'}",
          f"- Sitasi (penulis, tahun) tanpa entri referensi: {unknown or 'tidak ada'}"]
cite_ok = not unused and not unknown
# pastikan string `cite` tiap referensi muncul
for r in refs:
    n = main.count(r["cite"].split(",")[0].replace(" & ", " & "))
    lines.append(f"- {r['cite']}: nama muncul {n}x di teks")

# --- kutipan terjemahan ---
tr_ok = None
ap = argparse.ArgumentParser(); ap.add_argument("--source-txt")
a = ap.parse_args()
if a.source_txt and Path(a.source_txt).exists():
    src = norm(re.sub(r"-\n\s*", "", Path(a.source_txt).read_text(encoding="utf-8")))
    sec = body.split("**Teks Bahasa Inggris")[1].split("**Terjemahan Bahasa Indonesia**")[0]
    bullets = [re.sub(r"^>\s*(- )?", "", l).strip() for l in sec.splitlines() if l.startswith(">")]
    bullets = [b for b in bullets if b and not b.startswith("*")]
    miss = []
    for b in bullets:
        for sent in re.split(r"(?<=[.;])\s+", b):
            if len(sent.split()) > 4 and norm(sent) not in src:
                miss.append(sent)
    tr_ok = not miss
    lines += ["", "## Kecocokan kutipan Inggris dengan teks PDF sumber", "",
              "Seluruh kalimat cocok (setelah normalisasi spasi/tanda baca)." if tr_ok else "Tidak cocok:\n" + "\n".join(f"- {m}" for m in miss)]

lines += ["", "## Ringkasan", "", f"- Metadata Crossref: {'SEMUA LULUS' if ok_all else 'ADA YANG PERLU DIPERIKSA'}",
          f"- Konsistensi sitasi: {'LULUS' if cite_ok else 'PERIKSA'}",
          f"- Kutipan terjemahan: {'LULUS' if tr_ok else ('PERIKSA' if tr_ok is False else 'tidak diperiksa')}"]
(ROOT / "docs/verification_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines[-4:]))
sys.exit(0 if ok_all and cite_ok and tr_ok is not False else 1)
