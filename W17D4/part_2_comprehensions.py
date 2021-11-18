'''
Comprehensions
Comprehensions are composed of an expression followed by a for...in statement,
followed by an optional if clause. 
They can be used to create new lists (or other mutable sequence types).
'''

iterable = [1,2,3,4,5,6,7,8,9,10]

my_list = [member *2  for member in iterable] # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# with optional if statement
my_list = [member *2 for member in iterable if member < 5] # [2, 4]

# Copying a list
# With a for loop:

my_list = [1, "2", "three", True, None]
my_list_copy = []
#     for loop
#    ----------
# /               \
for item in my_list:
    my_list_copy.append(item)
#                        |
#                       var
print(my_list_copy)  # [1, '2', 'three', True, None]

#Copying a list
#With a list comprehension:

my_list = [1, "2", "three", True, None]
#              var         for loop
#               |        -------------
#               |      /              \
my_list_copy = [item for item in my_list]

print(my_list_copy)  # [1, '2', 'three', True, None]

'''
Mapping over a list with comprehensions
Include the desired expression before the for statement
'''

my_list = ["jerry", "MARY", "carrie", "larry"]
#          expression            for loop
#               |               -------------
#               |             /              \
mapped_list = [item.lower() for item in my_list]

print(mapped_list)  # ['jerry', 'mary', 'carrie', 'larry']

#Convert map() to list comprehension

nums = [-5, 11, 10, 14]
mapped_nums = map(lambda num: num * 2 + 1, nums)

print(list(mapped_nums))  # [-9, 23, 21, 29]

nums = [-5, 11, 10, 14]
# mapped_nums = map(lambda num: num * 2 +1, nums)
mapped_nums = [num * 2 + 1 for num in nums]

print(mapped_nums)  # [-9, 23, 21, 29]

#Filtering a list with comprehensions

nums = [-5, 11, 10, 14]

filtered_nums = filter(lambda num: num > 0, nums)

print(list(filtered_nums))  # [11, 10, 14]

nums = [-5, 11, 10, 14]

# filtered_nums = filter(lambda num: num > 0, nums)
filtered_nums = [num for num in nums if num > 0]

print(filtered_nums)  # [11, 10, 14]

#Nested loops
#Nested for loop:

letters = ["a", "b", "c"]
nums = [1, 2]

new_list = []

#  outer loop
#  ----------
# /          \
for l in letters:
    for n in nums:  # <- inner loop
        new_list.append((l, n))
#                        \   /
#                         ---
#                      expression

print(new_list)  # [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]

'''
Nested loops (list comprehension)
With list comprehension—note that the outer loop is first:
'''

letters = ["a", "b", "c"]
nums = [1, 2]
#       expression    outer loop     inner loop
#            ---    --------------   -----------
#           /   \  /              \ /           \
new_list = [(l, n) for l in letters for n in nums]

print(new_list)  # [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]

'''
Dictionary comprehensions
Use a colon in the expression to separate the key and value.
'''

# a dictionary that maps numbers to the square of the number
number_dict = {num: num**2 for num in range(5)}
print(number_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}