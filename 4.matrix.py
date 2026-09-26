# Demonstrates the following: 
# # ● Enter an r by c matrix M (r and c being positive integers)
#  # ● Display M in matrix format # ● Display the rows and columns of the matrix M 
# # ● Find the scalar multiplication of M for a given scalar. 
# # ● Find the transpose of the matrix M
import numpy as np

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input(f"Enter M[{i+1},{j+1}]: ")))
    matrix.append(row)

matrix = np.array(matrix)

while True:
    print("\n1. Display Matrix")
    print("2. Display Rows")
    print("3. Display Columns")
    print("4. Scalar Multiplication")
    print("5. Transpose")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print(matrix)

    elif choice == 2:
        for i in range(r):
            print("Row", i + 1, "=", matrix[i])

    elif choice == 3:
        for i in range(c):
            print("Column", i + 1, "=", matrix[:,i])

    elif choice == 4:
        scalar = int(input("Enter scalar: "))
        print(matrix * scalar)

    elif choice == 5:
        print(matrix.T)

    elif choice == 6:
        break

    else:
        print("Invalid choice")