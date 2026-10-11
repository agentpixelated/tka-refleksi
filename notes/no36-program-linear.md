# Refleksi No.36 — Program Linear: Keuntungan Terbaik di Sudut

**Soal (W1-No.9, Matwa, MOTS):**

Sebuah perusahaan konveksi memproduksi dua tipe jaket: Tipe Standar dan Tipe Premium. Setiap jaket Standar memerlukan 2 meter kain parasut dan 1 meter kain polar. Setiap jaket Premium memerlukan 1 meter kain parasut dan 3 meter kain polar. Persediaan harian kain parasut maksimal 48 meter dan kain polar maksimal 64 meter. Keuntungan jaket Standar Rp60.000,00/buah dan jaket Premium Rp80.000,00/buah. Keuntungan maksimum yang dapat diperoleh dalam sehari adalah …

- A. Rp1.800.000,00
- B. Rp2.160.000,00
- C. Rp2.240.000,00
- D. Rp2.400.000,00
- E. Rp2.560.000,00

*(Sumber: Try Out TKA 001 (Drive))*

## Dasarnya — Batas-batas membentuk arena, juara duduk di sudut

Program linear itu soal *optimasi dengan keterbatasan*: kamu mau keuntungan sebesar-besarnya, tapi bahan bakunya terbatas. Langkah berpikirnya selalu tiga:

1. **Namai** yang tidak diketahui (misal $x$ = jumlah Standar, $y$ = jumlah Premium).
2. **Tuliskan batasan** (kendala) sebagai pertidaksamaan — setiap bahan baku memberi satu batasan. Jangan lupa $x \ge 0$, $y \ge 0$ (tidak mungkin produksi jaket minus tiga).
3. **Tuliskan fungsi tujuan** — yang mau dimaksimumkan.

Batasan-batasan itu, kalau digambar, membentuk sebuah daerah (poligon) yang disebut *daerah layak*: semua kombinasi $(x,y)$ yang boleh diproduksi. Sekarang fakta ajaibnya: **fungsi tujuan yang linear selalu mencapai nilai terbaiknya di salah satu titik sudut daerah layak** — tidak pernah di tengah-tengah. Jadi kerja kamu bukan memeriksa semua titik (tak terhingga!), melainkan: cari semua titik sudut, hitung nilai fungsi tujuan di masing-masing, ambil yang terbesar. Itulah seluruh "kalkulus" program linear.

Titik sudut biasanya berupa perpotongan sumbu (buat $x=0$ atau $y=0$) dan perpotongan dua garis batas — yang terakhir ini dicari dengan menyelesaikan sistem dua persamaan.

## Aplikasinya

**Langkah 1 — Modelnya.** Misal $x$ = jaket Standar, $y$ = jaket Premium.

Kendala kain parasut: $2x + y \le 48$
Kendala kain polar: $x + 3y \le 64$
$x \ge 0,\ y \ge 0$

Fungsi tujuan (keuntungan, dalam ribu rupiah biar angkanya ramah): $Z = 60x + 80y$.

**Langkah 2 — Cari titik-titik sudut.**

- $(0, 0)$ — tidak produksi apa-apa.
- Potong sumbu-$x$ ($y = 0$): dari $2x \le 48$ → $(24, 0)$.
- Potong sumbu-$y$ ($x = 0$): dari $3y \le 64$ → $(0, \frac{64}{3})$.
- Perpotongan dua garis batas: selesaikan
  $$\begin{cases} 2x + y = 48 \\ x + 3y = 64 \end{cases}$$
  Dari persamaan pertama $y = 48 - 2x$, masukkan ke yang kedua:
  $$x + 3(48 - 2x) = 64 \;\Rightarrow\; x + 144 - 6x = 64 \;\Rightarrow\; -5x = -80 \;\Rightarrow\; x = 16$$
  lalu $y = 48 - 32 = 16$. Jadi titiknya $(16, 16)$.

**Langkah 3 — Uji fungsi tujuan di setiap sudut** (dalam ribu rupiah):

- $(0,0)$: $Z = 0$
- $(24,0)$: $Z = 60 \times 24 = 1440$
- $(0, \frac{64}{3})$: $Z = 80 \times \frac{64}{3} = \frac{5120}{3} \approx 1706{,}67$
- $(16,16)$: $Z = 60 \times 16 + 80 \times 16 = 960 + 1280 = 2240$

Terbesar: $2240$ ribu rupiah = **Rp2.240.000,00**, dicapai dengan memproduksi 16 jaket Standar dan 16 jaket Premium.

**Jebakan yang dihindari:** hanya menguji titik-titik di sumbu (lupa titik potong dua garis — padahal di situlah juaranya), atau tertukar menulis kendala ($2x + y$ untuk parasut, bukan polar — baca tabel kebutuhan bahan per tipe dengan teliti).

**Kunci: C**
