age = int(input("Enter your Age : "))

if age <= 18:
    print(age, "You are Teenager and Not Eligibal for vote")
elif age >= 90:
    print(age, "Aged Person Not allowed for vote")
else:
    print(age, "You can vote now")
