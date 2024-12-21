n = int(input("Enter the Positive Number Only : "))

try:
    assert n > 0
    if n % 2 == 0:
        print(n,"is Even Number")
    else:
        print(n,"is Odd Number")
except AssertionError:
    print("You Entered Negative Number")


