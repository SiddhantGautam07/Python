# To take input to the users
str = input("Enter a string : ")

i = c = 0
flag = True
for s in str:
    if flag == False and str[i] == " ":
        c+=1
    if str[i]==" ":
        flag = True
    else:
        flag = False
    i+=1
print("No. of Words : ",c+1)
