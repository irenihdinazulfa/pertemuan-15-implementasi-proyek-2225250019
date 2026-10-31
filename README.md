# Proyek Akhir Individu – Implementasi dan Pengujian (Pertemuan 15)

**Judul:** Sistem Rekap dan Analisis Nilai Matematika Kelas Berbasis Python  
**Nama:** Iren Ihdina Zulfa  
**NIM:** 2225250019  
**Kelas:** 3E  
**Pelaksana:** Individu sesuai arahan dosen

## Deskripsi dan keterkaitan Pertemuan 14
Proyek ini melanjutkan rancangan **Pertemuan 14**, bukan mengganti topiknya. Pengguna utamanya adalah guru matematika yang ingin membaca data nilai siswa, memvalidasinya, menghitung statistik kelas, menentukan ketuntasan berdasarkan KKM, dan menyimpan laporan teks.

Dokumen rancangan awal tetap tersedia pada [proposal.md](proposal.md) dan [pseudocode](rancangan/pseudocode.md).

## Fitur utama
1. Membaca berkas teks berformat `NIM,nama,nilai` dengan encoding UTF-8.
2. Melewati baris kosong dan data tidak valid sambil menampilkan peringatan.
3. Memvalidasi rentang nilai 0–100 serta menolak NIM duplikat.
4. Menghitung jumlah siswa, rata-rata, minimum, dan maksimum.
5. Menentukan jumlah **Tuntas** dan **Belum tuntas** memakai KKM 75 (nilai tepat KKM termasuk tuntas).
6. Menyimpan laporan rinci ke `output/laporan_nilai.txt`.
7. Menangani file hilang, file yang bukan berkas biasa, KKM salah, dan kegagalan menulis.

## Persyaratan
- Python 3.9 atau lebih baru.
- VS Code disarankan, tetapi program dapat dijalankan melalui terminal biasa.
- Tidak perlu memasang pustaka tambahan; hanya memakai pustaka standar Python.

## Cara menjalankan
Buka terminal VS Code pada folder utama proyek dan jalankan:

```bash
python src/main.py
```

Untuk data pengujian yang berisi nilai tidak valid:

```bash
python src/main.py --input data/nilai_uji_invalid.txt --output output/laporan_uji_invalid.txt
```

Untuk mengubah KKM (opsional):

```bash
python src/main.py --kkm 80
```

## Format input
Setiap baris memiliki format `NIM,nama,nilai`, tanpa header, misalnya:

```text
A001,Ayu,85
A002,Budi,78
A003,Citra,92
```

Data contoh bersifat fiktif, bukan nilai mahasiswa/siswa sungguhan.

## Contoh hasil
Dengan `data/nilai_contoh.txt` dan KKM 75:

```text
=== REKAP NILAI MATEMATIKA ===
KKM: 75
Jumlah siswa: 6
Rata-rata: 69.17
Minimum: 0.00
Maksimum: 100.00
Tuntas: 4
Belum tuntas: 2
```

## Struktur folder
```text
data/       nilai_contoh.txt, nilai_uji_invalid.txt
src/        main.py, data_io.py, analisis.py, utilitas.py
tests/      test_program.py, test_case.md
docs/       HASIL_PENGUJIAN.md, BUG_LOG.md, PANDUAN_DEMO.md, screenshot/
output/     .gitkeep; laporan hasil dibuat otomatis
rancangan/  pseudocode.md (rancangan Pertemuan 14)
proposal.md
.gitignore
README.md
PANDUAN_GITHUB_P15.md
```

## Cara menguji
Jalankan dari folder utama proyek:

```bash
python -m unittest discover -s tests -v
```

Pengujian meliputi **normal, batas, input tidak valid, file hilang, data kosong, penyimpanan laporan, dan integrasi**. Hasil pengujian paket ini dicatat di [docs/HASIL_PENGUJIAN.md](docs/HASIL_PENGUJIAN.md) dan kasus-kasusnya ada di [tests/test_case.md](tests/test_case.md).

## Debugging, regression check, dan known issues
Pengecekan lanjutan menemukan satu jalur error yang belum ditangani pada versi rancangan: ketika path input berupa direktori, operasi baca dapat menghasilkan `IsADirectoryError`. Penanganan `OSError` ditambahkan pada `src/main.py`; test `TC15` memastikan program menampilkan pesan, bukan traceback. Semua test lama dijalankan ulang sebagai regression check. Lihat [docs/BUG_LOG.md](docs/BUG_LOG.md).

**Known issues:** Program ini ditujukan untuk berkas teks sederhana dengan pemisah koma, bukan CSV kompleks dengan nama yang memuat koma. Laporan output ditulis ulang ketika program dijalankan kembali (sesuai kebutuhan rekap terbaru).

## Tanggung jawab individu
Seluruh pekerjaan perancangan, pembuatan kode, pengujian, perbaikan, dokumentasi, dan pengunggahan GitHub dilakukan sebagai tugas **individu**, atas nama Iren Ihdina Zulfa.

## GitHub dan presentasi
Pembaruan Pertemuan 15 sebaiknya **di-commit ke repository Pertemuan 14 yang sama**, agar pengembangan dari proposal ke implementasi dapat ditelusuri. Gunakan [PANDUAN_GITHUB_P15.md](PANDUAN_GITHUB_P15.md). Pedoman demo 3–5 menit ada di [docs/PANDUAN_DEMO.md](docs/PANDUAN_DEMO.md).

## Referensi/bantuan
- Bahan Ajar Pertemuan 14 dan 15, Algoritma dan Pemrograman FKIP Untirta, 2026/2027 Ganjil.
- Dokumentasi Python 3 (pustaka standar dan `unittest`).
- Pembuatan contoh kode dan dokumentasi dibantu ChatGPT. Seluruh implementasi perlu dipahami dan dapat dijelaskan oleh pemilik tugas.
