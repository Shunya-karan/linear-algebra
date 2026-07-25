import numpy as np;
try:
    r=int(input("Enter the number of row for matrix M: "))
    c=int(input("Enter the number of column for matrix M: "))

    M=[]
    N=[]

    for i in range (r):
        rows=[]
        for j in range(c):
            column = int(input(f" Enter the values at M[{i+1}][{j+1}]"))
            rows.append(column)

        M.append (rows)
    M=np.array(M)
    print("Matrix M =\n",M)    

    P=int(input("Enter the Number of column for matrix N:"))
    if(P!=c):
        print("NUMBER OF COLUMN IN M AND N SHOULD BE SAME")
    else:
        for i in range (r):
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
        result=np.dot(N,M)
        print("Multiplication =M\n",result)
except Exception as e:
    print(e)