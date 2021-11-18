'''
Built-in functions: all()
    all() returns True if all items in a collection are truthy.

    It returns False if there is at least one falsey item

'''
test1 = {"item", "truthy", ""}
test2 = []
test3 = [[]]
print(all(test1), test1)  # False {"", "truthy", "item"}
print(all(test2), test2)  # True []
print(all(test3), test3)  # False [[]]

'''
Built-in functions: any()
    any() returns True if there are any truthy items in the provided collection.

    It returns False if there are no truthy items.
'''

test1 = ["item", [], []]
test2 = []
test3 = [[]]
print(any(test1), test1)  # True ['item', [], []]
print(any(test2), test2)  # False []
print(any(test3), test3)  # False [[]]

'''
Built-in functions: filter()

    filter() takes in a function and an iterable as arguments and returns a filter object.

        The returned collection includes only the items which, 
        when the function parameter was applied to them, returned a truthy value.

        filter() does not filter in place. It returns an entirely new object.
'''

def is_a(num):
    if num >= 90:
        return True
    else:
        return False


scores = [90, 86, 75, 91, 62, 99, 88, 90]
only_as = filter(is_a, scores)  # does not mutate original
print(only_as)                  # <filter object at 0x10546ad30>
print(list(only_as))            # [90, 91, 99, 90]

'''
filter’s function parameter can also be defined in line as a lambda function.
'''

scores = [90, 86, 75, 91, 62, 99, 88, 90]
only_as = filter(lambda num: num >= 90, scores)
print(only_as)        # <filter object at 0x10546ad30>
print(list(only_as))  # [90, 91, 99, 90]

'''
Built-in functions: map():
    map() takes in a function and an iterable as arguments and returns a map object.

    map() transforms each value from the original iterable according to the provided
    function and returns them in a new object.
'''

def get_grade(num):
    if (num >= 90):
        return "A"
    elif (num <90 and num >= 80):
        return "B"
    elif (num < 80 and num >= 70):
        return "C"
    elif (num < 70 and num >= 60):
        return "D"
    else:
        return "F"
scores = [90, 86, 75, 91, 62, 99, 88, 90]
print(map(get_grade, scores))  # <map object at 0x106faffa0>
grades = list(map(get_grade, scores))
print(grades)                  # ['A', 'B', 'C', 'A', 'D', 'A', 'B', 'A']


'''
Built-in functions: zip()
zip() takes two iterables as arguments and returns a zip object that pairs
values at corresponding indices.

You can typecast the zip object as a sequence of tuples or as a dictionary.
'''

scores = [90, 86, 75, 91, 62, 99, 88, 90]
grades = ["A", "B", "C", "A", "D", "A", "B", "A"]
combined = zip(scores, grades)
combined_list = list(combined)
combined_dict = dict(combined_list)
print(combined)       # <zip object at 0x1023a9600>
print(combined_list)  # [(90, 'A'), (86, 'B'), (75, 'C'), (91, 'A'), (62, 'D'), (99, 'A'), (88, 'B'), (90, 'A')]
print(combined_dict)  # {90: 'A', 86: 'B', 75: 'C', 91: 'A', 62: 'D', 99: 'A', 88: 'B'}

