str = input("Enter a string : ")
sub = input("Enter a sub String : ")
n = int(input("Enter Position no : "))

# Decrease n by 1 to insert in correct position
n -= 1

# find the number of characters in str, sub
l1 = len(str)
l2 = len(sub)

# take another string as a list
str1 = []

# append 0 to n-1 characters from str to str1
for i in range(n):
    # print("Enter String : ")
    str1.append(str[i])

# Append sub string to str1
for i in range(l2):
    str1.append(sub[i])

# Append the remaining characters from str to str1
for i in range(n,l1):
    str1.append(str[i])

# Convert the individual characters of list into
# a String using join() method with empty string as separator
str1 = "".join(str1)
# Display the total string
print(str1)