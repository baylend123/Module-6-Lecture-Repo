'''
Dictionaries:
    Dictionaries are ordered and mutable.
    They consist of pairs of keys and values.
        The keys must be “hashable” (immutable) values
        e.g. keys can be strings, numbers, tuples, booleans, but not lists or dictionaries
    Dictionaries use curly braces, similar to JavaScript objects, although keys do not 
    have to be strings.
        but if the keys are strings, they must use quotes, unlike JS
'''

'''
What’s Hashable?
Hashing allows Python to quickly access elements in collections via their hash values.

In Python, all immutable objects are hashable. We know that accessing that object
by its hash will always give us the same exact object.

While dictionaries themselves and each value within them are mutable, the keys must be hashable.
'''

a = {'one':1, 'two':2, 'three':3}
b = dict(one=1, two=2, three=3)
print(b)  # {'one': 1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
print(c)  # {'one': 1, 'two': 2, 'three': 3}
print(a == b == c)   # True

'''
Using [] and .get() to index into a Dictionary
******Unlike javascript in Python you cannot index into a dictionary with dot notation
******Remeber this, as there will definitly come a time when you try to dot into 
******a dictionary and you will get an error.
'''

my_dict = {'one':1, 'two':2, 'three':3}
print(my_dict.one) #AttributeError: 'dict' object has no attribute 'one'
print(my_dict['one']) #1
print(my_dict['new']) # KeyError: 'new'
print(my_dict.get('one', None))  # 1
print(my_dict.get('banana', "Nope!")) # Nope!


'''
Adding, Updating, Deleting Data in Dictionaries:
    del keyword to delete a key/value pair
    [] to add or update a key/value pair
'''

my_dict = {
    "word": "cooool",
    1: "one",
    False: 42,
    ("tuple", "keys"): ["lists", "can", "be", "values", "not", "keys"],
    None: {"key": "value"}
}

my_dict[1] = "two" # Updates value
print(my_dict[1]) # "two"
print(my_dict[False]) # 42
print(my_dict[("tuple", "keys")]) # ["lists", "can", "be", "values", "not", "keys"]
print(my_dict[None]) # {"key": "value"}
my_dict["new_key"] = "new_value" #Adds key/value
del my_dict["word"] # Deletes key/value
print(my_dict) # I promise, all the changes are there!

'''
Using in:
    in also allows you to check if a value exists in a sequence
    For dictionaries, it checks whether a value is a key in the dictionary
'''

print(1 in {1: "one", 2: "two"}) # True
print("1" in {1: "one", 2: "two"})  # False
print(4 in {1: "one", 2: "two"})    # False
print("one" in {1: "one", 2: "two"})    # False

'''
.items():
    .items() returns a list of tuples
    Each tuple contains the key/value pair of the item in the dictionary
'''

book = {
    'title': 'Goodnight Moon',
    'ratings': 7492,
    'stars': 4.8,
    'author': {'firstName': 'Margaret', 'lastName': 'Wise Brown'},
    'images': ['goodnight1.png', 'goodnight2.png'],
}
    
for key, value in book.items():
    print('key:', key, 'value:', value)

for key in book:
     print('key:', key, 'value:', book[key])

'''
.keys() and .values():
    .keys() returns a list of the keys in the dictionary
    .values() returns a list of the values in the dictionary
'''

book = {
    'title': 'Goodnight Moon',
    'ratings': 7492,
    'stars': 4.8,
    'author': {'firstName': 'Margaret', 'lastName': 'Wise Brown'},
    'images': ['goodnight1.png', 'goodnight2.png'],
}

for value in book.values():
    print('value:', value)

for key in book.keys():
    print('key:', key)



