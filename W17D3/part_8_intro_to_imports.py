'''
Basic imports in Python
Python import syntax is backwards from import syntax in JavaScript.
'''

# from module_name import variable_name
from random import randint

print(randint(0, 10))

# You can also import an entire module, and then access all the values from it using dot notation.

import random

print(random.randint(0, 10))

'''
Exports in Python
Unlike JavaScript, Python does not require exports. All of the objects, classes, functions, etc. 
that are defined in a module are automatically available to import.
'''

