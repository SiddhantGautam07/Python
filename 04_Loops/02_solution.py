n = int(input("Enter any number : "))

sum_even = 0

for i in range (1, n+1):
    if i % 2 == 0:
        sum_even += 1

print("Sum of all Even Number are :",sum_even)
