# TKA Refleksi — Hari 01

Reflection framework for Naby's TKA drill, Hari 01 (46 questions, 2026-10-11).
Score: **17/28 (61%)** — 18 unattempted, 11 wrong.

- **18 unattempted** → `notes/`: fundamental concept taught from scratch
  (*catatan dasar*, Thompson's *Calculus Made Easy* voice, Indonesian),
  then applied to the specific question (*aplikasinya*).
- **11 wrong** → `videos/`: short Manim reflection videos (Blackboard
  Framework style — pure black, serif, Indonesian), each starting from
  fundamental laws and addressing the exact error.

Question texts are from `latihan-tka-hari01-46soal-2026-10-11.pdf`
(Tryout TKA-1 Prosus Inten × Pusmendik 2026/2027, TO Asli Pusmendik,
Try Out TKA 001, TO Inten, TO GO). Explanations are original.

## Notes — soal yang tidak diisi (tidak tahu dasarnya)

| No | Kode | Mapel | File | Fundamental |
|----|------|-------|------|-------------|
| 2 | F1-No.2 | Fisika | [no02-menyusul.md](notes/no02-menyusul.md) | GLB vs GLBB; "menyusul" = posisi sama |
| 5 | F1-No.11 | Fisika | [no05-tumbukan.md](notes/no05-tumbukan.md) | Momentum kekal; koefisien restitusi |
| 8 | F1-No.14 | Fisika | [no08-pegas.md](notes/no08-pegas.md) | Energi potensial pegas → kinetik |
| 9 | F1-No.18 | Fisika | [no09-fase-gelombang.md](notes/no09-fase-gelombang.md) | Beda fase vs beda jarak |
| 10 | F1-No.19 | Fisika | [no10-gelombang-berjalan.md](notes/no10-gelombang-berjalan.md) | Persamaan gelombang berjalan |
| 28 | F1-No.6 | Fisika | [no28-tikungan.md](notes/no28-tikungan.md) | Gaya sentripetal; v_maks |
| 29 | F1-No.7 | Fisika | [no29-momentum-sudut.md](notes/no29-momentum-sudut.md) | Momentum sudut kekal |
| 30 | F1-No.8 | Fisika | [no30-impuls.md](notes/no30-impuls.md) | Impuls = Δp |
| 42 | F2-No.7 | Fisika | [no42-archimedes.md](notes/no42-archimedes.md) | Hukum Archimedes |
| 17 | W1-No.18 | Matwa | [no17-peluang-kombinasi.md](notes/no17-peluang-kombinasi.md) | Kombinasi; peluang "paling sedikit" |
| 25 | W6-No.15 | Matwa | [no25-peluang-tabel.md](notes/no25-peluang-tabel.md) | Tabel kontingensi |
| 34 | W1-No.6 | Matwa | [no34-fungsi-invers.md](notes/no34-fungsi-invers.md) | Fungsi invers |
| 35 | W1-No.7 | Matwa | [no35-barisan-aritmetika.md](notes/no35-barisan-aritmetika.md) | Barisan aritmetika |
| 36 | W1-No.9 | Matwa | [no36-program-linear.md](notes/no36-program-linear.md) | Program linear |
| 40 | L1-No.3 | Matlan | [no40-persamaan-garis.md](notes/no40-persamaan-garis.md) | Persamaan garis |
| 44 | W1-No.3 | Matwa | [no44-teori-bilangan.md](notes/no44-teori-bilangan.md) | Kongruensi / sisa pembagian |
| 19 | L1-No.7 | Matlan | [no19-lingkaran.md](notes/no19-lingkaran.md) | Persamaan lingkaran |
| 21 | L1-No.21 | Matlan | [no21-titik-pada-lingkaran.md](notes/no21-titik-pada-lingkaran.md) | Titik pada lingkaran |

## Videos — soal yang salah (refleksi)

| No | Kode | File | Durasi | Poin |
|----|------|------|--------|------|
| 3 | F1-No.3 | [no03-proyektil-46s.mp4](videos/no03-proyektil-46s.mp4) | 46s | t jatuh hanya dari vertikal; horizontal = Hukum I |
| 4 | F1-No.4 | [no04-kecukupan-46s.mp4](videos/no04-kecukupan-46s.mp4) | 46s | Jangan selundupkan konstanta yang tak diberikan |
| 6 | F1-No.12 | [no06-katrol-46s.mp4](videos/no06-katrol-46s.mp4) | 46s | Katrol bermassa "memakan" torsi → T₁≠T₂ |
| 7 | F1-No.13 | [no07-torsi-47s.mp4](videos/no07-torsi-47s.mp4) | 47s | Keseimbangan ditentukan torsi, bukan massa |
| 16 | W1-No.17 | [no16-sin2x-45s.mp4](videos/no16-sin2x-45s.mp4) | 45s | Angka 2 sudah ada di dalam identitas sin 2x |
| 23 | F3-No.3 | [no23-iklim-42s.mp4](videos/no23-iklim-42s.mp4) | 42s | Uji tiap pernyataan: nambah atau ngurangin CO₂? |
| 27 | F1-No.5 | [no27-lift-46s.mp4](videos/no27-lift-46s.mp4) | 46s | "Diperlambat" = percepatan melawan kecepatan |
| 31 | F1-No.9 | [no31-hukum3-46s.mp4](videos/no31-hukum3-46s.mp4) | 46s | Aksi-reaksi bekerja pada benda BERBEDA |
| 33 | W1-No.5 | [no33-domain-48s.mp4](videos/no33-domain-48s.mp4) | 48s | Penyebut ≠ 0 → ujung interval terbuka |
| 37 | W1-No.11 | [no37-sudut-51s.mp4](videos/no37-sudut-51s.mp4) | 51s | Cek dulu: garisnya di dalam bidang? |
| 41 | L1-No.4 | [no41-akarkembar-47s.mp4](videos/no41-akarkembar-47s.mp4) | 47s | ± selalu berarti dua kasus |

Manim sources (`.py`) sit next to each mp4. Built with the
[Blackboard Framework](https://github.com/agentpixelated/blackboard-framework).

## Website integration

The [tka-performance](https://github.com/agentpixelated/tka-performance)
dashboard can surface these per question: each Hari 01 question row links to
its note (`notes/noNN-*.md`, rendered) or its reflection video
(`videos/noNN-*-*s.mp4`, embedded). Suggested data shape per question:

```json
{ "no": 3, "kode": "F1-No.3", "status": "salah",
  "refleksi": { "tipe": "video", "path": "videos/no03-proyektil-46s.mp4" } }
{ "no": 2, "kode": "F1-No.2", "status": "tidak-dikerjakan",
  "refleksi": { "tipe": "catatan", "path": "notes/no02-menyusul.md" } }
```
