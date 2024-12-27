from array import *

x = array('i',[10,20,30,40,10,20,30,50,60,40])
n = len(x)
print(n)

i = 0
while i < n:
    print(x[i],end=" ")
    i+=1
    