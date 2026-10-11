# Refleksi No.44 — Teori Bilangan: Sisa Pembagian (Aritmetika Modular)

**Soal (W1-No.3, Matwa, HOTS):**

Suatu bilangan bulat positif $N$ jika dibagi 3 bersisa 2, jika dibagi 5 bersisa 3, dan jika dibagi 7 bersisa 2. Nilai terkecil dari $N$ yang bernilai lebih dari 100 adalah …

- A. $128$
- B. $137$
- C. $158$
- D. $173$
- E. $233$

*(Sumber: Try Out TKA 001 (Drive))*

## Dasarnya — Sisa itu bukan sampah, sisa itu petunjuk

Aritmetika modular terdengar angker, padahal ia cuma bahasa rapi untuk "bersisa berapa kalau dibagi". Tulisan $N \equiv 2 \pmod{3}$ dibaca "$N$ kongruen 2 modulo 3", artinya persis: **$N$ dibagi 3 bersisa 2**. Simbol $\equiv$ di sini bukan "=" biasa — ia bilang "sama sisanya". Jadi $N \equiv 2 \pmod{3}$ berarti $N$ bisa jadi $2, 5, 8, 11, 14, \dots$ — semua bilangan yang kalau dibagi 3 bersisa 2.

Teknik paling jujur menyelesaikan sistem sisa-sisa seperti ini: **gabungkan dua sisa jadi satu, lalu cocokkan dengan sisa ketiga** (ini versi sederhananya Teorema Sisa Cina).

Perhatikan: dua syarat pertama, $N \equiv 2 \pmod{3}$ dan $N \equiv 2 \pmod{7}$, meminta sisa yang **sama** (sama-sama 2). Kalau dua pembagi tidak punya faktor persekutuan (3 dan 7 relatif prima), dan sisanya sama, maka $N$ bersisa 2 juga kalau dibagi *hasil kali* keduanya: $N \equiv 2 \pmod{21}$. Masuk akal: bilangan yang "2 lebihnya dari kelipatan 3" sekaligus "2 lebihnya dari kelipatan 7" pasti "2 lebihnya dari kelipatan 21".

Lalu tulis $N = 21k + 2$ dan paksa agar memenuhi sisa terakhir — tinggal mencoba nilai $k$ yang kecil. Itu saja seluruh strateginya.

## Aplikasinya

**Langkah 1 — Gabungkan sisa mod 3 dan mod 7.**

$$N \equiv 2 \pmod{3}, \quad N \equiv 2 \pmod{7} \;\Rightarrow\; N \equiv 2 \pmod{21}$$

Jadi $N = 21k + 2$ untuk suatu bilangan bulat $k \ge 0$.

**Langkah 2 — Paksa sisa mod 5.** Syaratnya $N \equiv 3 \pmod{5}$:

$$21k + 2 \equiv 3 \pmod{5}$$

Karena $21 \equiv 1 \pmod{5}$ (21 dibagi 5 bersisa 1), ini menyederhanakan jadi:

$$k + 2 \equiv 3 \pmod{5} \;\Rightarrow\; k \equiv 1 \pmod{5}$$

Jadi $k = 1, 6, 11, 16, \dots$

**Langkah 3 — Bangkitkan calon $N$ dan ambil yang terkecil di atas 100.**

- $k = 1 \Rightarrow N = 21 + 2 = 23$
- $k = 6 \Rightarrow N = 126 + 2 = 128$ ← terkecil yang lebih dari 100 ✓
- $k = 11 \Rightarrow N = 231 + 2 = 233$

**Langkah 4 — Verifikasi** (jangan pernah lewatkan ini untuk soal HOTS): $128 \div 3 = 42$ sisa **2** ✓; $128 \div 5 = 25$ sisa **3** ✓; $128 \div 7 = 18$ sisa **2** ✓.

**Catatan jujur:** opsi D ($173$) memang menggoda — ia benar untuk sisa mod 3 dan mod 5, tapi $173 \div 7 = 24$ sisa **5**, bukan 2. Ia gagal di syarat ketiga. Selalu cek semua syarat.

**Kunci: A**
