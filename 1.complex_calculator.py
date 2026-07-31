# Write a Python program to take the required complex number(s) as input from the user and perform the following operations(from user input): addition, subtraction, multiplication, division, finding the conjugate of a complex number, and multiplication of a complex number with its conjugate.
try:
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
except Exception as e:
    print(e)










#while True:
# try:
# real1, imag1 = map(int, input(&quot;Enter 1st complex number
# (real,imag): &quot;).split(&quot;,&quot;))
# real2, imag2 = map(int, input(&quot;Enter 2nd complex number
# (real,imag): &quot;).split(&quot;,&quot;))
# break
# except ValueError:
# print(&quot;Invalid input! Please enter in format: real,imag
# (example: 3,4)&quot;)
# z1=complex(real1, imag1)
# z2=complex(real2, imag2)
# while True:
# opr = input(&#39;Operations (add=1 , conjugate=2, mul=3, subtract=4,
# multiply_by_its_conjugate=5) s to stop:&#39;)
# if opr==&quot;1&quot;:
# print(&quot;Z1 + Z2: &quot;, z1+z2)
# elif opr==&quot;2&quot;:
# print(&quot;Conjugate of z1: &quot;,z1.conjugate())
# print(&quot;Conjugate of z2: &quot;,z2.conjugate())
# elif opr==&quot;3&quot;:
# print(&quot;Multiplication: &quot;,z1*z2)
# elif opr==&quot;4&quot;:
# print(&quot;Subtraction: &quot;, z1-z2)
# elif opr==&quot;5&quot;:
# cz1 = z1.conjugate()
# cz2 = z2.conjugate()
# print(&quot;Multiplication of z1 conjugate: &quot;,cz1*z1)
# print(&quot;Multiplication of z2 conjugate: &quot;,cz2*z2)
# elif opr==&quot;s&quot;:
# break
# else:
# print(&quot;wrong input&quot;)