from numpy import *

a = arange(10)
print(a)

# 1. reshape() method :- it is used to covert 1D array inot another Dimension array.
print(a.reshape(2,5))
print(a.reshape(5,2))
print()

# 2. flatten() Method :- It is used to return a copy of the array collapsed into one dimension.
b = array([[1,2,3],[4,5,6]])
print(b)
print(b.flatten())
