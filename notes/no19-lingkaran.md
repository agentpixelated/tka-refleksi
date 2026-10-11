# Catatan Refleksi — L1 No. 7: Persamaan Lingkaran

> L1-No.7 (Matlan, LOTS)
> \src{Try Out TKA 001 (Drive)}

**Soal.** Diketahui sebuah lingkaran berpusat di titik $(4,-1)$ dan menyinggung sumbu-$x$. Persamaan lingkaran tersebut adalah …

- A. $x^2+y^2-8x+2y+16=0$
- B. $x^2+y^2+8x-2y+16=0$
- C. $x^2+y^2-8x+2y+17=0$
- D. $x^2+y^2-8x-2y+17=0$
- E. $x^2+y^2-8x+15=0$

---

## Dasarnya

Bayangkan lingkaran itu apa adanya: sebuah garis melengkung di mana *setiap* titiknya berdiri pada jarak yang sama dari satu titik tengah. Titik tengah itu namanya **pusat**. Jarak yang sama itu namanya **jari-jari**.

Orang matematika, yang lebih sopan dari kita, menulis ini sebagai:

$$(x-a)^2+(y-b)^2=r^2$$

Jangan panik melihat huruf-hurufnya. Beginilah terjemahannya ke bahasa manusia:

- $(a,b)$ adalah pusat lingkaran — koordinatnya.
- $r$ adalah jari-jari.
- $(x,y)$ adalah *setiap* titik yang duduk di keliling lingkaran. Persamaan ini sekadar cara mewah untuk berkata: "jarak dari $(x,y)$ ke pusat $(a,b)$ sama dengan $r$" — tidak lebih dari rumus jarak Pythagoras yang menyamar.

Jadi seluruh isi soal lingkaran selalu satu pertanyaan: **berapa $a$, berapa $b$, berapa $r$?** Setelah ketiganya ketahuan, pekerjaannya selesai — tinggal memasukkan angka.

Sekarang, kata yang satu ini: **menyinggung**. "Menyinggung sumbu-$x$" artinya lingkaran itu *menyentuh* sumbu-$x$ — tepat di satu titik, seperti bola yang diletakkan di atas lantai. Dan inilah akal sehatnya: kalau lingkaran menyentuh sumbu-$x$, maka jarak dari pusatnya ke sumbu-$x$ *pasti* sama dengan jari-jarinya. Karena jari-jari adalah garis dari pusat ke titik singgung, dan titik singgungnya adalah titik terdekat pusat ke sumbu itu.

Jarak pusat ke sumbu-$x$ itu tidak perlu dihitung dengan rumus sakti — cukup lihat ordinat pusatnya. Sumbu-$x$ adalah garis $y=0$. Pusatnya $(4,-1)$: koordinat $y$-nya $-1$, artinya pusatnya berdiri tepat 1 satuan di bawah sumbu-$x$. Maka jari-jarinya: $r = |-1| = 1$.

Itulah seluruh triknya. Pusatnya diberi, jari-jarinya bisa dibaca dari kata "menyinggung".

Satu hal terakhir yang sering menjebak: soal-soal sering menyajikan jawabannya dalam bentuk "umum" (yang sudah dikuadrat-kuadratkan dan diratakan), bukan bentuk $(x-a)^2+(y-b)^2=r^2$. Jadi biasakan menguraikan:

$$(x-4)^2+(y+1)^2=1 \;\to\; x^2-8x+16+y^2+2y+1=1 \;\to\; x^2+y^2-8x+2y+16=0.$$

Hati-hati pada tanda: $(x-4)^2$ menjadi $x^2-8x+16$, dan $(y-(-1))^2=(y+1)^2$ menjadi $y^2+2y+1$. Inilah tempat paling manusiawi untuk salah — dan soal-soal tahu itu, makanya opsi B dan D dipasang sebagai perangkap tanda.

---

## Aplikasinya

1. **Identifikasi pusat.** Soal bilang pusatnya $(4,-1)$, jadi $a=4$, $b=-1$.
2. **Tentukan jari-jari.** "Menyinggung sumbu-$x$" → jari-jari = jarak pusat ke sumbu-$x$ = $|{-1}| = 1$. Jadi $r=1$.
3. **Tulis bentuk baku.** $(x-4)^2+(y-(-1))^2=1^2$, yaitu $(x-4)^2+(y+1)^2=1$.
4. **Uraikan ke bentuk umum.** $x^2-8x+16+y^2+2y+1-1=0$, sehingga $x^2+y^2-8x+2y+16=0$.

Cocok dengan opsi A.

**Kunci: A**
