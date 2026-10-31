"""Membaca data dari berkas CSV sederhana dan menulis laporan teks."""

from pathlib import Path
from utilitas import validasi_nilai, tentukan_status

def baca_data(path):
    """Baca baris NIM,nama,nilai; kembalikan (data_valid, peringatan)."""
    data = []
    peringatan = []
    nim_terpakai = set()

    with open(path, "r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()
            if not baris:
                continue

            bagian = [kolom.strip() for kolom in baris.split(",")]
            if len(bagian) != 3:
                peringatan.append(f"Baris {nomor}: format harus NIM,nama,nilai.")
                continue

            nim, nama, teks_nilai = bagian
            if not nim or not nama:
                peringatan.append(f"Baris {nomor}: NIM atau nama kosong.")
                continue
            if nim in nim_terpakai:
                peringatan.append(f"Baris {nomor}: NIM {nim} duplikat.")
                continue

            try:
                angka = float(teks_nilai)
            except ValueError:
                peringatan.append(f"Baris {nomor}: nilai '{teks_nilai}' bukan angka.")
                continue

            if not validasi_nilai(angka):
                peringatan.append(f"Baris {nomor}: nilai harus di antara 0 dan 100.")
                continue

            data.append({"nim": nim, "nama": nama, "nilai": angka})
            nim_terpakai.add(nim)

    return data, peringatan

def simpan_laporan(path, data, statistik, kkm):
    """Buat laporan lengkap di path; hanya untuk statistik nonkosong."""
    if statistik is None:
        raise ValueError("Tidak ada data valid untuk dilaporkan.")

    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write("LAPORAN NILAI MATEMATIKA KELAS\n")
        file.write(f"KKM: {kkm:g}\n")
        file.write(f"Jumlah siswa: {statistik['jumlah_data']}\n")
        file.write(f"Rata-rata: {statistik['rata_rata']:.2f}\n")
        file.write(f"Minimum: {statistik['minimum']:.2f}\n")
        file.write(f"Maksimum: {statistik['maksimum']:.2f}\n")
        file.write(f"Tuntas: {statistik['jumlah_tuntas']}\n")
        file.write(f"Belum tuntas: {statistik['jumlah_belum_tuntas']}\n")
        file.write("\nRINCIAN SISWA\n")

        for siswa in data:
            status = tentukan_status(siswa["nilai"], kkm)
            file.write(
                f"{siswa['nim']} | {siswa['nama']} | "
                f"{siswa['nilai']:g} | {status}\n"
            )
