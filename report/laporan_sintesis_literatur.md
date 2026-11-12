::: {custom-style="CoverTop"}
SELF-INITIATED PORTFOLIO PROJECT
:::

::: {custom-style="CoverTitle"}
PENGENDALIAN PERSEDIAAN BAHAN BAKU DAN PENGURANGAN FOOD WASTE PADA UMKM KULINER
:::

::: {custom-style="CoverSub"}
Sintesis Literatur Akademik dan Sampel Terjemahan Teknis Inggris–Indonesia
:::

::: {custom-style="CoverSub"}
*Raw Material Inventory Control and Food Waste Reduction in Small Food Businesses*
:::

::: {custom-style="CoverMeta"}
Bidang: Teknik Industri · Manajemen Operasi · Manajemen Rantai Pasok\
Jenis dokumen: Literature Synthesis, Comparative Analysis, Technical Translation, Technical Glossary\
Disusun oleh: Steven\
Tanggal: 12 November 2026
:::

::: {custom-style="CoverNote"}
Dokumen ini adalah proyek portofolio mandiri (*self-initiated portfolio project*). Dokumen ini bukan hasil penelitian lapangan dan bukan publikasi ilmiah. Seluruh isi bersumber dari literatur yang telah dipublikasikan dan diverifikasi metadatanya melalui Crossref, OpenAlex, dan Semantic Scholar. Analisis teks lengkap hanya dilakukan untuk satu artikel; tujuh artikel lainnya dianalisis berdasarkan abstrak (lihat Bagian 3 dan Lampiran A).
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 1. EXECUTIVE SUMMARY

UMKM kuliner mengelola bahan baku yang cepat rusak dengan permintaan harian yang berfluktuasi dan sumber daya analitis yang terbatas. Laporan ini menyintesis delapan publikasi akademik (2018–2025) untuk menjawab: bagaimana pengendalian persediaan dan peramalan permintaan dapat membantu UMKM kuliner mengurangi pemborosan bahan baku sekaligus meningkatkan efisiensi operasional?

1. **Manfaat pengendalian persediaan terdokumentasi pada tingkat kasus, tetapi bukti untuk usaha mikro-kecil sangat tipis.** Studi dua toko roti melaporkan penghematan biaya pengadaan sekitar 15–18% melalui *Economic Order Quantity* (EOQ) tanpa pembusukan bahan (Lipnik & Čepar, 2025).
2. **Meminimalkan *food waste* tidak identik dengan memaksimalkan laba**; kuantitas produksi pemaksimal laba dapat melebihi permintaan yang diharapkan (Lipnik & Čepar, 2025).
3. **Peramalan penjualan restoran berakurasi wajar dapat dicapai dengan model sederhana** (Schmidt et al., 2022), tetapi tidak ada studi dalam korpus yang menguji dampak akurasi ramalan pada volume waste.
4. **Praktik manajemen, termasuk manajemen pasokan, dilaporkan sebagai determinan waste restoran** (Fajriah et al., 2025; Santos Silva & Florêncio de Almeida, 2024). Bukti ini asosiatif, bukan kausal.
5. **Hambatan UMKM**: kompetensi staf, biaya investasi, pencatatan data yang lemah, dan kerumitan perhitungan manual (Filimonau & De Coteau, 2019; Lipnik & Čepar, 2025).

# 2. PENDAHULUAN

*Food waste* dipandang memiliki implikasi ekonomi, lingkungan, dan etika yang besar (Lipnik & Čepar, 2025). Pada produk berumur simpan pendek seperti roti, pemborosan terutama bersumber dari produksi berlebih dan persediaan tak terjual (Lipnik & Čepar, 2025). Kelebihan stok bahan *perishable* berisiko menjadi limbah, sedangkan kekurangan stok menyebabkan penjualan hilang; keseimbangan dua risiko ini adalah inti pengendalian persediaan (Lipnik & Čepar, 2025). Literatur model persediaan produk mudah rusak sangat luas (Chaudhary et al., 2018), dan literatur waste restoran menyoroti determinan perilaku dan manajerial (Santos Silva & Florêncio de Almeida, 2024), tetapi kedua arus ini jarang dipertemukan pada skala usaha kecil.

**Tujuan:** (1) menyintesis literatur pengendalian persediaan, peramalan, dan pengurangan waste; (2) membandingkan temuan, metode, dan keterbatasan; (3) mengidentifikasi *research gap* dan menyusun kerangka konseptual; (4) mendemonstrasikan terjemahan teknis dan glosarium Teknik Industri.

# 3. METODOLOGI PENCARIAN LITERATUR

**Sumber.** API Crossref (sembilan kueri bibliografis), diperkaya OpenAlex, Semantic Scholar, halaman penerbit, dan repositori institusi. Google Scholar tidak digunakan karena tidak dapat diakses secara terprogram. **Kata kunci:** *food waste*, *inventory management/control*, *demand forecasting*, *perishable inventory*, *restaurant*, *small/medium enterprises*, *bakery*, *systematic review*.

**Inklusi.** (a) Artikel jurnal atau prosiding ber-DOI; (b) terbit 2019–2026, dengan satu pengecualian: Chaudhary et al. (2018), disertakan sebagai tinjauan fundamental model persediaan mudah rusak; (c) relevan dengan persediaan, peramalan, *perishable*, atau waste di usaha makanan; (d) metadata cocok pada minimal dua basis data; (e) abstrak atau teks lengkap dapat dibaca.

**Seleksi.** Dari 64 rekaman metadata, delapan artikel dipilih. Dua artikel relevan (DOI 10.1016/j.ijhm.2021.102933 dan 10.1007/s43069-025-00541-x) **dikeluarkan** karena abstrak dan teks lengkapnya tidak dapat diverifikasi.

**Dasar analisis.** Teks lengkap hanya dibaca untuk Lipnik & Čepar (2025); tujuh artikel lain dianalisis dari abstrak terverifikasi, sehingga temuan dan keterbatasannya tidak melampaui isi abstrak (ditandai pada kolom pertama Tabel 1). Artikel jurnal dianggap *peer-reviewed* berdasarkan jurnalnya; Tanizaki et al. (2019) dan Fajriah et al. (2025) adalah makalah prosiding yang penelaahannya tidak diverifikasi terpisah.

# 4. LITERATURE MATRIX

Tabel 1 merangkum kedelapan studi (versi lengkap: `data/literature_matrix.csv` dan `.xlsx`).

<!-- MATRIX -->

# 5. HASIL SINTESIS LITERATUR

## 5.1 Konsep dasar pengendalian persediaan

Pengendalian persediaan menyeimbangkan biaya pemesanan, biaya penyimpanan, dan risiko kehabisan stok. EOQ menentukan ukuran pesanan yang meminimalkan jumlah biaya pemesanan dan penyimpanan dengan asumsi permintaan konstan, harga konstan, dan tanpa kekurangan stok; Newsvendor menangani keputusan satu periode ketika permintaan acak, dengan kuantitas optimal ditentukan rasio kritis antara biaya kekurangan dan kelebihan (Lipnik & Čepar, 2025). Tinjauan 418 artikel (1990–2016) menunjukkan model terus diperkaya faktor diskon harga, kekurangan stok, inflasi, dan nilai waktu uang (Chaudhary et al., 2018).

## 5.2 Peramalan permintaan dalam bisnis kuliner

Schmidt et al. (2022) membandingkan model linear, *ensemble*, dan RNN pada data satu restoran menengah: horizon satu hari mencapai sMAPE 19,6% (model linear), dan horizon satu minggu hanya RNN yang mendekati 20% (19,5%). Tanizaki et al. (2019) menyatakan peramalan di toko nyata memerlukan model spesifik-toko yang memadukan data POS dengan lokasi, cuaca, dan acara. Pada dua toko roti kecil, peramalan masih berbasis tren historis, dan permintaan, ramalan, serta galatnya tidak dicatat sehingga simpangan baku permintaan tak dapat diestimasi; penjualan juga dapat lebih rendah daripada permintaan sebenarnya saat stok habis (Lipnik & Čepar, 2025).

## 5.3 Karakteristik persediaan bahan baku yang mudah rusak

Umur simpan membatasi kebijakan pemesanan: EOQ menyarankan pembelian tepung, gula, dan garam dalam jumlah besar dan lebih jarang, tetapi ragi dibatasi 128 kg per pesanan agar tidak busuk (Lipnik & Čepar, 2025). Untuk produk jadi berumur simpan sangat pendek dengan permintaan acak, penulis yang sama memakai Newsvendor. Model multi-item masih terbatas (Chaudhary et al., 2018), padahal menu kuliner memakai banyak bahan mudah rusak sekaligus. Dalam eksperimen numerik pada ritel, ritel daring yang membuang barang sebelum kedaluwarsa tetap menghasilkan waste lebih sedikit untuk banyak produk, antara lain karena efek *pooling* permintaan (Barto et al., 2024).

## 5.4 Hubungan inventory management dengan food waste

Tinjauan sistematis 80 artikel mengidentifikasi tiga determinan waste restoran: perilaku konsumen, manajemen restoran, dan kebijakan publik (Santos Silva & Florêncio de Almeida, 2024). Tinjauan naratif restoran Asia menyebut manajemen pasokan, gaya penyajian, dan perilaku pelanggan sebagai faktor berpengaruh, dengan mayoritas waste dapat dihindari (Fajriah et al., 2025). Filimonau dan De Coteau (2019) menegaskan waste hospitality kurang diteliti dari perspektif manajemen operasi. Bukti ini **asosiatif**: tinjauan memetakan faktor yang dilaporkan berhubungan dengan waste, bukan mengestimasi efek kausal persediaan. Bukti paling dekat dengan sebab-akibat berasal dari model (Barto et al., 2024; Lipnik & Čepar, 2025) dan bersyarat pada asumsinya.

## 5.5 Strategi pengurangan pemborosan bahan baku

Strategi dalam korpus: EOQ untuk bahan stabil dan Newsvendor untuk produk mudah rusak; pencatatan permintaan dan galat ramalan (Lipnik & Čepar, 2025); peramalan berbasis data penjualan (Schmidt et al., 2022; Tanizaki et al., 2019); perbaikan manajemen pasokan, piring lebih kecil, dan edukasi pelanggan (Fajriah et al., 2025); serta pelatihan karyawan dan kebijakan pendukung (Santos Silva & Florêncio de Almeida, 2024).

## 5.6 Tantangan implementasi pada UMKM

(1) *Data*: pencatatan permintaan belum sistematis (Lipnik & Čepar, 2025), padahal model spesifik-toko butuh data POS (Tanizaki et al., 2019). (2) *Kompetensi dan biaya*: kompetensi internal, pelatihan, dan investasi awal menentukan kelayakan adopsi (Filimonau & De Coteau, 2019). (3) *Kerumitan*: perhitungan manual EOQ dan Newsvendor menyulitkan pemilik usaha kecil (Lipnik & Čepar, 2025). (4) *Kapasitas fisik*: pemesanan tepung 10.000 kg yang direkomendasikan menuntut perluasan gudang (Lipnik & Čepar, 2025).

## 5.7 Analisis komparatif

**Kesamaan.** Seluruh studi memperlakukan waste sebagai masalah yang dapat dikelola lewat keputusan operasional; studi model dan kasus sama-sama menekankan keseimbangan kelebihan–kekurangan stok (Barto et al., 2024; Lipnik & Čepar, 2025), dan tinjauan menempatkan faktor manajerial di antara determinan utama (Fajriah et al., 2025; Santos Silva & Florêncio de Almeida, 2024).

**Perbedaan.** (a) *Tingkat bukti*: hanya Lipnik dan Čepar (2025) menunjukkan nilai moneter perbaikan persediaan pada usaha kecil. (b) *Tujuan peramalan*: Schmidt et al. (2022) meramal penjualan untuk penjadwalan tenaga kerja, bukan persediaan. (c) *Waste dan laba*: Lipnik dan Čepar (2025) menemukan konflik keduanya, sedangkan Barto et al. (2024) menunjukkan, pada ritel, bahwa karakteristik sistem seperti *pooling* memengaruhi besarnya waste.

**Metode terbanyak:** empat tinjauan, dua studi peramalan ML, satu studi kasus dengan model analitik, dan satu studi numerik (Tabel 2).

::: {custom-style="TableCaption"}
Tabel 2. Perbandingan pendekatan metodologis dalam korpus
:::

| Pendekatan | Studi | Kelebihan | Kelemahan |
|:-----------|:------|:----------|:----------|
| Tinjauan | Santos Silva & Florêncio de Almeida (2024); Filimonau & De Coteau (2019); Fajriah et al. (2025); Chaudhary et al. (2018) | Memetakan faktor dan celah secara luas | Asosiatif; tanpa estimasi efek |
| Peramalan ML | Schmidt et al. (2022); Tanizaki et al. (2019) | Memakai data penjualan; akurasi terukur | Butuh data dan keahlian; spesifik-toko; tak dikaitkan dengan waste |
| Model analitik studi kasus | Lipnik & Čepar (2025) | Sederhana, menghasilkan angka keputusan | Asumsi kuat; sampel sangat kecil |
| Simulasi numerik | Barto et al. (2024) | Mengisolasi efek kebijakan | Bukan data lapangan; konteks ritel |

**Faktor paling berpengaruh.** Menurut tinjauan: faktor manajerial (termasuk manajemen pasokan), perilaku konsumen, dan kebijakan publik (Fajriah et al., 2025; Santos Silva & Florêncio de Almeida, 2024); urutan kekuatannya tak dapat ditetapkan dari abstrak. **Penerapan hasil berskala besar pada UMKM:** hanya sebagian. Model ritel dan umum (Barto et al., 2024; Chaudhary et al., 2018) memberi wawasan konseptual tetapi mengandaikan data dan kapasitas yang jarang dimiliki UMKM; penerapan langsung pada skala kecil baru terdokumentasi pada dua toko roti (Lipnik & Čepar, 2025), sehingga generalisasi ke UMKM Indonesia masih hipotesis.

# 6. RESEARCH GAP

**Sudah banyak diteliti:** model persediaan mudah rusak (Chaudhary et al., 2018); determinan waste restoran (Santos Silva & Florêncio de Almeida, 2024); akurasi peramalan penjualan restoran (Schmidt et al., 2022; Tanizaki et al., 2019).

**Masih terbatas** (berlaku untuk delapan studi terverifikasi, bukan seluruh literatur):

1. **Bukti empiris persediaan–waste pada usaha mikro-kecil**: studi toko roti hanya dua kasus, dan penulisnya menyebut literatur masih konseptual atau simulasi (Lipnik & Čepar, 2025).
2. **Kaitan akurasi ramalan dengan volume waste**: studi peramalan melaporkan galat (Schmidt et al., 2022) atau verifikasi model (Tanizaki et al., 2019), bukan dampaknya pada waste.
3. **Model multi-item mudah rusak** terbatas (Chaudhary et al., 2018), padahal mirip kondisi menu kuliner.
4. **Pencatatan data dan *censored demand*** menghambat penerapan model (Lipnik & Čepar, 2025).
5. **Trade-off laba–waste** (Lipnik & Čepar, 2025) belum dikaji lintas jenis usaha.
6. **Konteks Indonesia**: tidak ada studi UMKM kuliner Indonesia dalam korpus ini; ini keterbatasan pencarian, bukan bukti ketiadaan literatur.

**Peluang riset:** studi multikasus pada UMKM kuliner Indonesia yang mengukur volume waste sebelum dan sesudah penerapan EOQ/Newsvendor; uji model peramalan sederhana terhadap waste; alat bantu berbiaya rendah yang mengotomatisasi perhitungan; integrasi faktor perilaku staf dengan model kuantitatif. **Relevansi:** kasus toko roti menunjukkan model klasik berbiaya rendah dapat menghemat nyata, sementara celah di atas menunjukkan dukungan bukti untuk konteks Indonesia masih perlu dibangun.

# 7. KERANGKA KONSEPTUAL

Gambar 1 menyajikan kerangka yang disesuaikan dengan bukti. Setiap panah adalah hubungan yang **dihipotesiskan**; keterangannya menyatakan tingkat dukungan bukti. Faktor kontekstual UMKM diperlakukan sebagai kondisi yang diduga memoderasi hubungan, disusun dari Filimonau dan De Coteau (2019), Lipnik dan Čepar (2025), dan Tanizaki et al. (2019), dan belum diuji sebagai moderator.

![**Gambar 1.** Kerangka konseptual peramalan permintaan hingga efisiensi operasional. Sumber: sintesis penulis dari literatur yang dikaji.](figures/kerangka_konseptual.png){width=4.4in}

# 8. TECHNICAL TRANSLATION

**Sumber (kutipan artikel berlisensi terbuka, bukan teks simulasi):** Špela Lipnik dan Žiga Čepar (2025), *Reducing Food Waste and Boosting Profits through Inventory Management: The Case of Small Slovenian Bakeries*, *Managing Global Transitions, 23*(3), 259–294 (bagian "EOQ Model", hlm. 267–268). DOI: https://doi.org/10.26493/1854-6935.23.259-294. **Lisensi:** CC BY-SA 4.0; terjemahan ini adalah adaptasi dan dilisensikan dengan lisensi yang sama. **Perubahan:** diterjemahkan ke Bahasa Indonesia; kalimat pengantar beserta sitasi internal sumber serta tiga bagian lain (butir "Each order is delivered individually", kalimat "The EOQ model typically applies to a single product or item", dan kalimat "Only the order quantity is directly under our control") dihilangkan agar sesuai panjang cuplikan; judul butir ditambahkan; daftar diformat ulang. Tidak ada perubahan makna.

**Teks Bahasa Inggris (kutipan, ±245 kata)**

> *Key assumptions of the classic EOQ model:*
>
> - Demand rate is known, continuous, constant, independent and uniform over time. In reality, demand often fluctuates seasonally or daily.
> - No stockouts are allowed (the model assumes there are no shortages; demand is always met).
> - All costs are precisely known and do not change (there are fixed order costs – each order has a fixed cost, regardless of the order size – and constant holding costs – the cost to hold or store inventory is known and constant per unit per time period).
> - Lead time is zero (the time between placing an order and receiving it is fixed and known). In reality, suppliers may have inconsistent lead times.
> - Only one product is considered, which means there are no savings from consolidating multiple items into a single order.
> - Inventory is replenished instantly once the order arrives (no gradual stock build-up).
> - The purchase price per unit is constant (i.e. there are no bulk discount incentives).
>
> The inventory cycle involves three variables: (i) the order quantity Q which is the fixed order size always placed; (ii) the cycle time T which is the time between two consecutive orders and depends on the order quantity; and (iii) the demand D which represents the number of units needed in stock during a given period. The quantity entering inventory during the cycle is Q while the quantity exiting is D × T. These two quantities must be equal because the inventory level at the beginning and end of the cycle is zero.

**Terjemahan Bahasa Indonesia**

> *Asumsi utama model EOQ klasik:*
>
> - Laju permintaan diketahui, kontinu, konstan, independen, dan seragam sepanjang waktu. Pada kenyataannya, permintaan sering berfluktuasi secara musiman atau harian.
> - Kehabisan stok (*stockout*) tidak diperbolehkan (model mengasumsikan tidak ada kekurangan persediaan; permintaan selalu terpenuhi).
> - Seluruh biaya diketahui dengan tepat dan tidak berubah (terdapat biaya pemesanan tetap, yaitu setiap pesanan memiliki biaya tetap berapa pun ukuran pesanannya, serta biaya penyimpanan yang konstan, yaitu biaya menyimpan persediaan yang diketahui dan konstan per unit per periode waktu).
> - Waktu tunggu (*lead time*) bernilai nol (selang waktu antara pemesanan dan penerimaan barang bersifat tetap dan diketahui). Pada kenyataannya, waktu tunggu dari pemasok bisa tidak konsisten.
> - Hanya satu produk yang dipertimbangkan, sehingga tidak ada penghematan dari penggabungan beberapa item ke dalam satu pesanan.
> - Persediaan terisi ulang seketika begitu pesanan tiba (tidak ada penumpukan stok secara bertahap).
> - Harga beli per unit konstan (artinya tidak ada insentif diskon pembelian dalam jumlah besar).
>
> Siklus persediaan melibatkan tiga variabel: (i) kuantitas pesanan Q, yaitu ukuran pesanan tetap yang selalu diajukan; (ii) waktu siklus T, yaitu selang waktu antara dua pemesanan berturut-turut yang bergantung pada kuantitas pesanan; dan (iii) permintaan D, yaitu jumlah unit yang dibutuhkan dalam persediaan selama suatu periode tertentu. Kuantitas yang masuk ke persediaan selama siklus adalah Q, sedangkan kuantitas yang keluar adalah D × T. Kedua kuantitas ini harus sama karena tingkat persediaan pada awal dan akhir siklus adalah nol.

**Catatan penerjemah.** (1) *Lead time is zero* dipertahankan sebagai "bernilai nol"; sumber sendiri tidak konsisten karena kalimat dalam kurung menyebut waktu tunggu "tetap dan diketahui", dan terjemahan tidak memperbaikinya. (2) *Stockout* diterjemahkan "kehabisan stok" dan *shortage* "kekurangan persediaan" agar kedua konsep tetap terbedakan. (3) *Holding cost* dan *order cost* mengikuti istilah baku glosarium (Bagian 9); simbol Q, T, D dan notasi D × T dipertahankan. (4) *Cycle time* diterjemahkan "waktu siklus", bukan "waktu daur".

# 9. TECHNICAL GLOSSARY

| English Term | Indonesian Equivalent | Technical Explanation |
|:-------------|:----------------------|:----------------------|
| Inventory Control | Pengendalian Persediaan | Aktivitas merencanakan dan mengatur jumlah serta waktu pemesanan dan penyimpanan barang agar permintaan terpenuhi dengan biaya total minimum. |
| Demand Forecasting | Peramalan Permintaan | Estimasi permintaan masa depan berdasarkan data historis dan faktor eksternal sebagai dasar perencanaan persediaan. |
| Forecast Accuracy | Akurasi Peramalan | Tingkat kedekatan ramalan dengan permintaan aktual, diukur antara lain dengan MAPE atau sMAPE. |
| Reorder Point | Titik Pemesanan Ulang | Tingkat persediaan yang memicu pemesanan baru, setara dengan permintaan selama waktu tunggu ditambah persediaan pengaman. |
| Safety Stock | Persediaan Pengaman | Persediaan tambahan untuk melindungi dari variasi permintaan atau waktu tunggu. |
| Economic Order Quantity (EOQ) | Kuantitas Pemesanan Ekonomis | Ukuran pesanan yang meminimalkan jumlah biaya pemesanan dan biaya penyimpanan; Q* = √(2·S·D/H), dengan S biaya pemesanan per pesanan, D permintaan per periode, dan H biaya penyimpanan per unit per periode. |
| Newsvendor Model | Model Newsvendor (Penjual Koran) | Model satu periode untuk menentukan kuantitas pesanan optimal ketika permintaan acak dan sisa barang bernilai rendah. |
| Critical Ratio | Rasio Kritis | Perbandingan Cu/(Cu + Co) pada model Newsvendor, dengan Cu biaya kekurangan per unit dan Co biaya kelebihan per unit; menentukan tingkat layanan optimal. |
| Lead Time | Waktu Tunggu (Lead Time) | Selang waktu antara pemesanan dan penerimaan barang. |
| Perishable Inventory | Persediaan Mudah Rusak | Persediaan yang nilainya menurun atau yang tidak dapat digunakan lagi setelah umur simpan terlampaui. |
| Shelf Life | Umur Simpan | Lama waktu produk tetap layak digunakan atau dijual dalam kondisi penyimpanan yang ditentukan. |
| Food Waste | Limbah Pangan (Sisa Pangan) | Pangan yang masih layak konsumsi namun dibuang atau tidak dimanfaatkan pada tahap rantai pasok setelah panen. |
| Inventory Turnover | Perputaran Persediaan | Rasio biaya barang terjual terhadap rata-rata nilai persediaan; menunjukkan seberapa cepat persediaan berputar. |
| Stockout | Kehabisan Stok | Kondisi ketika permintaan tidak terpenuhi karena persediaan habis, sehingga timbul penjualan hilang atau pesanan tertunda. |
| Overstocking | Kelebihan Stok | Persediaan melebihi kebutuhan, yang meningkatkan biaya penyimpanan dan risiko kerusakan. |
| Holding Cost | Biaya Penyimpanan | Biaya menyimpan persediaan, antara lain ruang, pendinginan, asuransi, kerusakan, dan biaya modal. |
| Ordering Cost | Biaya Pemesanan | Biaya tetap setiap pesanan, di luar harga barang, seperti administrasi dan pengiriman. |
| Base-Stock Policy | Kebijakan Base-Stock | Kebijakan peninjauan periodik: pesan sebanyak selisih antara tingkat target dan posisi persediaan. |
| Salvage Value | Nilai Sisa (Salvage) | Nilai pemulihan per unit barang yang tidak terjual, misalnya dijual dengan diskon atau diolah kembali. |
| Supply Chain | Rantai Pasok | Jaringan pemasok, produsen, distributor, dan pengecer yang mengalirkan barang, informasi, dan dana hingga konsumen akhir. |

*Definisi glosarium dirumuskan penulis laporan berdasarkan praktik umum Teknik Industri dan manajemen operasi; rumus EOQ memakai notasi S, D, H, sedangkan artikel sumber memakai RC, D, HC untuk besaran yang sama.*

# 10. KESIMPULAN

Sintesis delapan studi menunjukkan bahwa pengendalian persediaan dan peramalan permintaan adalah jalur yang masuk akal untuk menekan waste di UMKM kuliner. Bukti paling konkret berasal dari studi dua toko roti: penghematan biaya pengadaan sekitar 15–18% melalui EOQ, serta temuan bahwa meminimalkan waste tidak otomatis sejalan dengan memaksimalkan laba (Lipnik & Čepar, 2025). Model peramalan sederhana dapat memadai (Schmidt et al., 2022), dan tinjauan menempatkan faktor manajerial sebagai determinan waste (Santos Silva & Florêncio de Almeida, 2024).

Batasannya: rantai dari peramalan hingga efisiensi operasional belum terbukti empiris seluruhnya; banyak bukti bersifat asosiatif atau berbasis model; tujuh dari delapan artikel hanya dianalisis dari abstrak; konteks UMKM Indonesia belum terwakili. Bagi praktisi, langkah paling dapat ditindaklanjuti adalah mencatat permintaan harian dan galat ramalan, lalu menerapkan EOQ untuk bahan tahan lama dan Newsvendor untuk produk mudah rusak dengan mempertimbangkan gudang dan kemampuan staf. Bagi peneliti, prioritasnya studi lapangan multikasus yang mengukur volume waste langsung.

# 11. DAFTAR PUSTAKA

<!-- REFERENCES -->

# LAMPIRAN A. KETERBATASAN SUMBER DAN PROSES VERIFIKASI

**Verifikasi.** (1) Setiap DOI dicocokkan dengan Crossref (judul, penulis, tahun, jurnal, volume, halaman) oleh `scripts/verify_references.py`; hasil di `docs/verification_report.md`. (2) Abstrak dibaca dari Crossref, OpenAlex, atau Semantic Scholar. (3) Hanya Lipnik dan Čepar (2025) dibaca penuh; seluruh angka laporan (€1.951; 18,35%; €712,26; 128 kg; 55 roti) berasal dari teks itu. (4) Skrip yang sama memeriksa setiap referensi dikutip dan setiap sitasi punya entri. (5) Teks Inggris Bagian 8 dicocokkan kalimat demi kalimat dengan PDF sumber.

**Keterbatasan.** Tujuh dari delapan artikel hanya dianalisis dari abstrak; empat di antaranya (Filimonau & De Coteau, 2019; Chaudhary et al., 2018; Barto et al., 2024; Santos Silva & Florêncio de Almeida, 2024) tidak dapat diunduh karena pembatasan akses. Korpus kecil dan bukan tinjauan sistematis lengkap, tanpa penilaian kualitas formal (misalnya PRISMA, CASP). Google Scholar, Scopus, dan Web of Science tidak digunakan langsung. Nama penulis ketiga Fajriah et al. (2025) mengikuti metadata Crossref ("Hustina Rachman, P.").

