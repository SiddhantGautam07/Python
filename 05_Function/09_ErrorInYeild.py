limit = int(input("Enter any number :"))

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        return i
    
for num in even_generator(limit):
    print(num)
    