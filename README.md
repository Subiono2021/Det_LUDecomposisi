# LU Determinant Calculator

Modul Python untuk menghitung **determinan matriks persegi** menggunakan metode **LU decomposition dengan pivoting**. Proses perhitungan divisualisasikan secara interaktif menggunakan LaTeX dalam Jupyter Notebook.

## 📌 Fitur

- Menggunakan dekomposisi `LU` dari `SymPy`
- Menghitung:
  - Matriks `L` dan `U`
  - Matriks permutasi `P`
  - Tanda determinan dari jumlah pertukaran baris
  - Produk elemen diagonal `U`
- Menampilkan seluruh proses dalam format matematis menggunakan LaTeX
- Siap digunakan di Jupyter Notebook dan Google Colab

---

## 🔧 Instalasi

Tidak perlu instalasi khusus jika sudah menggunakan Jupyter + SymPy.

Jika belum, kamu bisa install dependensi berikut:

```bash
pip install sympy
```

---

## 🚀 Penggunaan

```python
from sympy import Matrix
from lu_determinant import lu_determinant

A = Matrix([[2, 3, 1],
            [4, 1, -3],
            [6, 18, 5]])

det, k, P = lu_determinant(A)
print("Determinan:", det)
print("Jumlah swap:", k)
```

Output visual (jika di Jupyter) akan mencakup:
- Matriks A
- Matriks permutasi P
- Matriks L dan U
- Verifikasi PA = LU
- Perhitungan determinan dengan rumus:

\[
\det(A) = (-1)^k \cdot \prod u_{i,i}
\]

---

## 📁 Struktur File

```
.
├── lu_determinant.py     # Modul utama
├── example.py            # Contoh pemakaian di luar notebook
├── README.md             # Dokumentasi proyek
```

---

## 🧪 Contoh Hasil di Jupyter Notebook

![Contoh Output](https://via.placeholder.com/800x200.png?text=Output+LaTeX+di+Notebook)

---

## 📎 Lisensi

Proyek ini dapat digunakan secara bebas untuk tujuan edukasi dan riset.

---

## 📌 Catatan

Jika ingin menampilkan modul ini langsung di Google Colab, tambahkan badge berikut:

```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]
(https://colab.research.google.com/github/Subiono2021/repo/blob/main/example.ipynb)
```
