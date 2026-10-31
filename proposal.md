# PROPOSAL PROYEK INDIVIDU — PERTEMUAN 14

## Identitas
- **Nama:** Iren Ihdina Zulfa
- **NIM:** 2225250019
- **Kelas:** 3E
- **Mata kuliah:** Algoritma dan Pemrograman
- **Bentuk tugas:** Individu (penyesuaian dari petunjuk kelompok berdasarkan arahan dosen)
- **Tahun ajaran:** 2026/2027 Ganjil

## 1. Judul Proyek
**Sistem Rekap dan Analisis Nilai Matematika Kelas Berbasis Python**

## 2. Latar Belakang
Guru matematika perlu mengolah nilai siswa untuk mengetahui gambaran hasil belajar dan ketuntasan kelas. Menghitung nilai satu per satu secara manual memerlukan waktu dan berpotensi salah, terutama saat harus memeriksa data yang tidak lengkap atau tidak valid. Karena itu, dirancang program sederhana berbasis terminal untuk membaca data nilai dari file teks, memvalidasi isinya, menghitung statistik kelas, menentukan ketuntasan, dan menyimpan laporan. Ide dan fitur inti proyek mengacu pada contoh workshop dalam Bahan Ajar Pertemuan 14.

## 3. Pengguna dan Tujuan
**Pengguna utama:** guru matematika.  
**User story:** *Sebagai guru matematika, saya ingin membaca data nilai siswa secara otomatis sehingga saya dapat memperoleh statistik dan status ketuntasan yang mudah diperiksa.*

**Tujuan:** mempercepat rekap, meminimalkan kesalahan perhitungan, dan menyediakan laporan teks yang dapat diperiksa kembali.

## 4. Ruang Lingkup
**Fitur wajib:**
1. Membaca file teks berformat `NIM,nama,nilai`.
2. Memvalidasi nilai numerik 0–100, baris kosong, dan format salah.
3. Menghitung rata-rata, minimum, maksimum, dan jumlah siswa.
4. Menghitung jumlah tuntas/belum tuntas berdasarkan KKM.
5. Menyimpan hasil ke laporan `.txt`.

**Batas proyek:** program terminal Python, data contoh sintetis, satu kelas, satu mata pelajaran, tanpa database, login, antarmuka web, atau GUI. **KKM 75** adalah nilai contoh yang dipilih untuk rancangan, bukan ketentuan khusus dari modul.

## 5. Kebutuhan

### Kebutuhan fungsional
| ID | Kebutuhan | Prioritas | Modul |
|---|---|---|---|
| F01 | Membaca file data siswa | Wajib | `data_io.py` |
| F02 | Memvalidasi nilai 0–100 | Wajib | `utilitas.py`, `data_io.py` |
| F03 | Menghitung statistik kelas | Wajib | `analisis.py` |
| F04 | Menentukan ketuntasan berdasar KKM | Wajib | `utilitas.py`, `analisis.py` |
| F05 | Menyimpan laporan teks | Wajib | `data_io.py` |

### Kebutuhan nonfungsional
- Dapat dijalankan di VS Code menggunakan Python 3 tanpa library tambahan.
- Memberikan pesan yang jelas untuk file hilang atau data invalid.
- Kode modular dengan nama fungsi yang mudah dipahami.
- Data contoh tidak menggunakan informasi siswa nyata.
- Test case dapat dijalankan kembali menggunakan `unittest`.

## 6. Spesifikasi Input–Proses–Output (IPO)
| Input | Proses | Output |
|---|---|---|
| `data/nilai_contoh.txt` berisi NIM, nama, nilai; KKM 75 | Baca → validasi → simpan sebagai list dictionary → hitung statistik → tentukan status → rekap | Statistik di terminal dan file `output/laporan_nilai.txt` |

**Format data:** setiap baris `NIM,nama,nilai`; contoh `A001,Ayu,85`. Nilai menggunakan angka 0–100. Data invalid dilewati dengan peringatan.

## 7. Algoritma
1. Tentukan lokasi file input, output, dan KKM.
2. Buka file input; bila tidak ditemukan tampilkan pesan lalu akhiri.
3. Baca baris; lewati baris kosong dan validasi tiap record.
4. Simpan record valid dalam `list[dict]`, laporkan record invalid.
5. Jika tidak ada data valid, tampilkan pesan lalu akhiri.
6. Hitung jumlah siswa, rata-rata, minimum, dan maksimum.
7. Tentukan ketuntasan menggunakan perbandingan nilai `>= KKM`.
8. Tampilkan ringkasan dan simpan laporan teks.

Pseudocode dan flowchart: [`rancangan/pseudocode.md`](rancangan/pseudocode.md).

## 8. Struktur Program dan Folder
```text
pertemuan-14-perancangan-proyek-2225250019/
├── README.md
├── proposal.md
├── .gitignore
├── data/
│   └── nilai_contoh.txt
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   ├── test_case.md
│   └── test_program.py
├── rancangan/
│   └── pseudocode.md
└── output/
    └── .gitkeep
```

| Fungsi | Peran |
|---|---|
| `baca_data(path)` | Membaca file serta mengumpulkan data valid dan peringatan |
| `validasi_nilai(nilai)` | Memvalidasi nilai dalam rentang 0–100 |
| `hitung_statistik(data, kkm)` | Menghasilkan dictionary ringkasan statistik |
| `tentukan_status(nilai, kkm)` | Menentukan tuntas atau belum tuntas |
| `simpan_laporan(path, data, statistik, kkm)` | Menulis laporan teks |
| `main()` | Mengatur proses keseluruhan |

## 9. Pemilihan Struktur Data
- **List:** menyimpan seluruh record siswa valid agar dapat diiterasi.
- **Dictionary:** menyimpan atribut `nim`, `nama`, dan `nilai` tiap siswa serta statistik ringkasan.
- **String:** menyimpan teks NIM/nama, peringatan, dan laporan.
- **File `.txt`:** menyimpan data input dan output secara sederhana.

## 10. Rancangan Test Case
Minimal enam yang dicontohkan modul, ditambah empat kasus penguatan.

| ID | Kategori | Input/kondisi | Expected result |
|---|---|---|---|
| TC01 | Normal | 80,70,90 | Rata-rata 80 |
| TC02 | Batas | Nilai 0 | Diterima |
| TC03 | Batas | Nilai 100 | Diterima |
| TC04 | Invalid | Nilai 105 | Ditolak |
| TC05 | Error file | File tidak ada | Ditangani tanpa crash pada program utama |
| TC06 | Normal | Semua nilai >=75 | Semua tuntas |
| TC07 | Invalid | Nilai `abc` | Dilewati dengan peringatan |
| TC08 | Kosong | List kosong | Statistik tidak dihitung |
| TC09 | Batas KKM | Nilai 75 dan 74 | Tuntas dan belum tuntas |
| TC10 | Output | Satu data valid | Laporan dibuat |

Detail dan perintah tes: [`tests/test_case.md`](tests/test_case.md).

## 11. Penanggung Jawab (Tugas Individu)
Berdasarkan arahan dosen, **seluruh pekerjaan dilaksanakan secara individu**, tanpa anggota kelompok lain. Pembagian peran pada bahan ajar dialihkan menjadi pembagian tanggung jawab pribadi.

| Peran pada modul | PIC individu | Bukti kerja |
|---|---|---|
| Koordinasi dan perencanaan | Iren Ihdina Zulfa | `proposal.md` dan milestone |
| Pengolahan file dan validasi | Iren Ihdina Zulfa | Rancangan `src/data_io.py`, `src/utilitas.py` |
| Logika matematika | Iren Ihdina Zulfa | Rancangan `src/analisis.py` |
| Pengujian / QA | Iren Ihdina Zulfa | `tests/test_case.md`, `tests/test_program.py` |
| Dokumentasi | Iren Ihdina Zulfa | `README.md` dan GitHub |

## 12. Jadwal / Milestone
| Tahap | Target dan bukti |
|---|---|
| Pertemuan 14 | Proposal individu, ruang lingkup, IPO, pseudocode, struktur folder, test case, GitHub |
| Antara P14–P15 | Implementasi awal fitur wajib; integrasi modul |
| Pertemuan 15 | Pengujian, debugging, penyempurnaan, laporan, pembaruan dokumentasi |
| Pertemuan 16 | Demonstrasi hasil proyek, presentasi, evaluasi/UAS |

## 13. Repository GitHub
Rencana alamat repository (aktif setelah repository dibuat dan di-push):  
`https://github.com/irenihdinazulfa/pertemuan-14-perancangan-proyek-2225250019`

## Status Pelaksanaan
**Pertemuan 14 berfokus pada blueprint/rancangan.** Selain proposal, disertakan prototipe awal dan pengujian otomatis sebagai bahan persiapan Pertemuan 15. Prototipe bukan pengganti penjelasan rancangan.

## Referensi
- Bahan Ajar Pertemuan 14, *Perancangan Proyek Program Sederhana*, FKIP Untirta, 2026/2027 Ganjil.
- Bantuan ChatGPT digunakan untuk menyusun contoh kode, kerangka proposal, dan draft dokumentasi; pemilik proyek perlu memahami dan memeriksa hasilnya.
