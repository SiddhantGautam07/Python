list = [10,20,30,40,50,60,70,80,100]
sum = 0

for i in list:
    print(i,end="\t")
    sum = sum + i

print("Sum =",sum)


while i < len(list):
    print(list[i],end="\t")
    sum = sum + list[i]
    i+=1
print("Sum =",sum)
