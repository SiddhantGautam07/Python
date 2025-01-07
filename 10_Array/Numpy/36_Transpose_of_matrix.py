from numpy import *

a = matrix("1,2,3; 4,5,6; 7,8,9")
print(a)
print()

# Tropose() methods
b = a.transpose()
print("transpose =",b)
print()

# getT() method
c = a.getT()
print("getT =",c)
print()

# getA() method
d = a.getA()
print("getA =",d)
print()

# getA() method
e = a.getA1()
print("getA1 =",e)
print()


