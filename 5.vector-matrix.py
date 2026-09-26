import numpy as np

print("Vector-Matrix & Matrix-Matrix Multiplication")

r = int(input("Enter rows of matrix M: "))
c = int(input("Enter columns of matrix M: "))

M = []

# Create Matrix M
for i in range(r):
    row = []
    for j in range(c):
        value = int(input(f"Enter M[{i+1}][{j+1}]: "))
        row.append(value)
    M.append(row)

M = np.array(M)

print("\nMatrix M =")
print(M)

while True:

    print("\n1. Vector-Matrix Multiplication")
    print("2. Matrix-Matrix Multiplication")
    print("3. Exit")

    choice = input("Enter choice: ")

    # Exit
    if choice == "3":
        break

    # Vector-Matrix
    elif choice == "1":

        v = []

        # Length of vector = rows of M
        for i in range(r):
            value = int(input(f"Enter v[{i+1}]: "))
            v.append(value)

        v = np.array(v)

        print("Vector v =", v)

        result = np.dot(v, M)

        print("v × M =", result)

    # Matrix-Matrix
    elif choice == "2":

        # M is r × c
        # N must be c × p

        p = int(input("Enter columns of matrix N: "))

        N = []

        for i in range(c):
            row = []

            for j in range(p):
                value = int(input(f"Enter N[{i+1}][{j+1}]: "))
                row.append(value)

            N.append(row)

        N = np.array(N)

        print("\nMatrix N =")
        print(N)

        result = np.dot(M, N)

        print("\nM × N =")
        print(result)

    else:
        print("Invalid choice")