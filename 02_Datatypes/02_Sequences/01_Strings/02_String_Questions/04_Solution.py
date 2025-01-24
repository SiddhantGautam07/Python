str = []

n = int(input("How many strings? : "))

for i in range(n):
    print("Enter String : ",end="")
    str.append(input())

str1 = sorted(str)

print("Sorted list: ")
for i in str1:
    print(i)
    