# The Programm with two Functions

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

def add(first_number, second_number):
    """This function takes two numbers and finds their sum.
        It displays the sum as result."""
    print("Sum of Two Numbers :",first_number + second_number)

def message():
    '''
        This function displays a message.
        This is a welcome message to the user.'''
    print("Welcome to Python")

# Now Call teh function
add(first_number,second_number)
message()
