import numpy as np

n=int(input("Enter the number of elements"))

u=[]
v=[]

for i in range(n):
    u.append(int(input(f"Enter u{i+1}: ")))

for i in range(n):
    v.append(int(input(f"Enter v{i+1}: ")))

v=np.array(v)
u=np.array(u)
print("face vector u=",u)
print("face vector v=",v)
while True:
    print("1.Linear combination")
    print("2.Avg faces")
    print("3.Exit")

    choice=int(input("Enter choice 1-3"))

    if(choice==1):
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        print("Linear combination=",a*u+b*v)
    elif(choice==2):
        print("Average faces=",(u+v)/2)
    elif(choice==3):
        break
    else:
        print("invalid")


