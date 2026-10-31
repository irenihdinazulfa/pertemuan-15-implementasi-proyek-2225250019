# Panduan Demo 3–5 Menit – Persiapan Pertemuan 16

**Proyek individu:** Sistem Rekap dan Analisis Nilai Matematika Kelas.

1. **Pembuka (30 detik):** jelaskan kebutuhan guru matematika untuk mengolah nilai kelas.
2. **Tunjukkan input (30 detik):** buka `data/nilai_contoh.txt`; jelaskan format `NIM,nama,nilai`.
3. **Jalankan program (60 detik):** `python src/main.py`; tunjukkan rata-rata 69.17, nilai minimum 0, maksimum 100, dan 4 siswa tuntas.
4. **Tunjukkan output (30 detik):** buka `output/laporan_nilai.txt` yang dibuat otomatis.
5. **Uji data invalid (45 detik):** `python src/main.py --input data/nilai_uji_invalid.txt --output output/laporan_uji_invalid.txt`; tunjukkan baris invalid dilewati.
6. **Test dan debugging (45 detik):** `python -m unittest discover -s tests -v`; jelaskan `TC15` dan penanganan `OSError`.
7. **Penutup (20 detik):** tampilkan README dan commit bertahap di GitHub.

**Tiga fungsi yang penting dipahami:**
- `baca_data()`: parsing dan validasi file nilai.
- `hitung_statistik()`: rekap nilai dan ketuntasan.
- `simpan_laporan()`: hasil output berupa laporan teks.

**Saran bukti:** simpan screenshot terminal uji dan tampilan laporan di folder `docs/screenshot/` jika diminta dosen. Screenshot belum otomatis dibuat dari VS Code pengguna.
