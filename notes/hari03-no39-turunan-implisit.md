# No. 39 — Turunan fungsi implisit: turunkan, lalu substitusi titiknya

**Soal (L1-No.14).** f dan g memenuhi f(x+1)·g(x) = (x−3)/(1+2x). Jika g(0) = 1, maka f′(1) − 3g′(0) = …

A. 5 B. 6 C. 7 D. 8 E. 9

*Sumber: Try Out TKA 001*

---

## Dasarnya

Kalau persamaan memuat **perkalian dua fungsi**, turunannya pakai **aturan perkalian**: (uv)′ = u′v + uv′. Di sini u = f(x+1) — jangan lupa **aturan rantai**: turunan f(x+1) terhadap x adalah f′(x+1)·1.

Setelah diturunkan, **substitusi x yang ditanya** (di sini x = 0, karena yang muncul f′(1) dan g′(0)). Nilai f(1) dicari dulu dari persamaan awal di x = 0.

## Aplikasinya

Turunkan kedua ruas terhadap x:
f′(x+1)·g(x) + f(x+1)·g′(x) = [(1)(1+2x) − (x−3)(2)]/(1+2x)²

Substitusi x = 0:
f′(1)·g(0) + f(1)·g′(0) = [(1+0) − (−3)(2)]/1 = 7.

g(0) = 1. Cari f(1): dari persamaan awal di x = 0: f(1)·1 = (0−3)/(1+0) = −3 → **f(1) = −3**.

Maka: f′(1)·1 + (−3)·g′(0) = 7 → **f′(1) − 3g′(0) = 7**.

**Kunci: C** — 7.
