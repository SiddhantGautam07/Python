from array import *
lst = [int(num) for num in input("Enter marks : ").split(',')]

marks = array('i',lst)

sum = 0
for x in marks:
    print(x)
    sum = sum + x
print("Total Marks =",sum)

# Percentage
n = len(marks)
percentage = sum / n
print("Percentage =",percentage)



