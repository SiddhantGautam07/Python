from numpy import *

x = array([10,20,30,40,50])
print("Original Array =",x)
print()

# Do Arithmetic opeartions on the elements of the array 
print("After adding 5 =",x+5)
print("After Substracting 5 =",x-5)
print("After Multiply 5 =",x*5)
print("After Divide 5 =",x/5)
print("After Reminder 5 =",x%5)
print()

# We can use arrays in expression also 
print("Expression Value =",(x+5)**2-10)
print()

# Do some maths functions
print("Sine Value =",sin(x))
print("Cose Value =",cos(x))
print("tan Value =",tan(x))
print("Biggest Element =",max(x))
print("Smallest Element =",min(x))
print("Sum of all elements =",sum(x))
print("Average of all elements =",mean(x))
