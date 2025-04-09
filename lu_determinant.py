from sympy import Matrix, simplify, init_printing, latex, eye, prod
from IPython.display import display, Math

init_printing(use_latex=True)

def lu_determinant(A):
    L, U, perm = A.LUdecomposition()
    n = A.rows
    P = eye(n)
    k = 0  # jumlah swap baris

    # Fix: perm adalah daftar pasangan [i, j] yang harus ditukar
    for swap in perm:
        if isinstance(swap, (list, tuple)) and len(swap) == 2:
            i, j = swap
            P.row_swap(i, j)
            k += 1

    sign = (-1) ** k
    diag_product = simplify(prod([U[i, i] for i in range(U.rows)]))
    det_A = simplify(sign * diag_product)

    display(Math(r"A = " + latex(A)))
    display(Math(r"P = " + latex(P)))
    display(Math(r"L = " + latex(L)))
    display(Math(r"U = " + latex(U)))
    display(Math(r"LU = " + latex(L @ U)))
    display(Math(r"PA = " + latex(P @ A)))
    display(Math(r"\text{Jumlah pertukaran baris } k = " + str(k)))
    display(Math(r"\det(A) = (-1)^k \cdot \prod u_{{i,i}} = {} \cdot {} = {}".format(
        sign, latex(diag_product), latex(det_A))))

    return det_A, k, P
