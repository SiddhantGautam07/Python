from numpy import *

a = [[1,2,3],[4,5,6],[7,8,9]]
print(a)
a = reshape(a,(3,3))
print(a)
print()

# It will print entire arrays
b = a[:,:]
b = a[:]
b = a[: :]
print(b)
print()

c = a[0, :]
print(c)
c = a[1, :]
print(c)
c = a[2, :]
print(c)
print()

d = a[:, 0]
print(d)
d = a[:, 1]
print(d)
d = a[:, 2]
print(d)
print()

e = a[0:1, 0:1]
print(e)
e = a[1:2, 1:2]
print(e)
e = a[:, 1:3]
print(e)
print()