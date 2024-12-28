from array import *

arr = array('i',[10,20,30,40,50])
print("Original array :",arr)
print()

# append methods:- it is used to insert the value in array in last postion
s = arr.append(30)
t = arr.append(60)
print("After Append Array is :",arr)
print("Append elements :",s)
print("Append elements :",t)
print()

# insert 99 at position number 1 in arr
arr.insert(1,99)
print("After inserting 99 palce of 1 : ",arr)
print()

# remove an element from arr
arr.remove(20)
print("After removeing 20 : ",arr)
print()

# pop method : It is used to remove the elements form array and list but in last position
n = arr.pop()
print("After using pop() :",arr)
print("Popped elements : ",n)
print()

# finding position of element using index()method
n = arr.index(30)
print("First occurrence of element 30 is at :",n)

# Converting arry into list Using tolist() method
lst = arr.tolist()
print("List :",lst)
print("Array :",arr)

