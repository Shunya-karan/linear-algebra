import numpy as np

def projection(a,b):
    normB=np.square(np.linalg.norm(b))
    Euclidean = np.dot(a,b)

    print(normB)
    print(Euclidean)
    result=np.dot((Euclidean/normB),b)

    print(result)

totalVector= int(input("Enter Length Of vector:"))
vectorA=[]
vectorB=[]

for i in range(totalVector):
    val=int(input(f"Enter the value for vector element a[{i+1}]"))
    vectorA.append(val)
for i in range(totalVector):
    val=int(input(f"Enter the value for vector element b[{i+1}]"))
    vectorB.append(val)  
print(vectorA)
print(vectorB)

while True:
    userInput=int(input("Enter What You want to do\n1.Projection of b orthogonal to a\n" \
    "1.Projection of a orthogonal to b\n3.Exit\nEnter:"))

    if(userInput==3):
        break
    if(userInput==1):
        projection(vectorA,vectorB)
    elif(userInput==2):
        projection(vectorB,vectorA)