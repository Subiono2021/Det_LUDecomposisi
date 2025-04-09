from sympy import Matrix, simplify, init_printing, latex, eye, prod
from IPython.display import display, Math

init_printing(use_latex=True)

def lu_determinant(A):
    """
    Menghitung determinan matriks A menggunakan LU decomposition:
    det(A) = (-1)^k * prod(diag(U))
    Di mana k adalah banyaknya pertukaran baris (dilihat dari matriks P)

    Parameters:
        A (sympy.Matrix): Matriks persegi

    Returns:
        det_A (sympy.Expr): Determinan dari A
        k (int): Banyaknya pertukaran baris
        P (sympy.Matrix): Matriks permutasi
    """
    # Lakukan dekomposisi LU
    L, U, perm = A.LUdecomposition()
    n = A.rows
    P = eye(n)
    k = 0
    perm = list(perm)

    for i in range(n):
        while perm[i] != i:
            j = perm[i]
            P.row_swap(i, j)
            perm[i], perm[j] = perm[j], perm[i]
            k += 1

    sign = (-1) ** k
    diag_product = simplify(prod([U[i, i] for i in range(U.rows)]))
    det_A = simplify(sign * diag_product)

    # Tampilkan hasil
    display(Math(r"A = " + latex(A)))
    display(Math(r"P = " + latex(P)))
    display(Math(r"L = " + latex(L)))
    display(Math(r"U = " + latex(U)))
    display(Math(r"LU = " + latex(L @ U)))
    display(Math(r"PA = " + latex(P @ A)))
    display(Math(r"\text{Jumlah pertukaran baris } k = " + str(k)))
    display(Math(r"\det(A) = (-1)^k \cdot \prod u_{i,i} = {} \cdot {} = {}".format(
        sign, latex(diag_product), latex(det_A))))

    return det_A, k, P
