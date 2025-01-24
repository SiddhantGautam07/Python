# Take a empty Array
str = []

# Accept How many strings
n = int(input("How many Strings? : "))

# Append String to str array
for i in range(n):
    print("Enter the String : ")
    str.append(input())

# Ask for the string to search
q = input("Enter String to search : ")

# Linear Search or Sequential Search
flag = False
for i in range(len(str)):
    if q == str[i]:
        print("Found at : ",i+1)
        flag = True
        # break
if flag == False:
    print("Not Found")

