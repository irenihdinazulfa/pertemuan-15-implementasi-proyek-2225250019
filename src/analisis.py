"""Logika statistik dan ketuntasan kelas; terpisah dari input/output."""

from utilitas import tentukan_status, validasi_nilai

def hitung_statistik(data, kkm=75):
    """Kembalikan ringkasan kelas atau None untuk data kosong."""
    if not validasi_nilai(kkm):
        raise ValueError("KKM harus berada pada rentang 0-100.")
    if not data:
        return None

    nilai = [siswa["nilai"] for siswa in data]
    if not all(validasi_nilai(angka) for angka in nilai):
        raise ValueError("Data mengandung nilai tidak valid.")

    jumlah_tuntas = sum(
        tentukan_status(angka, kkm) == "Tuntas" for angka in nilai
    )
    return {
        "jumlah_data": len(nilai),
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai),
        "jumlah_tuntas": jumlah_tuntas,
        "jumlah_belum_tuntas": len(nilai) - jumlah_tuntas,
    }
