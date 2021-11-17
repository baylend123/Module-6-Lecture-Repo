'''
Collecting Function Arguments:
    In JavaScript, we could use the spread/rest operator (...) 
    to collect a variable number of function arguments into an array.
'''

'''
// javascript example
const myHobbies = (name, ...args) => {
    console.log("name (first positional arg):", name)
    console.log("collected arguments:", args)
    return `${name}'s favorite hobbies are ${args.join(', ')}`
}
console.log(myHobbies("Mitchell", "swimming", "cycling", "making pizza", "BBQ"))
'''

'''
In Python, we can use the “splat” operator (*) 
and the “double-splat” operator (**) to do something similar.
'''

'''
Positional arguments
In Python, if we want to collect some variable number of anonymous positional arguments, 
we use the splat operator after all of the named positional arguments.

Note that the args will be collected into a tuple, not a list.
'''

def my_hobbies(name, *args):
    print("name (first positional arg):", name)
    print("collected positional args:", args)
    return f"{name}'s favorite hobbies are {', '.join(args)}"


print(my_hobbies("Mitchell", "swimming", "cycling", "making pizza", "BBQ"))
# name (first positional arg): Mitchell
# collected positional args: ('swimming', 'cycling', 'making pizza', 'BBQ')
# Mitchell's favorite hobbies are swimming, cycling, making pizza, BBQ

'''
Keyword Arguments
In addition to positional arguments (args), Python also has keyword arguments (kwargs). 
Anonymous keyword arguments can be collected using the ** operator.

Keyword arguments must follow all positional arguments, so the input order is always:

named_arguments, *args, named_keyword_args=value, **kwargs
The ** operator collects keyword arguments into a dictionary.
'''

def my_hobbies(name, *args, age=10, **kwargs):
    print("age (collected args):", age)
    print("collected kwargs:", kwargs)
    info_dict = {
        "hobbies": f"{name} favorite hobbies are {', '.join(args)}",
        "stats": {**kwargs, "age": age}
    }
    return info_dict


print(my_hobbies("Mitchell", "swimming", "cycling",
      "making pizza", "BBQ", age=30, height=60, glasses=False))