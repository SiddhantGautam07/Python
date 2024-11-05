x = 99

def func():
    global x
    x = 50
    print(x)


print(x)
func()
print(x)

