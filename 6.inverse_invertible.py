import numpy as np

try:
    while True:
        r=int(input("Enter the Form of Matrix :"))

        Matrix1 = []
        for i in range (r):
            rows=[]
            for j in range(r):
                column = int(input(f"Enter value for A{i+1}{j+1} : "))
                rows.append(column)
            Matrix1.append (rows)
        Matrix1=np.array(Matrix1)
        print("Matrix A = \n",Matrix1) 

        determinat = np.linalg.det(Matrix1)
        print(int(determinat))
        if determinat == 0:
            print("Matrix Is Singular \nA Is Not Invertible \nA Inverse Does Not Exists")
        else:
            print("Matrix Is Non-Singular \nA Is Invertible \nA Inverse Exists")  
            inverse = np.linalg.inv(Matrix1)  
            print("A Inverse : ",inverse)
    
except ValueError as e:
    print('Invalid Value ',e)