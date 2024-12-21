# All about Loops

- Assert Statement
    - It is used to give the appropriated input inside the input container.
    - If any users gives the input beyond the limitation then it through Error in run time.
    - Ex:-1 <br> n = int(input("Enter a number greater than 0 : "))
assert n > 0, "Wrong number you Entered"
print("U Entered",n)

- AssertionError is Exception and Exception is an error that occurs during runtime.
- To avoide such type of exceptions, we can handle them using <b>'try.....except' statements.</b>
- Ex: 2.<br> # To handle the assertion Error raised by assert:<br>
x = int(input("Enter a number greater than 0 : "))<br>
try:<br>
    assert (x > 0)<br>
    print("U Entered",x)<br>
except AssertionError:<br>
    print("Wrong input entered")
    