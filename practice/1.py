import numpy as np

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Conjugate")
    print("6. Multiply with Conjugate")
    print("7. Exit")

    choice = int(input("Enter choice (1-7): "))

    if choice == 7:
        break

    z1 = complex(input("Enter first complex number (e.g. 3+4j): ").replace("i","j"))

    if choice in [1, 2, 3, 4]:
        z2 = complex(input("Enter second complex number (e.g. 3+4j): ").replace("i","j"))

    if choice == 1:
        print("Result =", np.add(z1, z2))

    elif choice == 2:
        print("Result =", np.subtract(z1, z2))

    elif choice == 3:
        print("Result =", np.multiply(z1, z2))

    elif choice == 4:
        print("Result =", np.divide(z1, z2))

    elif choice == 5:
        print("Conjugate =", np.conjugate(z1))

    elif choice == 6:
        print("Result =", np.multiply(z1, z1.conjugate()))

    else:
        print("Invalid choice")