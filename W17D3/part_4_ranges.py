'''
Ranges
    An immutable sequence of numbers in order
    Arguments:
        start (default 0)
        stop (required)
        step (default 1)
    Can go in forward or reverse order
    Range is exclusive(the stop argument is not included in the returned list)
'''

numbers_range = range(10)
print(numbers_range) # range(0, 10)
# How can we make this a list?

starting_at_one = range(1, 11) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(starting_at_one) # range(1, 11)
print(list(starting_at_one)) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Reverse Ranges

reversed_maybe = range(51, 5) 
print(reversed_maybe) # range(51, 5)
print(list(reversed_maybe)) # []

reversed = range(51, 5, -1)  # 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5
print(list(reversed)) # [51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5]


'''
Iterating over Sequences with For Loops:
    for keyword to start the loop
    in iterates over each element in the sequence
    We do not need to define an iterator variable!
'''

items = ['a', 'b', 'c']

for item in items:
    print(item)

# range gives us access to both the 
# current element and its index in the list
for i in range(len(items)):
    print(i, items[i])


for i in range(1, 10, 2):
    print(i)

'''
Iterating over Collections with enumerate():
    The built-in function enumerate() 
    gives us both an item and its index in a sequence/iterator.

    enumerate() takes in a sequence and returns an enumerate object.

    This object can be typecast as a sequence of tuples, 
    where each tuple contains both an element and its index in a sequence/iterator.
'''

items = ['a', 'b', 'c']

enumerated_items = enumerate(items)
print(enumerated_items)

enumerated_list = list(enumerated_items)
print(enumerated_list)

for i, element in enumerated_list:
    print(i, element)

# short version 
for i, element in enumerate(items):
    print(i, element)


