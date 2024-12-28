from array import *

x = array('i',[])
print("How many elements? :",end=' ')
n = int(input())

for i in range(n):
    print("Enter element : ",end=' ')
    x.append(int(input()))
print("Original array :",x)

# Bubble Sort
f = False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t = x[j]
            x[j] = x[j+1]
            x[j+1] = t
            f = True
    if f == False:
        break
    else:
        f = False
print("sorted array =",x)

