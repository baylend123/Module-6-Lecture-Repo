'''
Sets
Sets are mutable, unordered collections where all elements are unique.

Sets use curly braces, like a dictionary. You can create an empty set with set().

While sets can be mutated, the individual elements must be immutable types.
'''

print(set([[1,2,3],2,3])) # TypeError: unhashable type: 'list'

not_an_empty_set = {}
print(type(not_an_empty_set))

empty_set = set()
print(type(empty_set))

set_with_elements = {1, "hello", None}
print(set_with_elements)

ones = {1, 1, 1}
print(ones)

'''
Creating sets from other iterables
You can use the set() function to create new sets from other iterable types.
'''

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list))    # {1, 2, 3, 4, 5}
my_string = "hello"
print(set(my_string))  # {'l', 'h', 'o', 'e'}
my_tuple = (1, 1, 1)
print(set(my_tuple))   # {1}
my_dict = {"hello": "value", "goodbye": "value"}
print(set(my_dict))    # {'goodbye', 'hello'}

'''
Union (a | b)
All elements in a and b (or in both)
'''

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)       # {1, 2, 3, 4, 5}
print(a.union(b))  # {1, 2, 3, 4, 5}
# Python _-_-_->
print(max(list(a | b))) # 5
# order of a and b does not matter

'''
Set operations
Intersection (a & b)
Only elements in both a and b
'''

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)              # {3}
print(a.intersection(b))  # {3}
# order of a and b does not matter

'''
Code from “Combining Data Structures”
'''

# posts is a list of dictionaries, some of the values in that list
posts = [
    {
        "title": "All About Lists",
        "tags": ("fun", "informative", "lists")
    },
    {
        "title": "Tuple Trouble",
        "tags": ("fun", "tuples")
    },
    {
        "title": "Sparkling Sets",
        "tags": ("informative", "numbers")
    },
]

all_tags = []  # list to hold all tags
for i in range(len(posts)):
    print(posts[i]["tags"])
    all_tags.extend(posts[i]["tags"])

print(all_tags)
print(set(all_tags))
all_tags = list(set(all_tags))
all_tags.sort()
print(all_tags)

'''
Code example from “Stack and Queue Overview”
Interuption stack
'''

teller = []

teller.append("Greet Customer")
print(teller)
teller.pop()
print(teller)
teller.append("Process Deposit")
print(teller)
teller.append("Phone Ringing")
print(teller)
teller.pop()
teller.append("Greet Caller, Listen, Answer Question")
print(teller)
teller.pop()
print(teller)
teller.pop()
print(teller)

'''
Code example from “Stack and Queue Overview”
Processing queue
'''

processor = []
processor.append({'type':'page','path':'','header':[],'cookies':[]}),
processor.append({'type':'api', 'function':'', 'parameters':[]})
processor.append({'email':'email','address':'bob@gmail.com','subject':''})
print("PROCESSOR LIST", processor)

for i in range(len(processor)):
    item = processor.pop(0)
    print("PROCESSING ITEM", item)
    print("REMAINING LIST", processor)


