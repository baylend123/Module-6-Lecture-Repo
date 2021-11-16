# String Data Types

# Strings can use '' or ""

# Using ''' or """ allows you to write long strings

my_short_string = "hello"

my_long_string = '''
you can make
longer strings over multiple lines
individual quote characters ' " won't end the string
'''

# Thre string interpolation methods 

# 1 % sign
# good 

word = "hi"
num = 6
print("%s is a word. %i is an integer" % (word, num))

# prints "hi is a word. 6 is an integer"
# 2 .format()
# better

word = "hi"
num = 6
print("{stuff} and {number}".format(stuff=word, number=num))
# prints "hi and 6"

# positional
print("{1} is a value, so is {0}".format(word, num))

# 3 f-strings
# best
word = "hi"
num = 6
print(f"{word} and {num}")

# String arithmetic

a = "a"
b = "b"
an = "an"

print(b + an)
print(b + a*7)
print(b + an*2 + a)

print("$1" + ",000"*3)

# String indexing

print("Spaghetti"[0])  # S
print("Spaghetti"[4])  # h

# Negative indexing works too

print("Spaghetti"[-1])
print("Spaghetti"[-4])

# String indexing Indexing with ranges: 
# the start value is inclusive, 
# the end value is skipped

# indexing with ranges
print("Spaghetti"[1:4])   # pag
print("Spaghetti"[4:-1])  # hett
print("Spaghetti"[4:4])   # (empty string)
print("Spaghetti"[:4])    # Spag
print("Spaghetti"[:-1])
print("Spaghetti"[1:])
print("Spaghetti"[-4:])

'''
Out of range values will through errors
if you try to access the single value, 
but they are valid as part of a range.
'''

print("Spaghetti"[15])     # IndexError: string index out of range
print("Spaghetti"[-15])    # IndexError: string index out of range
print("Spaghetti"[:15])    # Spaghetti
print("Spaghetti"[15:])    # (empty string)
print("Spaghetti"[-15:])   # Spaghetti
print("Spaghetti"[:-15])
print("Spaghetti"[15:20])


# String methods : .index()

# .index() returns the index of the first 
# occurrence of the specified value

print("kiwi".index("k"))  # 0
print("kiwi".index("m"))  # ValueError: substring not found

# String methods : .count()
# .count() returns the number of occurrences

print("kiwi".count("k"))  # 1
print("kiwi".count("i"))  # 2
print("kiwi".count("m"))  # 0

''' String methods : .split()
Returns a list of substrings 
separated by the passed in charecter or string
if no charecter or string is passed in
a space is used'''

print("Hello World".split())     # ["Hello", "World"]
print("Hello World".split(" "))  # ["Hello", "World"]
print("i-am-a-dog".split("-"))   # ["i", "am", "a", "dog"]

# String methods : .join()
# .join() takes a list of strings and
# returns a string with the elements joined

# Kind of reverse to how join is used in JS
# first you do "something".join(list)

print(" ".join(["Hello", "World"]))       # "Hello World"
# ["Hello", "World"].join(" ") JavaScript
print("-".join(["i", "am", "a", "dog"]))  # "i-am-a-dog"

# String methods : .upper() and .lower()
# .upper() and .lower() return a copy of the string
# with all the charecters in upper or lower case
# These functions do not change the original string

a = 'Hello'
print(a)          # 'Hello'
print(a.upper())  # 'HELLO'
print(a)          # 'Hello'



