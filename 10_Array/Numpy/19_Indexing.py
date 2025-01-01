from numpy import *

a = arange(10,16)
print(a)
print()

# Indexing

b = a[1:6:2]
print(b)

i = 0
while (i <len(b)):
    print(b[i])
    i+=1