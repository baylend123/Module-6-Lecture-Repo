'''
Wrapping functions with decorators
    A decorator is just fancy syntax for a function that takes in another function
    as a callback and returns a modified version of the callback function.

    We can use decorators to add to or modify the behavior of regular functions.
'''

'''
Decorators
    Decorators can be used to add code that runs before and/or after
    a function runs, or modify the function itself.

    Let’s create a decorator that could be used for logging
'''

'''
Decorators
Without the decorator syntax, we would have to define our function, then reassign 
our function to the return value from invoking the decorator function on our old function.
'''


# decorator function
def logged(func):
    def wrapped():
        print(f"before {func.__name__} runs")
        val = func()
        print(val)
        print(f"after {func.__name__} runs")
        return val
    return wrapped


# function to decorate
def cool_function():
    return "sup"


# before decorating
cool_function()  # returns "sup"

# decorated function
cool_function = logged(cool_function)

# after decorating
cool_function()

# our decorator has to take a function
def logged(func):
    # define the function that we're going to return
    def wrapped():
        # do some logging
        print(f"before {func.__name__} runs")
        # invoke the passed-in function
        val = func()
        # log the return value of the function
        print(val)
        # do more logging
        print(f"after {func.__name__} runs")
        # return the value from invoking the passed-in function
        return val
    # decorator returns the wrapper function—without invoking
    return wrapped

#Decorator syntax

@logged
def printer():
    print("Because of line 26")
    return "Also because of line 26"

printer()

'''
Passing arguments through a decorator
What if I want to wrap functions that take arguments?
'''

def logged(func):
    def wrapped(name):
        print(f"before {func.__name__} runs")
        print(name)
        val = func(name)
        print(val)
        print(f"after {func.__name__} runs")
        return val
    return wrapped


@logged
def cool_function_args(name):
    return f"sup {name}"

'''
Passing arguments through a decorator
What if I want to wrap functions that take arguments… 
but I want to be flexible about what kind of arguments the function takes?
'''

def logged(func):
    def wrapped(*args, **kwargs):
        print(f"before {func.__name__} runs")
        print(args, kwargs)
        val = func(*args, **kwargs)
        print(val)
        print(f"after {func.__name__} runs")
        return val
    return wrapped

@logged
def cool_function_more_args(name, count):
    return f"sup {name} "*count