"""Fungsi validasi dan klasifikasi nilai pada proyek individu."""

from math import isfinite

def validasi_nilai(nilai):
    """True hanya untuk nilai numerik berhingga antara 0 dan 100."""
    return (
        isinstance(nilai, (int, float))
        and not isinstance(nilai, bool)
        and isfinite(nilai)
        and 0 <= nilai <= 100
    )

def tentukan_status(nilai, kkm=75):
    """Tentukan status ketuntasan; batas KKM bersifat inklusif."""
    if not validasi_nilai(nilai):
        raise ValueError("Nilai harus berupa angka dalam rentang 0-100.")
    if not validasi_nilai(kkm):
        raise ValueError("KKM harus berupa angka dalam rentang 0-100.")
    return "Tuntas" if nilai >= kkm else "Belum tuntas"
