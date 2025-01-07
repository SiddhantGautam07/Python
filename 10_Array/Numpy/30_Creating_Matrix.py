from numpy import *

# Using matrix 
arr = [[1,2,3],[4,5,6]]
a = matrix(arr)
print(a)
print()

# Using String

str = '1,2; 3,4; 5,6'
b = matrix(str)
print(b)
print()
b = matrix("1,2; 3,4; 5,6")
print(b)
