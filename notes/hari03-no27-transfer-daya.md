# No. 27 — Transfer daya maksimum: samakan beban dengan hambatan dalam

**Soal (F1-No.23).** Sumber DC ℰ = 20 V, hambatan dalam r = 4 Ω, menyuplai tiga resistor R1 = 2 Ω, R2 = 3 Ω, R3 = 6 Ω. Bagaimana merangkai ketiganya agar terjadi transfer daya maksimum?

A. ketiganya paralel B. ketiganya seri C. R2 seri R3, paralel ke R1 D. R1 paralel R2, seri ke R3 E. R2 paralel R3, seri ke R1

*Sumber: Tryout TKA-1 Prosus Inten × Pusmendik 2026/2027*

---

## Dasarnya

**Teorema transfer daya maksimum:** daya yang diserap beban maksimum ketika **hambatan beban = hambatan dalam sumber** (RL = r). Bukan "sekecil mungkin", bukan "sebesar mungkin" — tapi **sama persis**.

Daya pada beban: P = I²·RL dengan I = ℰ/(r + RL). Kalau RL terlalu kecil, arus besar tapi tegangan di beban kecil; kalau RL terlalu besar, tegangan besar tapi arus kecil. Titik imbangnya di RL = r.

Jadi tugasnya: rangkai R1, R2, R3 supaya hambatan totalnya = 4 Ω.

## Aplikasinya

r = 4 Ω, target RL = 4 Ω. Uji tiap opsi:

- A (paralel): 1/(1/2+1/3+1/6) = 1/1 = 1 Ω ✗
- B (seri): 2+3+6 = 11 Ω ✗
- C: R2+R3 = 9, paralel R1: (9·2)/(9+2) = 18/11 ≈ 1,6 Ω ✗
- D: R1∥R2 = (2·3)/5 = 6/5, seri R3: 6/5+6 = 7,2 Ω ✗
- E: R2∥R3 = (3·6)/9 = 2 Ω, seri R1: 2+2 = **4 Ω** ✓

**Kunci: E** — R2 paralel R3, lalu seri ke R1.
