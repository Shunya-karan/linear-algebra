import numpy as np

r=int(input("Enter Number of rows: "))
c=int(input("Enter Number of columns: "))
M=[]

for i in range(r):
    row=[]
    for j in range(c):
        col=int(input(f"Enter M[{i+1}{j+1}]: "))
        row.append(col)
    M.append(row)

m=np.array(M)
print("matrix M=",m)

while True:
    print("1.vector-matrix multiplication")
    print("2.matrix-matrix multiplication")
    print("3.exit")

    choic=int(input("Enter choice: "))
    if(choic==3):
        break
    if(choic==1):
        v=[]
        for i in range(r):
            v.append(int(input(f"Enter value for vector v[{i+1}]")))

        v=np.array(v)
        print("Vector-Matrix=",np.dot(v,m))
    elif(choic==2):
        N=[]
        p=int(input("Enter the number of column in matrix N"))

        for i in range(c):
            row=[]
            for j in range(p):
                col=int(input(f"Enter M[{i+1}{j+1}]: "))
                row.append(col)
            N.append(row)

        n=np.array(N)
        print("matrix N=",n)

        print("Matrix-Matrix=",np.dot(m,n))

    else:print("invalid")