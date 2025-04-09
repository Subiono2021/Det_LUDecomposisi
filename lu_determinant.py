from sympy import Matrix, simplify, init_printing, latex, eye 
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
    # Perform LU decomposition with pivoting
    L, U, perm_list = A.LUdecomposition()

    # Build the permutation matrix from the row swap indices (perm_list)
    n = A.rows
    P = eye(n)  # eye function is now imported and available
    k = 0  # Initialize the row swap count

    # Fix: Handle potential lists in perm_list for pivoting
    for item in perm_list:
        if isinstance(item, list):  # Check if item is a list (indicating a swap)
            i, j = item  # Get the row indices for the swap
            P.row_swap(i, j)  # Perform the row swap on the permutation matrix
            k += 1  # Increment the row swap count

    # Determinant = (-1)^k * product(diagonal U)
    sign = (-1)**k # sign = det(P) which is (-1)^k
    # Use list comprehension and then the prod function to calculate the product of diagonal elements

    from sympy import prod
    diag_product = simplify(prod([U[i, i] for i in range(U.rows)]))
    det_A = simplify(sign * diag_product)

    # Tampilkan hasil
    display(Math(r"A = " + latex(A)))
    display(Math(r"P = " + latex(P)))
    display(Math(r"L = " + latex(L)))
    display(Math(r"U = " + latex(U)))
    display(Math(r"LU = " + latex(L@U)))
    display(Math(r"PA = " + latex(P@A)))
    # Perbaikan: Menambahkan kurung kurawal ganda pada teks "Jumlah pertukaran baris"
    display(Math(r"\text{{Jumlah pertukaran baris $P$: }} k = {}".format(k)))
    display(Math(r"\det(A) = (-1)^k  \prod u_{{i,i}} = {} \times {} = {}".format(sign, latex(diag_product), latex(det_A))))

    return det_A, k, P

A = Matrix([[0, 2, 3, 4], [0, 0, 7, 8], [1, 10, 11, 1], [13, 7, 15, 11]])
detA, k, P= lu_determinant(A)
