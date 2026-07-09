import matplotlib.pyplot as plt
import numpy as np
# xpoints = np.array([2,0])
# ypoints = np.array([3,0])
# x1points = np.array([-3,0])
# y1points = np.array([2,0])
# x3points = np.array([-2,0])
# y3points = np.array([-3,0])
# plt.plot(xpoints,ypoints,marker = 'o')
# plt.plot(x1points,y1points,marker = 'o')
# plt.plot(x3points,y3points,marker = 'o')
# plt.show()


a = input("Enter complex number (real,imag): ")
x1, y1 = map(float, a.split(','))
print(x1,y1)
z= complex(x1,y1)
while True:
    userInput=input("1. Rotate 90\n2.Rotate 180\n3.Rotate 270\n4.original\n5.half scaling\n6double scaling\n7 one third\n8 exit \nEnter Choice :").lower()
    if userInput=="exit" or userInput=="8":
            break
    plt.plot([0, z.real], [0, z.imag], marker='o', label='Original')  
    if(userInput=="90" or userInput=="1"):
        z1=z*complex(0,1)
        print(z1)
        plt.plot([0, z1.real], [0, z1.imag], marker='o', label='90')
    elif (userInput=="180" or userInput=="2"):
        z1=z*complex(-1,0)
        print(z1)
        plt.plot([0, z1.real], [0, z1.imag], marker='o', label='180')  
    elif (userInput=="270" or userInput=="3"):
        z1=z*complex(0,-1)
        print(z1)
        plt.plot([0, z1.real], [0, z1.imag], marker='o', label='270')
    elif (userInput=="half scaling" or userInput=="5"):
        z1=z*0.5
        print(z1)
        plt.plot([0, z1.real], [0, z1.imag], marker='o', label='half scaling')
    elif (userInput=="double scaling" or userInput=="6"):
        z1=z*2
        print(z1)
        plt.plot([0, z1.real], [0, z1.imag], marker='o', label='double scaling')
    elif (userInput=="one third scaling" or userInput=="7"):
        z1=z*(1/3)
        print(z1)
        plt.plot([0, z1.real], [0, z1.imag], marker='o', label='one third scaling')
    elif(userInput=="original" or userInput=="4"):
         print(z)
    else:
         print("Invalid choice pls Enter a number between 1 to 8")
    plt.grid()
    plt.axhline(0,color="black")
    plt.axvline(0,color="black")
    plt.legend()
    plt.show()
    plt.close()