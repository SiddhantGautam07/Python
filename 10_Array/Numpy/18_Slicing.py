from numpy import *

a = arange(10,16)
print(a)
print()
# Slicing

b = a[1:6:2]
print(b)

c = a[::]
print(c)

d = a[-2:2:-1]
print(d)

e = a[:-2:]
print(e)
