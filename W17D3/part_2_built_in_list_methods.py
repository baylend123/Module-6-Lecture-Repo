'''
List methods:
    Use append to add items to the end of a list (like push in JavaScript).
    This mutates the list.
'''

fruits = ["banana", "apple", "kiwi"]

fruits.append("apple")
print(fruits)  # ["banana", "apple", "kiwi", "apple"]

'''
Use remove to delete the first instance of a given value.
(Also mutates the list).
'''

fruits.remove("apple")
print(fruits)  # ["banana", "kiwi", "apple"]

# Error if value is not present in list
fruits.remove("mango") # ValueError: list.remove(x): x not in list

# Link to the Python documentation: https://docs.python.org/3/tutorial/datastructures.html

'''
Sorting lists:
    The .sort() method will sort a list, mutating the list
'''

fruits = ["mango", "banana", "apple", "kiwi"]
fruits.sort()
print(fruits)  # ["apple", "banana", "kiwi", "mango"]

'''
Sorting lists (custom sort):
    You can provide a key to change how the list is sorted

    the key is a function that takes a single
    argument and returns a key to use for sorting
    rather than sort the list values directly,
    the sort will apply the key function to each value and sort based on the resulting value
    this will not mutate the values in the list (just the order), 
    it will just use the calculated values in the comparisons
'''

names = ["JAMES", "julie", "Ana", "Ria"]
names.sort()
print(names)
# ensure a case-insensitive sort with the `.lower` string method
names.sort(key=str.lower)
print(names)

'''
Sorting, continued:
    The sorted() function can be used to sort lists without mutating. 
    It also works with other iterable types (e.g. tuples).
'''
fruits = ["mango", "banana", "apple", "kiwi"]
sorted_fruits = sorted(fruits)
reversed_fruits = sorted(fruits, reverse=True)
print(sorted_fruits)   # ['apple', 'banana', 'kiwi', 'mango']
print(reversed_fruits) # ['mango', 'kiwi', 'banana', 'apple']
print(fruits)         # ['mango', 'banana', 'apple', 'kiwi']

'''
note that the parameters
key and reverse work with both .sort() and sorted()
'''

'''
Sorting lists (fun fact)
Sorting in Python uses Timsort. (The inventor’s name is Tim. Really.)
https://en.wikipedia.org/wiki/Timsort
It is based on a combination of merge sort and insertion sort.
'''

'''
More built-in functions
sum(), min(), max(), can be used to compute values over lists.
'''

values = [49, 22, 13, 25]
print(values)       # [49, 22, 13, 25]

total_value = sum(values)
print(total_value)  # 109

top_value = max(values)
print(top_value)    # 49

min_value = min(values)
print(min_value)    # 13

avg_val = sum(values)/len(values)
print(avg_val)     # 27.25

