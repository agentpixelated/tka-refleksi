# Refleksi No.40 — Persamaan Garis: Kemiringan dulu, Baru Titiknya

**Soal (L1-No.3, Matlan, MOTS):**

Suatu garis $p$ melewati titik $A(7,-3)$ dan $B(-5,9)$. Persamaan garis $p$ dalam bentuk umum $Ax + By = C$ adalah …

- A. $x + y = 4$
- B. $x - y = 4$
- C. $3x - y = 4$
- D. $3x + 4y = 12$
- E. $4x + 3y = 12$

*(Sumber: Try Out TKA 001 (Drive))*

## Dasarnya — Gradien: seberapa curam kamu melangkah

Garis lurus itu makhluk sederhana: ia punya satu sifat tetap di mana-mana, yaitu **kemiringan** (gradien, $m$) — seberapa banyak $y$ berubah setiap kali $x$ bertambah 1. Kalau dari titik $A$ ke titik $B$, $y$ berubah sebesar $\Delta y$ dan $x$ berubah sebesar $\Delta x$, maka:

$$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$$

Urutan pengurangannya bebas, asal *konsisten*: atas dan bawah harus "titik kedua dikurangi titik pertama". Kalau atas $B - A$, bawah pun $B - A$.

Setelah kemiringannya ketahuan, garisnya "terkunci" — tinggal menambatkannya ke salah satu titik dengan bentuk titik-gradien:

$$y - y_1 = m(x - x_1)$$

Artinya: mulai dari titik $(x_1, y_1)$ yang sudah diketahui, setiap melangkah $x$ sejauh $(x - x_1)$, naiklah $y$ sebesar $m$ kali langkah itu. Selesai — itulah persamaan garisnya. Bentuk $Ax + By = C$ hanyalah rapian aljabar dari bentuk ini.

## Aplikasinya

**Langkah 1 — Hitung kemiringan.** $A(7,-3)$, $B(-5,9)$:

$$m = \frac{9 - (-3)}{-5 - 7} = \frac{12}{-12} = -1$$

Garisnya miring turun: setiap $x$ bertambah 1, $y$ berkurang 1.

**Langkah 2 — Tambatkan ke satu titik.** Pakai $A(7,-3)$:

$$y - (-3) = -1 \cdot (x - 7)$$
$$y + 3 = -x + 7$$
$$x + y = 4$$

**Langkah 3 — Cek dengan titik satunya.** Masukkan $B(-5, 9)$: $-5 + 9 = 4$. Cocok! (Cek balik begini murah harganya dan menyelamatkan banyak nilai.)

**Jebakan yang dihindari:** salah tanda saat $\Delta y$ atau $\Delta x$ (titiknya mengandung negatif — hati-hati), atau lupa merapikan ke bentuk $Ax + By = C$ sehingga tidak menemukan opsinya.

**Kunci: A**
