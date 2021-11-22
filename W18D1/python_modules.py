'''
Python Modules
    A module is code that is imported from a file or directory. 
    A package is a collection of modules. A module/package can be:

    Built-in: already in Python’s standard library
    Third-party: downloaded via command line
    Custom: your own code
    To import code from a module, we use the import keyword. The import keyword will 
    locate and initialize a module, and give you 
    access to the specific names you have imported in the file.
'''

'''
The import keyword
The Python standard library has a number of packages you can import without having 
to install them—they are included when you install Python (documentation).

Let’s use the random package as an example (this would work the same with any package).
'''
import random  # import everything from random
print(random.randint(0, 10))

# with aliasing 
import random as rand  # import everything, alias random as rand
print(rand.randint(0, 10))

'''The import keyword
You can also import just specific functions from a package using the from keyword.'''

from random import randint  # import just the randint function
print(randint(0, 10))

from random import randint, shuffle  # import multiple functions at the same time
print(randint(0, 10))

from random import randint as r_i, shuffle
print(r_i(0, 10))

'''
Import Python code from a file
If I have two files at the same level, I can import one file using the filename (minus the .py)
project_folder
|  my_code.py
|  other_code.py
'''
import import_from_me  # import everything from my_code.py
import_from_me.printer()

from import_from_me import printer  # import just the printer function

printer()

'''
When I import the other_code.py file, 
all of the code in that file will run, 
even if I’m just importing one function.
'''

'''
Import Python code from a subdirectory
project_folder
|  my_code.py
|  other_code.py
|  subfolder
|  |  file_one.py
'''

import import_from_me_too.sub_import_file

# or 

from import_from_me_too import sub_import_file

#or 

from import_from_me_too.sub_import_file import sub_printer

sub_printer()

'''
Quick note about __init__.py
This file should go in any directory being imported. 
It will transform a plain old directory into a Python module/package.

Upon import from a module/package, its__init__.py file is implicitly executed, 
and all objects it defines are bound to the module’s namespace 
(https://docs.python.org/3/reference/import.html#regular-packages).
'''
'''
Why do we need __init__.py if we can import without it?
Python 3.3+ creates an implicit namespace package if no __init__.py 
file exists for a directory. We want to avoid this most of the time!

We need a __init__.py if we want to run the directory as a module, 
if we want to run pytest on it, etc.

This file can be completely empty (and often will be). 
It can also be the place where we initialize our applications!


'''


'''
JavaScript imports
Reminder: In Javascript, when we imported from other files, we used relative import statements.

project_folder
|  top_level_file.js
└──subfolder
|  |  file_one.js
|  |  file_two.js 
The import path changes depending on what file we are in.

// inside top_level_file.js
import { someObject } from "./subfolder/file_two"
// inside file_one.js
import { someObject } from "./file_two"
'''

'''
Python imports
project_folder
|  top_level_file.py
└──subfolder
|  |  __init__.py
|  |  file_one.py
|  |  file_two.py 
In Python, when you are importing code from other files, 
we (usually) use absolute import statements, which are relative to 
the top-level file being executed.

# inside top_level_file.py
import subfolder.file_two
# inside file_one.py
import subfolder.file_two
'''
'''
Python Imports
…that means that if I try to run a file directly, instead of from the intended entrypoint of my 
application, the file won’t work correctly.
'''
'''
# inside top_level_file.py
import subfolder.file_one
print("Hello from top_level_file.py")
# inside file_one.py
import subfolder.file_two
print("Hello from file_one.py")
# inside file_two.py
print("Hello from file_two.py")
'''
'''
If you run the top_level_file.py file at the command line, you will get the following output:

Hello from file_two.py
Hello from file_one.py
Hello from top_level_file.py
If you run the file_one.py file at the command line, you will get the following output:

ModuleNotFoundError: No module named 'subfolder'
If I rewrote file_one.py so that its import statement 
worked when it runs in isolation (import file_two), 
then it wouldn’t work in the context of the application.
'''

'''
Python imports (takeaways)
All import statements must be “absolute” - meaning relative to the top level of your project
Include a __init__.py file in any folder that has python code if you are going to be
importing from that folder. 
The __init__.py file can be completely empty (and often will be).
'''



