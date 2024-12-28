from array import *

x = array('i',[])
print("How many Elements? :",end=' ')
n = int(input())

for i in range(n):
    print("Enter element =",end=' ')
    x.append(int(input()))
print("Original Array =",x)

print("Enter element to search :",end=' ')
s = int(input())

# Serching using index method

try:
    pos = x.index(s)
    print("Found at Position =",pos+1)
except ValueError:
    print("Not Found in the array")
    