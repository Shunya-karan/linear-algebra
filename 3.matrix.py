# Demonstrates the following:
# ● Enter an r by c matrix M (r and c being positive integers)
# ● Display M in matrix format
# ● Display the rows and columns of the matrix M
# ● Find the scalar multiplication of M for a given scalar.
# ● Find the transpose of the matrix M.

import numpy as np;
try:
    r=int(input("Enter the length of the Row :"))
    c=int(input("Enter the length of the Column :"))

    matrix=[]
    transpose=[]
    for i in range(r):
        row=[]
        for j in range(c):
            column=int(input(f"Enter MATRIX value at row: {i+1} column: {j+1}: "))
            row.append(column)
        matrix.append(row)
    matrix=np.array(matrix)

    while True:
        userInput=int(input("1. Display Matrix\n2. Display Row\n3. Display columns\n4. Scalar Multiplications \n5. Transpose \n6. Exit\nEnter the Choice : "))
        
        if(userInput==6):
            break
        if userInput==1:
            print("Matrix")
            print(matrix)

        elif userInput==2:
            print("ROWS")
            for i in range(r):
                print(f"ROWS {i+1}",matrix[i])
           
        elif userInput ==3:
            print("Column")
            for i in range(c):
                col=[]
                for j in range(r):
                    col.append(matrix[j][i])
                print(f"Column {i+1}",np.array(col))


        elif userInput==4:
            print("Scalar Multiplication")
            scalar=int(input("Enter the value for scalar multiplication for matrix m :"))
            print(matrix*scalar)

        elif userInput==5:
            # for i in range(c):
            #     col=[]
            #     for j in range(r):
            #         col.append(matrix[j][i])
            #     transpose.append(col)
            # transpose=np.array(transpose)

            print(matrix.T)
   
       
except ValueError as e:
        print(e)
