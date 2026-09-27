import numpy as np

def projection(firstVector,secondeVector):
    norms=np.square(np.linalg.norm(secondeVector))
    euclidien=np.dot(firstVector,secondeVector)
    AProjectionOnB = np.dot((euclidien/norms),secondeVector)
    print(AProjectionOnB)

n=int(input("enter the number of the elements: "))
u=[]
v=[]

for i in range(n):
    u.append(int(input(f"Enter the element u[{i+1}]: ")))
for i in range(n):
    v.append(int(input(f"Enter the element v[{i+1}]: ")))




while True:
    print("1.projection u on v")
    print("2.projection v on u")
    print("3.Exit")
    choice=int(input("Enter choice(1-3): "))
    if(choice==1):
        projection(u,v)
    elif(choice==2):
        projection(v,u)
    elif(choice==3):
        break