# No. 22 — Matriks invers dari persamaan: kali invers dari kiri

**Soal (L5-No.4).** Jika [[2,4],[0,1]] · A = [[2,3],[0,1]], maka jumlah semua unsur matriks A⁻¹ adalah …

A. 3/2 B. 5/2 C. 3 D. 11/2 E. 15/2

*Sumber: 30 Soal TO Matlan Inten*

---

## Dasarnya

Persamaan matriks **MA = N** diselesaikan dengan mengalikan invers M dari **kiri**: A = M⁻¹N. (Perkalian matriks tak komutatif — kiri vs kanan fatal bedanya.)

Invers matriks 2×2 [[a,b],[c,d]]: **(1/(ad−bc)) · [[d,−b],[−c,a]]** — tukar a↔d, negasikan b dan c, **bagi determinan**. Yang terakhir ini paling sering kelupaan.

Di sini kita butuh A⁻¹, bukan A. Dari MA = N → A = M⁻¹N, maka A⁻¹ = (M⁻¹N)⁻¹ = **N⁻¹M**.

## Aplikasinya

M = [[2,4],[0,1]], N = [[2,3],[0,1]].

det(N) = 2·1 − 3·0 = 2.
N⁻¹ = (1/2)·[[1,−3],[0,2]] = [[1/2, −3/2],[0, 1]].

A⁻¹ = N⁻¹M = [[1/2,−3/2],[0,1]] · [[2,4],[0,1]]
= [[1/2·2, 1/2·4 − 3/2·1],[0, 1]]
= [[1, 1/2],[0, 1]].

Jumlah semua unsur = 1 + 1/2 + 0 + 1 = **5/2**.

**Kunci: B** — 5/2.
