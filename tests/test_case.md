# Test Case Proyek Akhir – Pertemuan 15

**Nama:** Iren Ihdina Zulfa · **NIM:** 2225250019 · **Kelas:** 3E · **Individu**

Pengujian menggunakan KKM 75 dan rentang nilai valid 0–100. Test mencakup input normal, nilai batas, invalid, list kosong, file I/O, dan integrasi.

| ID | Kategori | Input/kondisi | Expected result | Actual pada pengujian paket | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Nilai 70,80,90 | Rata-rata 80 | 80 | PASS |
| TC02 | Batas | Nilai 0 | Diterima | Diterima | PASS |
| TC03 | Batas | Nilai 100 | Diterima | Diterima | PASS |
| TC04 | Invalid | Nilai 105 | Ditolak | Ditolak | PASS |
| TC05 | File | File input hilang | Pesan error tanpa crash | Pesan error | PASS |
| TC06 | Normal | Nilai 75,80,100 | 3 tuntas | 3 tuntas | PASS |
| TC07 | Invalid | Nilai `abc` | Data dilewati | Dilewati | PASS |
| TC08 | Kosong | List kosong | Statistik None | None | PASS |
| TC09 | Batas | 75 dan 74 dengan KKM 75 | Tuntas; belum tuntas | Sesuai | PASS |
| TC10 | Output | 1 record valid | Laporan tersimpan | Tersimpan | PASS |
| TC11 | Invalid | Format tidak sesuai | Lewati baris | Dilewati | PASS |
| TC12 | Invalid | NIM duplikat | Lewati record kedua | Dilewati | PASS |
| TC13 | Invalid | Nama kosong | Lewati record | Dilewati | PASS |
| TC14 | Invalid | NaN/Infinity | Ditolak | Ditolak | PASS |
| TC15 | File | Path input berupa folder | Pesan tanpa crash | Pesan error | PASS |
| TC16 | Output | Path output berupa folder | Pesan tanpa crash | Pesan error | PASS |
| TC17 | Integrasi | 6 data contoh | Rata-rata 69.17; 4 tuntas | Sesuai | PASS |
| TC18 | Kosong/invalid | Seluruh baris tidak valid | Tidak membuat laporan | Sesuai | PASS |
| TC19 | Invalid | KKM 110 | Ditolak | Ditolak | PASS |

Catatan: Status di atas berasal dari **pengujian otomatis pada paket kode ini**. Jalankan ulang di perangkat sendiri sebelum mengumpulkan:

```bash
python -m unittest discover -s tests -v
```

File `docs/HASIL_PENGUJIAN.md` berisi catatan menjalankan test. Jika mengubah kode, perbarui Actual/Status sesuai hasil terbaru.
