import numpy as np;
try:
    print("Vector Matrix & Matrix-Matrix multiplication\n")
    r=int(input("Enter the number of row for matrix M: "))
    c=int(input("Enter the number of column for matrix M: "))
    M=[]

    for i in range (r):
        rows=[]
        for j in range(c):
            column = int(input(f" Enter the values at M[{i+1}][{j+1}]"))
            rows.append(column)
        M.append (rows)
    M=np.array(M)
    print("Matrix M =\n",M)  

    while True:
        userInput = input("\nEnter Choice\n1. Vector-matrix\n2. MATRIX-MATRIX\n3. Exit: ")
        
        if(userInput=="3"):
            break

        elif(userInput=="2"):
        #Number of Column in matrix M == Number of rows in matrix
            P=int(input("Enter the Number of column for matrix N:"))
            
            N=[]
            for i in range (c):
                rows=[]
                for j in range(P):
                    column = int(input(f" Enter the values at N[{i+1}][{j+1}]"))
                    rows.append(column)
                N.append (rows)
            N=np.array(N)
            print("Matrix N =\n",N,"\n")   

            # result=[]
            # for i in range(r):
            #     vm=[]
            #     for j in range(P):
            #         total=0
            #         for k in range (c):
            #             total+=N[i][k]*M[k][j]
            #         vm.append(total)
            #     result.append(vm)
            # result=np.array(result)
            result=np.dot(M,N)
            print("Multiplication =MxN \n",result)

        elif(userInput=="1"):
            # Length of vector==Number of Column In Matrix 
            v=[]
            for i in range(c):
                val=int(input(f"Enter the value for vector elemene v[{i+1}]"))
                v.append(val)
            v=np.array(v)
            print("\nvector v= ",v)
            result=np.dot(M,v)
            print(f"Vector-Matrix=",np.matrix
                  (result))
        else:
            print("Invalid Choice! Please enter 1, 2, or 3.")

except Exception as e:
    print(e)