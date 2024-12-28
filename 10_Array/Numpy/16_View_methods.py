from numpy import *

a = arange(1,6)
b = a.view()
print("Original elements :",a)
print("New elements :",b)
print()

b[0]= 99
print("After Modificaiton :",b)
print("Original elements :",a)
print("New elements :",b)
