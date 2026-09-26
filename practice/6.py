import numpy as np

r=int(input("enter the order of the matrix: "))

m=[]
for i in range(r):
    row=[]
    for j in range(r):
        row.append(int(input(f"enter m{i+1}{j+1}: ")))
    m.append(row)

m=np.array(m)

det=np.linalg.det(m)
print("determinant",det)

if(np.isclose(det,0)):
    print("It is singilar matrix")
    print("It is not invertible")
else:
    print("It is not singilar matrix")
    print("It is  invertible")
    inv=np.linalg.inv(m)
    print("Inverse=\n",inv)

