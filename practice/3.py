# Demonstrates the following:
# ● Enter a vector u as a n-list
# ● Enter another vector v as a n-list
# ● Find the vector au + bv for different values of a and b
# ● Find the dot product of u and v

import numpy as np

n=int(input("Enter the length of the vector: "))

u=[]
v=[]

for i in range(n):
    vectoU=int(input(f"Enter u{i+1}: "))
    u.append(vectoU)
for i in range(n):
    vectoV=int(input(f"Enter v{i+1}: "))
    v.append(vectoV)

u=np.array(u)
v=np.array(v)

while True:
    print("1.au+bv")
    print("2.dot product")
    print("3.exit")
    choice=int(input("enter a choice: "))

    if(choice==1):
        a=int(input("Enter a: "))
        b=int(input("Enter b: "))

        print("au=",a*u)
        print("bv=",b*v)
        print("result=",a*u+b*v)
    elif(choice==2):
        print("dotproduct",np.dot(u,v))
    elif(choice==3):
        break
    else:
        print("Invalid Choice")