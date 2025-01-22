str = input("Enter main String : ")
sub = input("Enter sub String : ")

try:
    n = str.index(sub,0,len(str))
except ValueError:
    print("Sub String is Not Found")
else:
    print("Sub String is Found at positon : ",n + 1)
