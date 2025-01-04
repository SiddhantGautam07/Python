from numpy import *

arr3 = array([[[1,2,3,4],
               [5,6,7,8],
               [8,9,10,11]]])
print(arr3)

b = array([[[1,2,3],[4,5,6],[7,8,9]]])
print(b)

c = array([[[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]])
print(c)

print(arr3.ndim)
print(b.ndim)
print(c.ndim)


