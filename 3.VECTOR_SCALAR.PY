import numpy as np

n = int(input("Enter length of vector: "))

u = []
v = []

for i in range(n):
    VectorU=int(input(f"Enter a vector u {i+1} value: ")) 
    u.append(VectorU)

for i in range(n):
    VectorV=int(input(f"Enter a vector v {i+1} value: ")) 
    v.append(VectorV)
u = np.array(u)
v = np.array(v)

while True:
    print("\n1. Find au + bv")
    print("2. Dot Product")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))

        result = a * u + b * v
        print("au=", a*u)
        print("bv =", b*v)

        print("au + bv =", result)

    elif choice == 2:
        print("Dot Product =", np.dot(u, v))

    elif choice == 3:
        break

    else:
        print("Invalid choice")