n = int(input("Enter any number : "))

for num in range(2,n+1):
    # print(num,end=" ")
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num,end=" ")