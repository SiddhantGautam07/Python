x = 99

def f1():
    x = 88
    def f2():
        print(x)
    return f2

myResult = f1()
print(myResult())
