a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if a > b and a > c:
    print(a, "is Greater Number")
elif b > a and b > c:
    print(b, "is Greater Number")
else:
    print(c, "is Greater Number")
    