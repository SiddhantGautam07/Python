from numpy import *

a = array([10,20,30,40])
b = array([20,10,30,40])

c = a > b
print("Result of a > b :",c)

print("Check if any one element is true :",any(c))
print("Check if all elements are true :",all(c))

if(any(a>b)):
    print("a contains atleast one element greater than those of b")