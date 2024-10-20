number = int(input("Enter your number : "))

factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial of Your number is :",factorial)

