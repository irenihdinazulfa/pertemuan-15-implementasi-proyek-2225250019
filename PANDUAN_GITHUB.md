# Panduan GitHub — Proyek Individu Pertemuan 14

1. Buat repository **kosong** pada akun `irenihdinazulfa` dengan nama `pertemuan-14-perancangan-proyek-2225250019` (jangan menambah README/gitignore otomatis).
2. Buka folder proyek di VS Code dan terminal pada folder utama.
3. Agar ada **riwayat commit bertahap**, lakukan:

```bash
git init
git add .gitignore data/ src/ output/.gitkeep
git commit -m "chore: menyiapkan struktur dan prototipe proyek individu"

git add proposal.md rancangan/
git commit -m "docs: menyusun proposal IPO dan pseudocode proyek"

git add tests/ README.md PANDUAN_GITHUB.md RINGKASAN_PRESENTASI.md
git commit -m "test: merancang test case dan dokumentasi individu"

git branch -M main
git remote add origin https://github.com/irenihdinazulfa/pertemuan-14-perancangan-proyek-2225250019.git
git push -u origin main
```

Catatan: hanya jalankan `git remote add origin` jika belum ada remote `origin`. Bila ada, cek dengan `git remote -v` dan perbaiki bila perlu menggunakan `git remote set-url origin URL`.

Verifikasi:

```bash
git status
git log --oneline -5
git remote -v
```

Bila ada perubahan setelahnya:

```bash
git add .
git commit -m "docs: menyempurnakan rancangan proyek individu"
git push origin main
```

Tidak ada fitur kuis formatif khusus pada bahan ajar Pertemuan 14 yang dilampirkan; tugas utamanya adalah **proposal proyek**.
