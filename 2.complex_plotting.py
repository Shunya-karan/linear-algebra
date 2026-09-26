import matplotlib.pyplot as plt

x, y = map(float, input("Enter complex number (real,imag): ").split(","))
z = complex(x, y)

while True:
    print("\n1. Rotate 90")
    print("2. Rotate 180")
    print("3. Rotate 270")
    print("4. Original")
    print("5. Half scaling")
    print("6. Double scaling")
    print("7. One-third scaling")
    print("8. Exit")

    choice = int(input("Enter choice: "))

    if choice == 8:
        break

    if choice == 1:
        result = z * complex(0, 1)

    elif choice == 2:
        result = z * complex(-1, 0)

    elif choice == 3:
        result = z * complex(0, -1)

    elif choice == 4:
        result = z

    elif choice == 5:
        result = z * 0.5

    elif choice == 6:
        result = z * 2

    elif choice == 7:
        result = z / 3

    else:
        print("Invalid choice")
        continue

    print("Result =", result)

    plt.plot([0, z.real], [0, z.imag], 'o-', label="Original")
    plt.plot([0, result.real], [0, result.imag], 'o-', label="Result")

    plt.axhline(0)
    plt.axvline(0)
    plt.grid()
    plt.legend()
    plt.show()