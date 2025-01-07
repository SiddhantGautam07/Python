from numpy import *

a = matrix([[5,4,1],[2,7,0]])
print(a)
print()

# sorting row-wise
b = sort(a,axis=1)
print(b)
print()

# Sorting column-wise
c = sort(a,axis=0)
print(c)
print()
