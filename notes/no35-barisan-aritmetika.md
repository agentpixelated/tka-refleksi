# Refleksi No.35 — Barisan Aritmetika: Suku Tengah adalah Rata-rata

**Soal (W1-No.7, Matwa, MOTS):**

Suatu barisan aritmetika dengan suku-suku positif memiliki jumlah 5 suku pertama bernilai 35. Jika hasil kali suku pertama dan suku kelima adalah 33, maka beda ($b$) barisan tersebut adalah …

- A. $1$
- B. $2$
- C. $3$
- D. $4$
- E. $5$

*(Sumber: Try Out TKA 001 (Drive))*

## Dasarnya — Barisan aritmetika itu tangga yang sama lebarnya

Barisan aritmetika artinya: setiap langkah naik (atau turun) **sama besar**. Suku pertama kita sebut $a$, besar langkahnya kita sebut beda $b$. Maka:

$$U_1 = a,\quad U_2 = a+b,\quad U_3 = a+2b,\quad U_4 = a+3b,\quad U_5 = a+4b,\ \dots$$

dan rumus umumnya $U_n = a + (n-1)b$.

Sekarang ada trik manis yang akan menghemat separuh kerja kamu. Untuk jumlah suku *ganjil* — misal 5 suku — suku yang di tengah ($U_3$) itu persis **rata-rata dari semuanya**. Bayangkan lima anak berderet dengan tinggi berjenjang sama: yang tengah tingginya pasti rata-rata kelimanya. Jadi:

$$U_3 = \frac{S_5}{5}$$

Kenapa bisa? Karena $S_5 = U_1+U_2+U_3+U_4+U_5$, dan suku-sukunya berpasangan simetris di sekitar $U_3$: $U_1 + U_5 = 2U_3$, $U_2 + U_4 = 2U_3$. Jumlahkan semua: $S_5 = 5U_3$. Jadi $U_3 = S_5/5$. Rumus umum $S_n = \frac{n}{2}(2a+(n-1)b)$ tidak perlu dihafal mati-matian kalau kamu paham logika ini — tapi boleh dipakai juga, sama hasilnya.

Satu lagi: $U_1 \times U_5$ dalam suku-suku $U_3$: karena $U_1 = U_3 - 2b$ dan $U_5 = U_3 + 2b$,

$$U_1 \cdot U_5 = (U_3 - 2b)(U_3 + 2b) = U_3^2 - (2b)^2 = U_3^2 - 4b^2$$

(selisin kuadrat — pola $(p-q)(p+q) = p^2 - q^2$ yang patut kamu cintai).

## Aplikasinya

**Langkah 1 — Cari suku tengah.** Diketahui $S_5 = 35$:

$$U_3 = \frac{35}{5} = 7$$

Satu langkah langsung, tanpa rumus panjang.

**Langkah 2 — Gunakan hasil kali.** $U_1 \cdot U_5 = 33$:

$$(7 - 2b)(7 + 2b) = 33$$
$$49 - 4b^2 = 33$$
$$4b^2 = 16$$
$$b^2 = 4 \quad \Rightarrow \quad b = 2 \text{ (barisan naik)}$$

Kita ambil $b = 2$ karena soal menyiratkan barisan yang suku-sukunya positif dan lazimnya naik; ceknya: $a = U_3 - 2b = 7 - 4 = 3$, suku-sukunya $3, 5, 7, 9, 11$ — semua positif, jumlah $35$, hasil kali ujung $3 \times 11 = 33$. Semua syarat terpenuhi.

**Jebakan yang dihindari:** langsung memakai rumus $S_n$ dengan dua variabel $a$ dan $b$ sekaligus (bisa, tapi kamu mengerjakan dua persamaan yang sebenarnya tidak perlu), atau berhenti di $b^2 = 4$ dan bingung memilih tanda — suku positif memastikan barisan naik, jadi $b = 2$.

**Kunci: B**
