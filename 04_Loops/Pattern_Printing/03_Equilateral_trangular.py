n = int(input("Enter any number : "))
for i in range(1,11):
    print(' '*n, end='')
    print('* '*(i))
    n-=1
