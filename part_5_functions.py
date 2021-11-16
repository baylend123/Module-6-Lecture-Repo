'''
Python Functions:
    We use the def keyword to define a function followed by:
        The name of the function
        The arguments that it accepts
        A new block identified as : and indent the next line
'''
def is_even(num):
    return num % 2 == 0

print(is_even(5)) # False
print(is_even(2)) # True

'''
Lambda Functions
    For simple one-line functions, we can also use a lambda, which takes in:
    Arguments on left side of :
        Returns the value resulting from the right side of the :
            They return automatically and cannot contain an explicit return keyword
'''

is_even = lambda num: num % 2 == 0

print(is_even(8)) # True

'''
PEP-8 Style Guidlines
The use case of lambdas is when 
you are going to use a function once without assigning it
Assigning a lambda to a variable essentially duplicates the purpose of the def keyword,
hence it is not pythonic
'''
def order_pizza(pizza_type):
    order = f"I would like a {pizza_type} pizza"
    print(pizza_type)
    return lambda topping_type: order + f" with {topping_type}."

sausage_pizza = order_pizza("sausage") 
# prints from line 3: "sausage" 

print(sausage_pizza)
# prints lambda function object

print(sausage_pizza("bell pepper")) 
# "I would like a sausage pizza with bell pepper."

'''
Python Scoping:
    Scoping is done at the function level
    In JS, we had block scopes
    In PY, our if statements do not create new scopes
'''
def make_a_five():
    y = 5
    return y

if True:
    x = 10


print(x) #10
# `x` was created in the global scope

# print(y) # NameError: name 'y' is not defined
# `y` was created in the scope of the make_a_five function