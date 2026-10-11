# Refleksi No.25 — Peluang dari Tabel Kontingensi

**Soal (W6-No.15, Matwa, LOTS):**

Pada acara pertemuan orang tua siswa hadir 120 orang, terdiri atas 80 wanita. Di antara pria yang hadir terdapat 15 orang berambut keriting, dan total orang tua yang berambut keriting pada acara itu ada 50 orang. Jika dipilih satu orang secara acak untuk memberi sambutan, peluang terpilihnya wanita yang tidak berambut keriting adalah …

- A. $\dfrac{9}{24}$
- B. $\dfrac{5}{24}$
- C. $\dfrac{3}{24}$
- D. $\dfrac{3}{48}$
- E. $\dfrac{7}{24}$

*(Sumber: TO 1 Inten Part 12 — youtu.be/2IVPGdowsfQ)*

## Dasarnya — Tabel dua arah: kotak-kotak yang saling menagih

Kalau data punya dua kategori sekaligus (di sini: jenis kelamin × keriting/tidak), jangan dihafal satu per satu — **gambar tabelnya**. Inilah yang disebut tabel kontingensi (dua arah). Baris untuk kategori pertama, kolom untuk kategori kedua, dan jumlah total baris serta kolom *harus cocok* dengan total keseluruhan. Tabel ini seperti rekening: yang kosong bisa ditemukan dengan pengurangan dari yang sudah diketahui.

Peluang "A *dan* B" berarti peluang irisan: orang yang **sekaligus** memenuhi kedua syarat — dalam tabel, itu tepat satu kotak. Jadi soal semacam ini selalu dua langkah: (1) lengkapi tabelnya, (2) ambil kotak yang diminta, bagi dengan total.

$$P(\text{wanita dan tidak keriting}) = \frac{\text{isi kotak itu}}{\text{total orang}}$$

## Aplikasinya

**Langkah 1 — Susun yang diketahui.**

- Total orang: 120.
- Wanita: 80 → maka pria = $120 - 80 = 40$.
- Pria keriting: 15.
- Total orang keriting: 50 → maka wanita keriting = $50 - 15 = 35$.

**Langkah 2 — Cari kotak yang diminta.** Kita mau *wanita yang tidak keriting*:

$$\text{Wanita tidak keriting} = \text{semua wanita} - \text{wanita keriting} = 80 - 35 = 45$$

Kalau mau ditulis jadi tabel penuh (biar puas):

| | Keriting | Tidak keriting | Total |
|---|---|---|---|
| Pria | 15 | 25 | 40 |
| Wanita | 35 | **45** | 80 |
| Total | 50 | 70 | 120 |

Periksa: $45 + 25 + 35 + 15 = 120$. Cocok. Tabelnya jujur.

**Langkah 3 — Peluangnya.**

$$P = \frac{45}{120} = \frac{3}{8} = \frac{9}{24}$$

**Jebakan yang dihindari:** langsung mengambil $\frac{15}{120}$ (itu peluang *pria* keriting — baca lagi yang diminta!), atau menghitung wanita keriting $\frac{35}{120}$ karena lupa kata "tidak".

**Kunci: A**
