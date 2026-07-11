import time
start = time.perf_counter()

lenOfVector=int(input("Enter the length of the vector: "))
u=[]
v=[]
dotProduct=0

for i in range(lenOfVector):
    VectorU=int(input(f"Enter a vector u {i+1} value: "))
    u.append(VectorU)
for i in range(lenOfVector):
    VectorV=int(input(f"Enter a vector v {i+1} value: "))
    v.append(VectorV)

while True:
    userInput=input("Enter Choice 1.Scalar Multiplication 2.Dot product .Exit: ")
    if(userInput=="3"):
        break

    if(userInput=="1"):
        a=int(input("Enter value of a :"))
        b=int(input("Enter value of b :"))

        au=[]
        bv=[]
        for i in range(len(u)):
            au.append(u[i]*a)
            bv.append(v[i]*b)
        result=[]
        for i in range(lenOfVector):
            result.append(au[i]+bv[i])

        print("au=",au)
        print("bv=",bv)
        print("au+bv=",result)
        end = time.perf_counter()
        print(f"Time = {end - start:.10f} seconds")
    elif(userInput=="2"):
        for i in range(len(u)):
            dotProduct +=(u[i]*v[i])
        print("DotProduct:",dotProduct)
        end = time.perf_counter()
        print(f"Time = {end - start:.10f} seconds")

        
