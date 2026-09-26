import numpy as np

try:
    r = int(input("Enter order of matrix: "))

    A = []

    for i in range(r):
        row = []
        for j in range(r):
            value = int(input(f"Enter A[{i+1}][{j+1}]: "))
            row.append(value)
        A.append(row)

    A = np.array(A)

    print("\nMatrix A =")
    print(A)

    det = np.linalg.det(A)

    if np.isclose(det, 0):
        print("\nMatrix is Singular")
        print("A is NOT invertible")
    else:
        print("\nMatrix is Non-Singular")
        print("A is Invertible")

        inverse = np.linalg.inv(A)

        print("\nInverse of A =")
        print(inverse)
except ValueError as e:
    print('Invalid Value ',e)