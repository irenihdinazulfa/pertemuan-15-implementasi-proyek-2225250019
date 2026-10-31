# GitHub: melanjutkan repository Pertemuan 14 (individu)

**Penting:** Menurut bahan ajar Pertemuan 15, ini adalah kelanjutan proposal Pertemuan 14. Perbarui **repository yang sudah digunakan pada Pertemuan 14**; tidak harus membuat repo baru.

1. Buka folder `pertemuan-14-perancangan-proyek-2225250019` milikmu di VS Code.
2. Salin file update P15 dari ZIP ke folder P14 tersebut, ganti file dengan nama sama. Jangan salin `.git` dari ZIP; riwayat Git lama tetap dipertahankan.
3. Jalankan `git status` untuk mengetahui file baru/berubah.
4. Jalankan `python src/main.py` dan `python -m unittest discover -s tests -v`.
5. Commit bertahap (jika ada perubahan):

```bash
git add src/ data/
git commit -m "feat: menyempurnakan implementasi analisis nilai kelas"

git add tests/
git commit -m "test: menambah pengujian batas validasi dan integrasi"

git add README.md docs/ .gitignore PANDUAN_GITHUB_P15.md
git commit -m "docs: melengkapi hasil uji bug log dan panduan proyek akhir"

git push origin main
```

6. Verifikasi:

```bash
git status
git log --oneline -5
git remote -v
```

Jika `git commit` menjawab *nothing to commit*, berarti tidak ada perubahan dalam kelompok file yang dipilih, bukan berarti error. Jika `git push` ditolak, periksa perubahan lokal dan remote terlebih dahulu, jangan langsung force-push.

Repository yang telah digunakan sebelumnya (jika sudah dibuat):
`https://github.com/irenihdinazulfa/pertemuan-14-perancangan-proyek-2225250019`

**Jika dosen justru mewajibkan repo P15 terpisah**, buat repository baru dan `git init` pada folder terpisah. Jangan menjalankan `git init` di folder P14 yang sudah mempunyai sejarah commit.
