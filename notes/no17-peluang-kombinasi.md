# Refleksi No.17 — Peluang: Kombinasi dan "Setidaknya"

**Soal (W1-No.18, Matwa, LOTS):**

Sebuah tim pengembang web beranggotakan 5 programmer laki-laki dan 4 programmer perempuan. Dari kelompok itu akan dipilih 3 orang secara acak untuk menghadiri sebuah seminar internasional. Peluang bahwa utusan yang terpilih memuat setidaknya 2 programmer perempuan adalah …

- A. $\dfrac{17}{42}$
- B. $\dfrac{19}{42}$
- C. $\dfrac{23}{42}$
- D. $\dfrac{25}{42}$
- E. $\dfrac{29}{42}$

*(Sumber: Try Out TKA 001 (Drive))*

## Dasarnya — Kombinasi: menghitung tanpa peduli urutan

Lupakan dulu rumusnya. Bayangkan kamu menunjuk 3 orang dari 9 untuk ke seminar. Apakah penting siapa yang ditunjuk *pertama*? Tidak. "Ani, Budi, Cici" dan "Cici, Ani, Budi" itu utusan yang **sama**. Jadi urutan tidak penting — dan itulah inti kombinasi.

Simbolnya $C(n,k)$, dibaca "kombinasi n pilih k": banyaknya cara memilih $k$ orang dari $n$ orang tanpa memedulikan urutan. Rumusnya:

$$C(n,k) = \frac{n!}{k!(n-k)!}$$

Angka $n!$ itu "semua susunan jika urutan penting", dan kita *bagi* dengan $k!(n-k)!$ untuk menghapus urutan yang kita tidak pedulikan. Jangan hafalkan mekaniknya dulu — yang penting kamu paham: **$C(n,k)$ menjawab "ada berapa kelompok yang mungkin".**

Contoh kecil biar terasa: $C(4,2)$. Dari 4 perempuan, pilih 2. Susunan berurutan ada $4 \times 3 = 12$, tapi karena "A lalu B" sama dengan "B lalu A", kita bagi 2 → hasilnya 6. Rumus: $\frac{4!}{2!2!} = \frac{24}{4} = 6$. Masuk akal.

Lalu, kata kunci yang satu ini sering bikin orang terjungkal: **"setidaknya 2"** (*at least 2*). "Setidaknya 2 perempuan" itu artinya: bisa 2 perempuan, **atau** bisa juga 3 perempuan. Ia bukan satu kasus — ia adalah dua kasus yang harus dihitung masing-masing lalu dijumlahkan. Sama seperti "setidaknya 2 hari hujan minggu ini" = "2 hari hujan ATAU 3 hari hujan ATAU … 7 hari hujan".

Rumus peluangnya biasa saja:

$$P = \frac{\text{kasus yang kita mau}}{\text{semua kasus yang mungkin}}$$

Kuncinya cuma: hati-hati menentukan *ruang sampel* (penyebut) dan *kasus favorit* (pembilang) memakai kombinasi yang benar.

## Aplikasinya

**Langkah 1 — Semua kasus yang mungkin.** Dari 9 orang pilih 3, urutan tak penting:

$$C(9,3) = \frac{9!}{3!6!} = \frac{9 \times 8 \times 7}{3 \times 2 \times 1} = \frac{504}{6} = 84$$

Ada 84 utusan yang mungkin.

**Langkah 2 — Kasus favorit: "setidaknya 2 perempuan" = (2P 1L) atau (3P).**

Kasus A: tepat 2 perempuan dan 1 laki-laki. Pilih 2 dari 4 perempuan, pilih 1 dari 5 laki-laki. Karena pemilihan perempuan dan laki-laki terjadi bersamaan, kita kalikan:

$$C(4,2) \times C(5,1) = 6 \times 5 = 30$$

Kasus B: tepat 3 perempuan. Pilih 3 dari 4 perempuan:

$$C(4,3) = \frac{4!}{3!1!} = 4$$

Total kasus favorit = $30 + 4 = 34$.

**Langkah 3 — Peluangnya.**

$$P = \frac{34}{84} = \frac{17}{42}$$

**Jebakan yang dihindari:** menggabung 2P dan 3P dalam satu hitungan $C(4,2)C(5,1)$ saja (lupa 3P), atau memakai permutasi sehingga penyebutnya jadi $9 \times 8 \times 7 = 504$ tanpa membagi pembilangnya dengan cara yang sama.

**Kunci: A**
