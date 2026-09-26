# Plotting a set of complex numbers
# ● Creating a new plot by rotating the given number by a 90, 180, 270 degrees and
# also by scaling by a number a = 1/2, a = 1/3, a = 2 etc.
import matplotlib.pyplot as plt

x,y=map(float,input("Enter complex number part (real,img)").split(","))
#print(x,y)

z=complex(x,y)

while True:
    print("\n1. Rotate 90")
    print("2. Rotate 180")
    print("3. Rotate 270")
    print("4. Original")
    print("5. Half scaling")
    print("6. Double scaling")
    print("7. One-third scaling")
    print("8. Exit")

    a=int(input("Enter Choice (1-8)"))
    if(a==8):
        break
    if(a==1):
        result=z*complex(0,1)
    elif(a==2):
        result=z*complex(-1,0)
    elif(a==3):
        result=z*complex(0,-1)
    elif(a==4):
        result=z
    elif(a==5):
        result=z/2
    elif(a==6):
        result=z*2
    elif(a==7):
        result=z/3
    else:
        print("Invalid")

    plt.plot([0,z.real],[0,z.imag],label="original")
    plt.plot([0,result.real],[0,result.imag],label="result")
    plt.grid()
    plt.legend()
    plt.show()
