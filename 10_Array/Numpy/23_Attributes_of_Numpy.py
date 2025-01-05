from numpy import *

# 1. ndim Attributes :- It is used to find the number of dimensions in the array
a = array([1,2,3,4])
print(a)
print(a.ndim)
print()
b = array([[10,11,12,13],[14,15,16,17]])
print(b)
print(b.ndim)
print()
c = array([[[10,20,30],[40,50,60],[70,80,90]]])
print(c)
print(c.ndim)
print()

# 2. shape Attribute : - It is used to count the number of rows and columns in the array
print(a.shape)
print(b.shape)
print(c.shape)
c.shape = (1,3,3)
print(c)

# 3. size Attribute : - It is used to show the total number of elements in the array.
print(a.size)
print(b.size)
print(c.size)

# 4. Item size Attributes :- It gives the memory size of the array elements in bytes.
print(a.itemsize)
print(b.itemsize)
print(c.itemsize)

# 5. dtype attributes :- It gives the data types of elements in the array.
print(a.dtype)
print(b.dtype)
print(c.dtype)

# 6. nbytes Attributes :- It gives the total number of bytes occupied by an array.
print(a.nbytes)
print(b.nbytes)
print(c.nbytes)
