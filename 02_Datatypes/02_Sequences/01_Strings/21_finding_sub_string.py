str = input("Enter the main string : ")
sub = input("Enter the Sub String : ")

n = str.find(sub,0,len(str))
if n == -1:
    print("Sub string is not Found")
else:
    print("Sub String is Found at Position : ",n+1)
    