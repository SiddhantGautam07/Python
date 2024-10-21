number = int(input("Enter any Number : "))

if number % 2 == 0:
    print(number,"is Even Number")
elif number < 0 and number % 2 == 0:
    print(number,"is Negative Even Number")
elif number < 0 and number % 2 != 0:
    print(number,"is Nagative Odd Number")
else:
    print(number,"is Odd Number")
    

