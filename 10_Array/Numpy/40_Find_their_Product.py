import sys
from numpy import *

row1,cols1 = [int(a) for a in input("Enter the rows1 and Columns1 :").split()]
row2,cols2 = [int(b) for b in input("Enter the rows2 and Cloumns2 : ").split()]
if row2 != cols1:
    print("Multiplication is not Possible")
    sys.exit()
str = input("Enter the first Matrix elements :")
m = reshape(matrix(str),(row1,cols1))
print("First Matrix =",m)

str2 = input("Enter the second Matrix elements : ")
n = reshape(matrix(str2),(row2,cols2))
print("Second Matrix = ",n)

print("The product of Matrix =")
c = m * n
print(c)

