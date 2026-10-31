# Bug Log dan Regression Check – Pertemuan 15

**Proyek:** Sistem Rekap dan Analisis Nilai Matematika Kelas  
**Pelaksana:** Iren Ihdina Zulfa (2225250019, 3E)

## BUG-01 – Path input menunjuk folder

| Komponen | Keterangan |
|---|---|
| Gejala | Program dapat berhenti dengan traceback ketika path input bukan file, melainkan folder. |
| Cara reproduksi pada versi P14 | Jalankan fungsi pembacaan dengan path berupa direktori, misalnya `baca_data(Path(folder))`; pada versi awal `main` hanya menangani `FileNotFoundError` dan `UnicodeError`. |
| Akar penyebab | Membuka direktori sebagai file pada sistem tertentu menimbulkan `IsADirectoryError` (turunan `OSError`), yang belum ditangani di alur utama. |
| Perbaikan P15 | Tambahkan blok `except OSError as error` saat membaca data agar muncul pesan `Gagal membuka file input: ...`. |
| Bukti test | `TC15` pada `tests/test_program.py`. |
| Hasil retest | PASS pada pengujian paket ini. |
| Status | Closed (untuk kode yang disertakan). |

## Regression check
Setelah perbaikan, uji ulang kasus normal dan batas (TC01–TC14), serta pengujian tambahan penyimpanan, integrasi, dan KKM (TC16–TC19). Semua test dijalankan dengan `unittest`.

## Catatan
Ini bukan klaim bahwa bug terjadi pada perangkat pengguna. Bug merupakan jalur error yang dapat direproduksi dari rancangan P14, lalu ditangani pada implementasi P15. Dokumentasikan bug lain di sini jika muncul pada VS Code milikmu.
