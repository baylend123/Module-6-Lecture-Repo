'''
The input() function
input() receives input from the user via standard input and returns it as a string.

It takes an optional string prompt as an argument that is printed to standard output.
'''

name = input("What's your name? ")
print(name)

'''
Code from Input Validation Walkthrough
'''

print("Welcome to the bday calculator. Enter 0 to end.")
age = 1

while age:
    age = input("What's your age? ")
    if age:
        try:
            age = int(float(age))
            if age > 0 and age < 120:
                print(f"Cool! You've had {age} birthdays.")
            elif age == 0:
                print("Goodbye!")
            else:
                print("Out of range. Please try again.")
        except ValueError:
            print("Please enter a number.")

