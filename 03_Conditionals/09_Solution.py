year = int(input("Enter the Year : "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"is leap Year")
else:
    print(year,"is NOT leap Year")

    