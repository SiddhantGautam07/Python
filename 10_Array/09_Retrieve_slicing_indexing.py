from array import *

x = array('i',[10,20,30,40,50,60,70,80,90,100])

n = x[7]
print(n)

t = x[4:9]
print(t)

for i in range(len(x)):
    print(x[i],end=" ")
print()

for f in x[4:9]:
    print(f,end=" ")
print()

x.append(4)
print(x)

a = x.count(50)
print(a)


