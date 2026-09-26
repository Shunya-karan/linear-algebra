# Demonstrates the following: 
# # ● Enter an r by c matrix M (r and c being positive integers)
#  # ● Display M in matrix format # ● Display the rows and columns of the matrix M 
# # ● Find the scalar multiplication of M for a given scalar. 
# # ● Find the transpose of the matrix M

import numpy as np
r=int(input("Enter the number of rows"))
c=int(input("Enter the number of cols"))

matrix=[]

for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"Enter M[{i+1}{j+1}]: ")))
    matrix.append(row)

matrix=np.array(matrix)

while True:
    print("1.Matrix")
    print("2.Rows")
    print("3.columns")
    print("4.scalar Multiplicaton")
    print("5.transpose")
    print("6.Exit")

    choice=int(input("Enter Choice: "))

    if(choice==1):
        print(matrix)
    elif(choice==2):
        for i in range(r):
            print(f"Row{i+1}={matrix[i]}")
    elif(choice==3):
        for i in range(c):
            print(f"Columns{i+1}={matrix[:,i]}")
    elif (choice==4):
        sc=int(input("Enter Scalar Value: "))
        print(matrix*sc)

    elif(choice==5):
        print(matrix.T)
    elif(choice==6):
        break
    else:
        print("Invalid")

