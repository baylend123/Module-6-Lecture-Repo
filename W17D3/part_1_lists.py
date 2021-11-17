'''
Lists are mutable,
ordered collections (like arrays in JavaScript). 
Use square brackets to make lists
'''

empty = []
print(empty)   # []


# Values are separated by commas.

fruits = ["banana", "apple", "kiwi"]
print(fruits)  # ["banana", "apple", "kiwi"]

'''
Indexing with lists:
    To get individual values:
        list_name[single_index]
'''

fruits = ["banana", "apple", "kiwi", "mango", "tangerine"]

print(fruits[1])   # apple
print(fruits[-1])  # tangerine

'''
Indexing with lists (ranges)
    To get a range of values:
'''

fruits = ["banana", "apple", "kiwi", "mango", "tangerine"]

# list_name[inclusive_start:exclusive_end]
print(fruits[1:4])
print(fruits[-1:])

# list_name[inclusive_start:exclusive_end:step_size]
print(fruits[::-1])
print(fruits[3::-1])

'''
Built-in functions (len()):
    We can use the len() function to get the length of lists.
'''

fruits = ["banana", "apple", "kiwi", "mango", "tangerine"]

print(len(fruits))       # 5
print(len(fruits[1:4]))  # 3

