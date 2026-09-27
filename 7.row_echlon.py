import sympy as sp

# Ask for matrix size
print("Row Echlon Form\n")
r = int(input("Enter the number of rows for matrix M: "))
c = int(input("Enter the number of columns for matrix M: "))

matrix = []

# Input matrix
for i in range(r):
    row = []
    for j in range(c):
        value = int(input(f"Enter the value at M[{i+1}][{j+1}]: "))
        row.append(value)
    matrix.append(row)

# Create SymPy matrix
A = sp.Matrix(matrix)

print("\nOriginal Matrix:")
sp.pprint(A)

# RREF
rref_matrix, pivot_columns = A.rref()
sp.pprint(A.echelon_form())
print("\nReduced Row Echelon Form (RREF):")
sp.pprint(rref_matrix)
sp.pprint(pivot_columns)

