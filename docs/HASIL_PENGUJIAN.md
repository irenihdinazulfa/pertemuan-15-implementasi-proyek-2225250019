# Bukti Pengujian Otomatis – Pertemuan 15

Program diuji dengan Python `3.13.5` menggunakan `unittest` bawaan Python di lingkungan pembuatan paket.

**Perintah:**

```bash
python -m unittest discover -s tests -v
```

**Hasil akhir pada paket ini:**

```text
----------------------------------------------------------------------
Ran 19 tests in 0.007s

OK
```

**Pengujian end-to-end:** `python src/main.py` menghasilkan ringkasan 6 siswa, rata-rata 69.17, nilai minimum 0, maksimum 100, 4 tuntas, 2 belum tuntas; laporan dibuat otomatis di `output/laporan_nilai.txt`.

**Pengujian invalid:** `python src/main.py --input data/nilai_uji_invalid.txt --output output/laporan_uji_invalid.txt` melewati baris `abc`, nilai 105, NIM duplikat, dan baris tanpa format benar sambil melanjutkan record valid.

**Regression check:** Semua test case awal beserta test tambahan dijalankan setelah perubahan `src/main.py`, termasuk TC15 untuk path direktori.

File output tidak dimasukkan Git karena dihasilkan kembali dari data contoh. Foto terminal pengguna, bila diminta dosen, bisa ditambahkan secara manual pada `docs/screenshot/`.
