'''
Tuples
Tuples are an ordered, immutable collection type.
They are defined using parentheses (), with values separated by a comma.
'''

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = ('a', 'b', 'c', 'd', 'e')
c = 10, 20, 30

print(a)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(b)  # ('a', 'b', 'c', 'd', 'e')
print(c)  # (10, 20, 30)

'''
Tuples are immutable [1/2]
You cannot append, remove, or sort the tuple in place.
We can concatenate tuples together, but the result will be an entirely new tuple
'''

tup = ("tall", "wide")
tup = ("small", "narrow")  # no error, this works
print(tup)                 # ("small", "narrow")
tup += ("tall", "wide")    # no error, this works
print(tup)                 # ("small", "narrow", "tall", "wide"

'''
Tuples are immutable [2/2]
Mutable items in a tuple can be mutated:
'''

tup = ([1, 2, 3], "hello")
print(tup[0])  # [1, 2, 3]
tup[0].append(4)
print(tup[0])  # [1, 2, 3, 4]
print(tup)     # ([1, 2, 3, 4], "hello")

'''
Sorting
The sorted() function works on tuples, 
just like lists. This will return a list by default.
'''
fruits = ("banana", "apple", "kiwi")
print(sorted(fruits))  # ['apple', 'banana', 'kiwi']
sorted_fruits = tuple(sorted(fruits))
print(sorted_fruits) # ('apple', 'banana', 'kiwi')
print(fruits)       # ('banana', 'apple', 'kiwi')

'''
Returning tuples
Using a comma in your return statement will return a tuple
You can store the tuple in one variable or destructure the 
tuples values into multiple variables.
'''

def min_max(numbers):
    return min(numbers), max(numbers)

values = (14, 2, -2, 3.3, -8, -25, 9, 0)

low_and_high = min_max(values)
print(low_and_high)  # (-25, 14)

lowest, highest = min_max(values)
print(lowest)        # -25
print(highest)       # 14

'''
Singleton tuples
Since parentheses are also used for grouping,
python won’t interpret a single like you might expect.
'''

hopefully_a_tuple = (5)
print(hopefully_a_tuple)  # 5
# whoops! not a tuple

'''
You need to use a comma so that python can recognize that a tuple is present.
'''

hopefully_a_tuple = (5,)
print(hopefully_a_tuple)  # (5,)
# nice, that is a tuple
also_a_tuple= 5,
print(also_a_tuple) # (5,)
# awesome, that is also a tuple

'''
Tuples vs. Lists: which is better?
As always, it depends!

Tuples are:
    Immutable
    Hashable
    More memory efficient than a list

Lists are:
    More familiar
    Mutable and dynamic
'''

