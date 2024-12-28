from numpy import *

a = arange(1,10)
b = a.copy()
print("Original Array =",a)
print("Copy Array =",b)
print()

b[0] = 25
print("After Modification =",b)
print("Original Array =",a)
print("copy array =",b)
