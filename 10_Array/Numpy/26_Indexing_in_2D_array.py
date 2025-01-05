from numpy import *

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
print()
for i in range(len(a)):
    print(a[i])
print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=" ")
