str = input("Enter the main String : ")
sub = input("Enter the Sub String : ")

flag = False
pos = -1
n = len(str)
while True:
    pos = str.find(sub,pos+1,n)
    if pos == -1:
        break
    print("Found at position : ",pos+1)
    flag = True
if flag == False:
    print("Not found")
    