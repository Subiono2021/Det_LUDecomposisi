<p align="justify">
Program Python ini mendefinisikan sebuah fungsi bernama <code>lu_determinant</code> yang bertujuan untuk menghitung determinan dari sebuah matriks persegi menggunakan dekomposisi $LU$ (Lower-Upper). Berikut adalah penjelasan mendetail tentang program tersebut:
</p>

**1. Import Library:**
   - `from sympy import Matrix, simplify, init_printing, latex, eye, prod`: Mengimpor fungsi-fungsi yang diperlukan dari library SymPy untuk manipulasi simbolik matriks, penyederhanaan ekspresi, inisialisasi output $\LaTeX$, konversi ekspresi ke $\LaTeX$, pembuatan matriks identitas, dan perhitungan produk elemen-elemen dalam list.
   - `from IPython.display import display, Math`: Mengimpor fungsi `display` dan `Math` dari library IPython.display untuk menampilkan output matematika menggunakan format LaTeX di lingkungan seperti Jupyter Notebook.

**2. Inisialisasi Output $\LaTeX$:**
   - `init_printing(use_latex=True)`: Mengaktifkan penggunaan $\LaTeX$ untuk menampilkan output matematika dari SymPy secara lebih rapi dan mudah dibaca.

**3. Definisi Fungsi `lu_determinant(A)`:**
   - Fungsi ini menerima satu argumen, `A`, yang diasumsikan sebagai objek matriks SymPy.
   - `L, U, perm = A.LUdecomposition()`: Melakukan dekomposisi LU pada matriks `A`. Metode `LUdecomposition()` mengembalikan tiga nilai:
     - `L`: Matriks segitiga bawah (Lower triangular matrix).
     - `U`: Matriks segitiga atas (Upper triangular matrix).
     - `perm`: Daftar pasangan indeks baris yang dipertukarkan selama proses dekomposisi untuk mengatasi masalah pivot nol. **Penting untuk dicatat bahwa format `perm` yang dikembalikan oleh SymPy adalah daftar tuple `(i, j)` yang menunjukkan baris `i` ditukar dengan baris `j`.**
   - `n = A.rows`: Mendapatkan jumlah baris (atau kolom, karena matriks diasumsikan persegi) dari matriks `A`.
   - `P = eye(n)`: Membuat matriks identitas berukuran `n x n`. Matriks ini akan digunakan untuk merepresentasikan matriks permutasi.
   - `k = 0`: Menginisialisasi variabel `k` yang akan menghitung jumlah pertukaran baris.

**4. Membangun Matriks Permutasi (Koreksi):**
   - Bagian ini mengoreksi bagaimana matriks permutasi `P` dibangun berdasarkan informasi dari `perm`.
   - `for swap in perm:`: Iterasi melalui setiap elemen dalam daftar `perm`.
   - `if isinstance(swap, (list, tuple)) and len(swap) == 2:`: Memastikan bahwa elemen `swap` adalah list atau tuple dengan dua elemen (indeks baris yang ditukar).
   - `i, j = swap`: Membongkar tuple `swap` menjadi indeks baris `i` dan `j`.
   - `P.row_swap(i, j)`: Menukar baris `i` dan `j` pada matriks identitas `P`. Setiap pertukaran baris ini sesuai dengan pertukaran yang dilakukan selama dekomposisi LU.
   - `k += 1`: Menambah counter `k` setiap kali terjadi pertukaran baris.

**5. Menghitung Determinan:**
   - `sign = (-1) ** k`: Menghitung tanda determinan berdasarkan jumlah pertukaran baris. Setiap pertukaran baris mengubah tanda determinan.
   - `diag_product = simplify(prod([U[i, i] for i in range(U.rows)]))`: Menghitung produk dari elemen-elemen diagonal matriks segitiga atas `U`. Determinan matriks segitiga (atas atau bawah) adalah hasil perkalian elemen-elemen diagonalnya. Fungsi `simplify` digunakan untuk menyederhanakan hasil perkalian.
   - `det_A = simplify(sign * diag_product)`: Menghitung determinan matriks `A` dengan mengalikan tanda (`sign`) dengan produk elemen diagonal matriks `U`.

**6. Menampilkan Hasil dalam $\LaTeX$:**
   - Serangkaian perintah `display(Math(r"..."))` digunakan untuk menampilkan matriks `A`, matriks permutasi `P`, matriks segitiga bawah `L`, matriks segitiga atas `U`, hasil perkalian `L @ U`, hasil perkalian `P @ A`, jumlah pertukaran baris `k`, dan nilai determinan `det_A` dalam format LaTeX yang mudah dibaca.

**7. Mengembalikan Nilai:**
   - `return det_A, k, P`: Fungsi mengembalikan tiga nilai:
     - `det_A`: Nilai determinan matriks `A`.
     - `k`: Jumlah pertukaran baris yang dilakukan.
     - `P`: Matriks permutasi yang digunakan dalam dekomposisi PA = LU.

**Kesimpulan:**

Program ini mengimplementasikan metode perhitungan determinan suatu matriks persegi menggunakan dekomposisi LU. Inti dari metode ini adalah:

1. **Dekomposisi LU dengan Pivoting:** Melakukan dekomposisi matriks $A$ menjadi matriks segitiga bawah $L$, matriks segitiga atas $U$, dan mencatat permutasi baris yang terjadi dalam bentuk daftar `perm`.
2. **Membangun Matriks Permutasi:** Membuat matriks permutasi $P$ berdasarkan urutan pertukaran baris yang tercatat. Hubungan yang berlaku adalah $PA = LU$.
3. **Menghitung Determinan:** Determinan matriks $A$ dapat dihitung dari determinan matriks $U$ (yang merupakan perkalian elemen-elemen diagonalnya) dan tanda yang ditentukan oleh jumlah pertukaran baris ($(-1)^k$). Karena $\det(PA) = \det(P) \det(A) = \det(LU) = \det(L) \det(U),$ dan $\det(L) = 1$ (karena elemen diagonalnya biasanya 1 dalam dekomposisi $LU$ tanpa normalisasi), maka $\det(A) = \det(U) / \det(P)$. Determinan matriks permutasi $P$ adalah $(-1)^k$, di mana $k$ adalah jumlah pertukaran baris. Oleh karena itu, $\det(A) = (-1)^k \cdot \det(U)$.

Program ini juga menyajikan langkah-langkah dekomposisi dan hasil perhitungan secara visual menggunakan $\LaTeX$, yang sangat berguna untuk pemahaman dan dokumentasi.
