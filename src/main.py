"""Aplikasi final rekap nilai matematika kelas (proyek individu)."""

import argparse
from pathlib import Path
from analisis import hitung_statistik
from data_io import baca_data, simpan_laporan
from utilitas import validasi_nilai

ROOT = Path(__file__).resolve().parent.parent
INPUT_DEFAULT = ROOT / "data" / "nilai_contoh.txt"
OUTPUT_DEFAULT = ROOT / "output" / "laporan_nilai.txt"
KKM_DEFAULT = 75

def jalankan(input_file=INPUT_DEFAULT, output_file=OUTPUT_DEFAULT, kkm=KKM_DEFAULT):
    """Jalankan alur input -> validasi -> statistik -> laporan.

    Return True saat rekap berhasil; False bila tidak ada data atau terjadi error.
    """
    if not validasi_nilai(kkm):
        print("KKM tidak valid: gunakan angka dari 0 sampai 100.")
        return False

    try:
        data, peringatan = baca_data(input_file)
    except FileNotFoundError:
        print(f"File input tidak ditemukan: {input_file}")
        return False
    except UnicodeError:
        print("File input gagal dibaca dengan encoding UTF-8.")
        return False
    except OSError as error:
        # Penyempurnaan dari P14: menangani path direktori/izin akses.
        print(f"Gagal membuka file input: {error}")
        return False

    for pesan in peringatan:
        print(f"Peringatan: {pesan}")

    if not data:
        print("Tidak ada data valid yang dapat dianalisis.")
        return False

    statistik = hitung_statistik(data, kkm)
    print("=== REKAP NILAI MATEMATIKA ===")
    print(f"KKM: {kkm:g}")
    print(f"Jumlah siswa: {statistik['jumlah_data']}")
    print(f"Rata-rata: {statistik['rata_rata']:.2f}")
    print(f"Minimum: {statistik['minimum']:.2f}")
    print(f"Maksimum: {statistik['maksimum']:.2f}")
    print(f"Tuntas: {statistik['jumlah_tuntas']}")
    print(f"Belum tuntas: {statistik['jumlah_belum_tuntas']}")

    try:
        simpan_laporan(output_file, data, statistik, kkm)
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False

    print(f"Laporan berhasil disimpan: {output_file}")
    return True

def main():
    parser = argparse.ArgumentParser(
        description="Rekap dan analisis nilai matematika siswa (tugas individu)."
    )
    parser.add_argument("--input", type=Path, default=INPUT_DEFAULT,
                        help="Path data nilai; format NIM,nama,nilai")
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT,
                        help="Lokasi file laporan hasil")
    parser.add_argument("--kkm", type=float, default=KKM_DEFAULT,
                        help="Batas tuntas antara 0 dan 100 (default 75)")
    args = parser.parse_args()
    return 0 if jalankan(args.input, args.output, args.kkm) else 1

if __name__ == "__main__":
    raise SystemExit(main())
