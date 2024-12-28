from array import *

a = array('i',[])

print("How many elements? :",end=' ')
n = int(input())

for i in range(n):
    print("Enter element :",end=' ')
    a.append(int(input()))
print("Original Array =",a)

print("Enter element to search :",end=' ')
s = int(input())

# Linear Search or Sequential Search
flag = False

for i in range(len(a)):
    if s == a[i]:
        print("Found at position =",i+1)
        flag = True
if flag == False:
    print("Not Found in the array")
    