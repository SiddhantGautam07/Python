from numpy import *

# 1. With the help of array function
a = array([1,2,3,4,5])
a = array([[1,2,3,4],[5,6,7,8]])
print(a)
print()

# 2. With the help of one() and zeros() funciton
b = ones((2,4),int)
print(b)
print()
c = zeros((2,4),int)
print(c)
print()

# 3. With the help of eye() function
d = eye(4, dtype=int)
print(d)
print()

# 4. with the help of reshape() function
e = arange(12)
print(e)
f = reshape(e,(2,3,2))
print(f)
g = reshape(e,(3,2,2))
print(g)

