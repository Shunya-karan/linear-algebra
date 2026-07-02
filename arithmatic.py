# Write a Python program to take the required complex number(s) as input from the user and perform the following operations(from user input): addition, subtraction, multiplication, division, finding the conjugate of a complex number, and multiplication of a complex number with its conjugate.
while True:
    print("\n===== Complex Number Operations =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Conjugate of a Complex Number")
    print("6. Multiplication with its Conjugate")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 7:
        print("Program Ended.")
        break

    elif choice in [1, 2, 3, 4]:
        c1 = complex(input("Enter first complex number (e.g., 3+4j): ").replace("i","j"))
        c2 = complex(input("Enter second complex number (e.g., 2-5j): ").replace("i","j"))

        if choice == 1:
            print("Addition =", c1 + c2)

        elif choice == 2:
            print("Subtraction =", c1 - c2)

        elif choice == 3:
            print("Multiplication =", c1 * c2)

        elif choice == 4:
            if c2 != 0:
                print("Division =", c1 / c2)
            else:
                print("Division by zero is not possible.")

    elif choice == 5:
        c = complex(input("Enter a complex number: "))
        print("Conjugate =", c.conjugate())

    elif choice == 6:
        c = complex(input("Enter a complex number: "))
        print("Multiplication with its conjugate =", c * c.conjugate())

    else:
        print("Invalid Choice! Please enter a number between 1 and 7.")