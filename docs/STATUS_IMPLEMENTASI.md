# Status Implementasi – Pemetaan Proposal Pertemuan 14 ke Pertemuan 15

| ID | Kebutuhan rancangan P14 | File/fungsi implementasi P15 | Bukti |
|---|---|---|---|
| F01 | Membaca data nilai | `src/data_io.py` / `baca_data()` | TC05, TC07, TC11–TC13, TC15 |
| F02 | Validasi nilai 0–100 | `src/utilitas.py` / `validasi_nilai()` | TC02–TC04, TC14 |
| F03 | Rata-rata, minimum, maksimum | `src/analisis.py` / `hitung_statistik()` | TC01, TC08, TC17 |
| F04 | Menentukan status ketuntasan | `src/utilitas.py` / `tentukan_status()` | TC06, TC09, TC17 |
| F05 | Menyimpan laporan | `src/data_io.py` / `simpan_laporan()` | TC10, TC16–TC17 |

Fitur tambahan sederhana: parameter CLI `--input`, `--output`, dan `--kkm`; tidak memerlukan GUI atau paket luar.

**Pendekatan individu:** seluruh modul diselesaikan oleh satu pengembang, bukan pembagian tugas fiktif. Jadwal mengikuti P14 untuk rancangan, P15 untuk implementasi, dan P16 untuk demonstrasi.
