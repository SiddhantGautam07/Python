n = int(input("Enter any number : "))


for i in range (1,11):
    if i == 5:
        continue
    table = i * n
    print(n, "x", i, "=",table)
print()

# Table Printing
for num in range (1,11):
    table = num * n
    print(n, "x", num, "=",table)



