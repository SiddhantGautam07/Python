from array import *

x = array('i',[10,20,30,40,50,60,70])
n = len(x)
print(n)

# For accessing the indexing value then use 
for i in range(n):
    print(i,end=" ")
print()

# For accessing the value then use
for t in x:
    print(t,end=" ")
print()

# For accessing the value according to their indexing value
for s in range(n):
    print(x[s],end=" ")

