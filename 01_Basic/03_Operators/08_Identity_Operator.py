a = 23
b = 23

print(id(a))
print(id(b))
print()

if a is b:
    print("a and b have same identity")
else:
    print("a and b do not have same identity")
print()

x = [1,2,3,4]
y = [1,2,3,4]

if x is y:
    print("X and Y is Same")
else:
    print("X and Y is Not Same")
print(id(x))
print(id(y))
print()

if x == y:
    print("X and Y is Same ")
else:
    print("X and Y is not same")


