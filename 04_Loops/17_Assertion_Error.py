# To handle the assertion Error raised by assert:
x = int(input("Enter a number greater than 0 : "))
try:
    assert (x > 0)
    print("U Entered",x)
except AssertionError:
    print("Wrong input entered")
    