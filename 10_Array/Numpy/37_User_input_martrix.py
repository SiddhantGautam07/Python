from numpy import *

row, cols = [int(a) for a in input("Enter the rows and columns :").split()]

str = input("Enter the array elements : ")
m = matrix(str)

x = reshape(m,(row,cols))
print("The Original Matrix : ")
print(x)

print("The Transpose Matrix :")
y = x.getT()
print(y)
