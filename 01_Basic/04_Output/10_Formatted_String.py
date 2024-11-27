n1,n2,n3 = 1,2,3

print("number1 = {0}".format(n1))

print("number1 = {0}, number2 = {2}, number3 = {1}".format(n1,n2,n3))

print("number1 = {two}, number2 = {one}, number3 = {three}".format(one = n1, two = n2, three = n3))
 
print()

name , salary = "Ravi", 12500.755455
print("Hello {0}, Your Salary is {1}".format(name,salary))
print()
print("Hey {n}, Your Salary is {s}".format(n = name, s = salary))
print()
print("Hey there {:s}, Your Salary is {:.2f}".format(name,salary))
print()
print("Hello %s, Your Salary is %f" % (name, salary))

