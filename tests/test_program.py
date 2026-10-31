"""Test unit dan integrasi aplikasi proyek akhir (standar unittest)."""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from analisis import hitung_statistik
from data_io import baca_data, simpan_laporan
from main import jalankan
from utilitas import tentukan_status, validasi_nilai

class TestProyekNilai(unittest.TestCase):
    def test_tc01_rata_rata_normal(self):
        data = [{"nilai": 70}, {"nilai": 80}, {"nilai": 90}]
        self.assertEqual(hitung_statistik(data)["rata_rata"], 80)

    def test_tc02_batas_nol(self):
        self.assertTrue(validasi_nilai(0))

    def test_tc03_batas_seratus(self):
        self.assertTrue(validasi_nilai(100))

    def test_tc04_nilai_di_luar_rentang(self):
        self.assertFalse(validasi_nilai(105))

    def test_tc05_file_hilang_ditangani(self):
        with tempfile.TemporaryDirectory() as folder:
            with redirect_stdout(StringIO()) as keluaran:
                berhasil = jalankan(Path(folder) / "hilang.txt",
                                   Path(folder) / "rekap.txt")
            self.assertFalse(berhasil)
            self.assertIn("tidak ditemukan", keluaran.getvalue())

    def test_tc06_semua_tuntas(self):
        data = [{"nilai": 75}, {"nilai": 80}, {"nilai": 100}]
        self.assertEqual(hitung_statistik(data, 75)["jumlah_tuntas"], 3)

    def test_tc07_nilai_abc_dilewati(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nilai.txt"
            path.write_text("A001,Ayu,85\nA002,Budi,abc\n", encoding="utf-8")
            data, peringatan = baca_data(path)
            self.assertEqual(len(data), 1)
            self.assertEqual(len(peringatan), 1)

    def test_tc08_data_kosong(self):
        self.assertIsNone(hitung_statistik([]))

    def test_tc09_batas_kkm(self):
        self.assertEqual(tentukan_status(75, 75), "Tuntas")
        self.assertEqual(tentukan_status(74, 75), "Belum tuntas")

    def test_tc10_simpan_laporan(self):
        data = [{"nim": "A001", "nama": "Ayu", "nilai": 80}]
        statistik = hitung_statistik(data, 75)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "hasil.txt"
            simpan_laporan(path, data, statistik, 75)
            isi = path.read_text(encoding="utf-8")
            self.assertIn("Jumlah siswa: 1", isi)
            self.assertIn("A001 | Ayu | 80 | Tuntas", isi)

    def test_tc11_format_salah_dilewati(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nilai.txt"
            path.write_text("DataTanpaKoma\nA001,Ayu,80\n", encoding="utf-8")
            data, peringatan = baca_data(path)
            self.assertEqual(len(data), 1)
            self.assertIn("format", peringatan[0])

    def test_tc12_nim_duplikat(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nilai.txt"
            path.write_text("A001,Ayu,80\nA001,Budi,90\n", encoding="utf-8")
            data, peringatan = baca_data(path)
            self.assertEqual(len(data), 1)
            self.assertIn("duplikat", peringatan[0])

    def test_tc13_nama_kosong(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nilai.txt"
            path.write_text("A001,,85\n", encoding="utf-8")
            data, peringatan = baca_data(path)
            self.assertEqual(data, [])
            self.assertEqual(len(peringatan), 1)

    def test_tc14_nan_dan_inf_ditolak(self):
        self.assertFalse(validasi_nilai(float("nan")))
        self.assertFalse(validasi_nilai(float("inf")))

    def test_tc15_input_adalah_folder(self):
        # Perbaikan P15: OS error input tertangani, bukan traceback.
        with tempfile.TemporaryDirectory() as folder:
            with redirect_stdout(StringIO()) as keluaran:
                berhasil = jalankan(Path(folder), Path(folder) / "hasil.txt")
            self.assertFalse(berhasil)
            self.assertIn("Gagal membuka file input", keluaran.getvalue())

    def test_tc16_lokasi_output_tidak_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            path_input = Path(folder) / "nilai.txt"
            path_input.write_text("A001,Ayu,85\n", encoding="utf-8")
            with redirect_stdout(StringIO()) as keluaran:
                berhasil = jalankan(path_input, Path(folder))
            self.assertFalse(berhasil)
            self.assertIn("Gagal menyimpan laporan", keluaran.getvalue())

    def test_tc17_proses_akhir_ke_akhir(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / "rekap.txt"
            with redirect_stdout(StringIO()) as keluaran:
                berhasil = jalankan(ROOT / "data" / "nilai_contoh.txt", output)
            self.assertTrue(berhasil)
            self.assertIn("Rata-rata: 69.17", keluaran.getvalue())
            self.assertIn("Tuntas: 4", output.read_text(encoding="utf-8"))

    def test_tc18_data_seluruhnya_invalid(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "invalid.txt"
            output = Path(folder) / "rekap.txt"
            path.write_text("A001,Ayu,abc\n", encoding="utf-8")
            with redirect_stdout(StringIO()) as keluaran:
                berhasil = jalankan(path, output)
            self.assertFalse(berhasil)
            self.assertFalse(output.exists())
            self.assertIn("Tidak ada data valid", keluaran.getvalue())

    def test_tc19_kkm_tidak_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            with redirect_stdout(StringIO()) as keluaran:
                berhasil = jalankan(ROOT / "data" / "nilai_contoh.txt",
                                   Path(folder) / "hasil.txt", 110)
            self.assertFalse(berhasil)
            self.assertIn("KKM tidak valid", keluaran.getvalue())

if __name__ == "__main__":
    unittest.main()
