# No. 43 — Rotasi 90°: geser ke pusat, putar, geser kembali

**Soal (L1-No.11).** Titik (2a, −a) diputar 90° berlawanan arah jarum jam dengan pusat rotasi (1, 1) menghasilkan titik (2 + a, −2) maka nilai a yang memenuhi adalah …

**A. −1** B. −2 C. 0 D. 1 E. 3

*Sumber: Try Out TKA 001 2026/2027*

---

## Dasarnya

Rotasi 90° **berlawanan jarum jam (CCW)** terhadap titik asal O(0,0) punya rumus satu baris:

**(x, y) → (−y, x)**

Kalau pusatnya bukan di origin melainkan di (h, k), pakai pola tiga langkah — **geser, putar, geser kembali**:

1. **Geser** ke origin: (x − h, y − k)
2. **Putar**: (−(y − k), (x − h))
3. **Geser kembali**: (h − (y − k), k + (x − h))

Hafalkan bentuk akhirnya: **(x, y) → (h − (y − k), k + (x − h))**. Kesalahan klasik: lupa menggeser kembali, atau memakai rumus searah jarum jam (x, y) → (y, −x).

## Aplikasinya

Titik (2a, −a), pusat (1, 1):

x' = 1 − (−a − 1) = 1 + a + 1 = **2 + a** ✓ (cocok dengan hasil yang diberikan)
y' = 1 + (2a − 1) = **2a**

Diketahui bayangannya (2 + a, −2), jadi:

2a = −2 → **a = −1**

**Cek kewarasan:** substitusi a = −1: titik awal (2·(−1), −(−1)) = (−2, 1). Putar 90° CCW terhadap (1,1): geser → (−3, 0); putar → (0, −3); geser kembali → (1, −2) = (2 + (−1), −2) ✓. Konsisten.

**Kunci: A** — a = −1.
