from numpy import *

a = matrix("1,2,3; 4,5,6; 7,8,9")
print(a)
print()

# Calculating Column-wise
b = a.prod(0)
print(b)
print()

# Calculating Row-wise
c = a.prod(1)
print(c)

