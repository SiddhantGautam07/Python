m,n = [int(i) for i in (input("Enter minimum and maximum range : ").split(','))]

x = m
if x % 2 != 0:
    x += 1
while x>=m and x<=n:
    print(x,end="\t")
    x+=2
