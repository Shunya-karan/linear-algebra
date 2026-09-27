import sympy as sp

r=int(input("Enter the number of the row: "))
c=int(input("Enter the number of the column: "))

m=[]

for i in range(r):
    row=[]
    for j in range(c):
        row.append(int(input(f"Enter the value M{i+1}{j+1}")))
    m.append(row)

m=sp.Matrix(m)

sp.pprint(m)

# sp.pprint(m.echelon_form())
rrf,pivot=m.rref()
sp.pprint(rrf)
print(pivot)