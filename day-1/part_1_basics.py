# Printing to the console.. Python vs Javascript

# Python, print() keyword

print("Printing in python")

# Comments in Python uses the # symbol

print("Comment inline") # This is a comment


'''

    Multiline comments in Python
    Comment Block

'''

# Number types in Python

#int
my_int = 1
#float
my_float = 1.1

# Math operators

# Addition
print(10 + 4) # 14
# Subtraction
print(10-4) # 6
# Multiplication
print(10*4) # 40
# Division
print(10/4) # 2.25
# Modulus
print(10%4) # 2
# Exponent
print(10**4) # 10000
# Floor Division
print(10//4) # 2

'''
Plus operator (+) can be used for 
both numeric addition
and string concatenation,

But type conversion between strings and numbers
won’t happen automatically (unlike JavaScript)
'''

print("hello " + "world")  # "hello world"
print("hello " + 7)        # TypeError
# explicitly convert types
print("hello" + str(7))    # "hello7"

'''
We can use assignment operators
(like in JavaScript) to concisely 
update values
'''
a = 2
a += 3 
print(a)  # 5
a *= 2
print(a)  # 10

## ++ and -- are not supported in Python

# print(a++) # 10

# a+=1 works


 


