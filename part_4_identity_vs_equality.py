'''
Truthiness vs. True
The concept of “truthiness” refers to values that evaluate to True when typecast as a Boolean.

“Truthy” values however are not necessarily equal to True.
this is basically saying anyhting that is not False is truthy 
but not necessarily equal to True the boolean value of True
'''

'''
Falsiness
Falsey values in Python are:

0 (for any number type)
0, 0.0, 0j
any empty collection
"", [], set(), {}, range(0)
False
None
All other values are truthy!
'''
# Logical operators
# and
# or
# not
# instead of &&, ||, and !

print(True and False)      # False
print(True or False)       # True
print(True and not False)  # True

# Parentheses can group our conditions, 
# just like JavaScript

print(False and (True or True))  # False
print((False and True) or True)  # True

'''
Short circuiting
If we can already determine the overall outcome of a conditional, 
Python won’t bother evaluating the rest of the statement.

(JavaScript also has short-circuiting)
'''

False and print("not printed")  # does not print
False or print("printed #1")    # prints "printed #1"
True and print("printed #2")    # prints "printed #2"
True or print("not printed")    # does not print

# While loops
# Similar to JavaScript

i = 0
while i < 5:
    print(f"{i}. Hello, world.")
    i += 1

print("You've printed 5 times. Goodbye.")

# Loop control statements 
# break, continue

i = 0
while True:
    print(f"{i}. Hello, world.")
    if i < 4:
        i += 1
        continue
    print("You've printed 5 times. Goodbye.")
    break

'''
Identity vs. Equality
    in JavaScript, == is bad, === is good
    in Python, is and == are both useful, just for different things
    Equality is not about typechecking, it’s just about whether the values are the same
'''

my_int = 4
my_float = 4.0

# check if the values are the same
print(my_int == my_float)  # True

# check if the values are the same and check type
print(my_int == my_float and isinstance(my_int, float))  # False

'''
When to use == (equality):
Most of the time!
    Whenever you are comparing two values to see if they are the same
    strings, numbers, lists, dictionaries, etc
'''

print({"gorilla": "large"} == {"gorilla": "large"}) 
# True

'''
The is operator
What if we compared two dictionaries of the same value with is?
'''

print({"gorilla": "large"} is {"gorilla": "large"}) 
# False

'''
While these dictionaries have the same value, 
they are two distinct objects in memory 
with different identities.
'''

# Use is to check if two objects 
# are the same in memory or not None 

a = []
if a:
    print("a is truthy")
else:
    print("a is falsey")    # prints "a is falsey"

if a is not None:
    print("a is not None")  # prints "a is not None"
else:
    print("a is None")

# Also use is to check if something is True or False

a = 1
print(a == True)  # don't do this
print(a is True)

a = []
print(a == False)  # don't do this
print(a is False)

# Use is to check if two objects are the same in memory

print([] == [])  # True
print([] is [])  # False
a = []
b = a
print(a is b)    # True
b.append(5)
print(a)         # [5]


'''
Interned memory
For many small, immutable (unchangeable) data types, 
Python stores only one distinct copy in memory.

This is a space optimization mechanism called interning.
'''

a = 5
b = 5
print(a is b) # True

c = "hey"
d = "hey"
print(c is d) # True

# Due to interning, these variables can share the same identity if they have equal value.

'''
What is the “identity”
id() returns the “identity” of an object.

Integer which is guaranteed to be unique and constant
for this object during its lifetime (i.e. while the program is running)
'''

print(id(None))
print(id(None))
a = None
print(id(a))

