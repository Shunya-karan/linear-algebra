import sympy as sp

A = sp.Matrix([
    [1, 2, 2],
    [2, 1, 2],
    [2, 2, 1]
])

eigen = A.eigenvects()

for value, multiplicity, vectors in eigen:
    print("Eigenvalue =", value)
    print("Eigenvector =", vectors[0])