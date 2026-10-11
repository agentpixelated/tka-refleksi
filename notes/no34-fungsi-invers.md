# Refleksi No.34 — Fungsi Invers: "Membatalkan" Fungsi

**Soal (W1-No.6, Matwa, MOTS):**

Jika $f(x) = \dfrac{4x-1}{2x+3}$ untuk $x \neq -\tfrac32$, dan fungsi $g(x) = f^{-1}(2x-1)$, maka nilai dari $g(1)$ adalah …

- A. $-2$
- B. $-1$
- C. $1$
- D. $2$
- E. $3$

*(Sumber: Try Out TKA 001 (Drive))*

## Dasarnya — Invers itu tombol "undo"

Simbol $f^{-1}$ sering bikin orang panik, padahal artinya sederhana: **fungsi kebalikan, alias tombol *undo***. Kalau $f$ mengubah $x$ menjadi $y$, maka $f^{-1}$ mengubah $y$ kembali menjadi $x$.

Aturan emasnya, satu kalimat:

$$f^{-1}(y) = x \quad \text{tepat ketika} \quad f(x) = y$$

Artinya: "nilai invers dari $y$ adalah $x$" itu sama persis artinya dengan "$f$ mengirim $x$ ke $y$". Dua cara mengatakan hal yang sama.

Seringkali kamu *tidak perlu* mencari rumus lengkap $f^{-1}(x)$ — cukup pakai aturan emas itu. Misal: "berapa $f^{-1}(5)$?" Artinya: "angka berapa yang dikirim $f$ ke 5?" Lalu kamu selesaikan $f(t) = 5$. Selesai. Ini jauh lebih cepat daripada menurunkan rumus inversnya dulu, apalagi kalau fungsi aslinya ribet seperti pecahan di atas.

(Catatan pinggir: kenapa soalnya menulis $x \neq -\frac32$? Karena penyebut $2x+3$ tidak boleh nol — fungsi aslinya memang tidak terdefinisi di situ. Bukan hiasan, tapi pengingat.)

## Aplikasinya

**Langkah 1 — Sederhanakan soalnya.** Yang ditanya $g(1)$:

$$g(1) = f^{-1}(2 \cdot 1 - 1) = f^{-1}(1)$$

Jadi pertanyaan sebenarnya: "$f$ mengirim angka berapa ke 1?"

**Langkah 2 — Pakai aturan emas.** Katakan jawabannya $t$. Maka:

$$f^{-1}(1) = t \quad \Longleftrightarrow \quad f(t) = 1$$

**Langkah 3 — Selesaikan persamaannya.**

$$\frac{4t-1}{2t+3} = 1$$

Kalikan silang (penyebut tidak nol, aman):

$$4t - 1 = 2t + 3$$
$$2t = 4$$
$$t = 2$$

Cek cepat: $f(2) = \frac{8-1}{4+3} = \frac{7}{7} = 1$. Betul — $f$ memang mengirim 2 ke 1, jadi inversnya mengirim 1 kembali ke 2.

$$g(1) = 2$$

**Jebakan yang dihindari:** membuang waktu mencari rumus umum $f^{-1}(x)$ dengan pertukaran $x \leftrightarrow y$ (bisa, tapi bertele-tele untuk soal ini), atau salah baca dan mengira $f^{-1}(2x-1)$ berarti $\frac{1}{f(2x-1)}$ — invers fungsi bukan kebalikan pangkat satu!

**Kunci: D**
