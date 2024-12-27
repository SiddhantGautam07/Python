from array import *

arr1 = array('d',[1.3,3.4,6.8,4.0])
for elements in arr1:
    print(elements,end="\t")
print()

arr2 = array(arr1.typecode,(a*3 for a in arr1))
for i in arr2:
    print(i,end="\t")

