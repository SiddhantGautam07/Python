def sum_all(*args):
    print(*args)
    return sum (args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8))
print()

def sum_a(*args):
    print(args)
    return sum(args)

print(sum_a(1,2))
print(sum_a(1,2,3,4,5))
print(sum_a(1,2,3,4,5,6,7,8))
