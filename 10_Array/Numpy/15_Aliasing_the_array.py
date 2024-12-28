from numpy import *

a = arange(1,10)
b = a
print("Original Array =",a)
print("Alias Array =",b)
print()

b[0]=99
print("After Modification =",b)
print("Original Array =",a)
print("Alias Array =",b)
