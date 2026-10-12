# No. 13 — Round-robin: C(n,2) menghitung pasangan yang bertemu

**Soal (W2-No.5).** Dalam sebuah kompetisi sepak bola terdapat 20 tim yang terbagi menjadi 5 grup. Jika dalam setiap grup banyaknya tim sama, dan setiap tim hanya bertemu sekali. Maka banyaknya pertandingan di fase grup ada … pertandingan.

A. 18 B. 24 **C. 30** D. 36 E. 42

*Sumber: 20 Soal TO Neutron 2026/2027*

---

## Dasarnya

"Setiap tim bertemu sekali" artinya setiap **pasangan** tim menghasilkan tepat satu pertandingan — urutan tidak penting (A lawan B sama dengan B lawan A). Ini definisi **kombinasi**:

**C(n,2) = n(n−1)/2** — banyak pasangan dari n tim.

Bedakan dengan permutasi: kalau A-lawan-B dihitung berbeda dari B-lawan-A (misalnya kandang-tandang), baru pakai n(n−1). Round-robin satu pertemuan = kombinasi, titik.

## Aplikasinya

Langkah 1 — tim per grup: 20 tim / 5 grup = **4 tim** per grup.
Langkah 2 — pertandingan per grup: C(4,2) = 4×3/2 = **6**.
Langkah 3 — total 5 grup: 5 × 6 = **30 pertandingan**.

**Cek kewarasan:** tiap tim main 3 kali (lawan 3 tim lain di grupnya) — 20 tim × 3 / 2 (tiap pertandingan melibatkan 2 tim) = 30. Dua jalan, satu jawaban.

**Kunci: C** — 30 pertandingan.
