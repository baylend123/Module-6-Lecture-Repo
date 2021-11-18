'''
Classes
To create a class we use the class keyword, and by convention, 
we capitalize the names of classes.

Looks a lot like JavaScript
'''

# python example
class Widget:
    # more code to come
    # pass keword is used to create a class without any code
    pass

'''
Initializing classes
Generally speaking:

Python’s __init__() is like JavaScript’s constructor()
Python’s self is like JavaScript’s this
'''

# python example
class Widget:
    def __init__(self):
        # more code to follow
        # pass keword is used to create a class without any code
        pass

'''
the __init__() method
Python’s constructor method is called __init__().
'''

# python example
class Widget:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


'''
Instance variables and methods
You can set attributes on the instance with dot notation (self.some_attribute = value).

You can add methods to the class by defining functions and passing in self.
'''

class Widget:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

    def my_method(self, word):
        print(f"hello {word}")
        return

'''
Wait, what is self?
self refers to the instance that a method was called on.

Whenever you invoke a method on an instance of a class, 
it is as though you are invoking the class’s own method,
and passing in the instance as an argument.
'''

some_widget = Widget("blue", "square")
# both below do the same thing
some_widget.my_method("other argument")
Widget.my_method(some_widget, "some other argument")

'''
Wait, what is self?
Calling the first parameter self is a convention.

This is technically valid Python, and it would do the same 
thing as calling it self.
 But no one would write it this way.
'''

class Widget:
    def __init__(banana, color, shape):
        banana.color = color
        banana.shape = shape

'''
Instances of classes
We create instances of a class by invoking the class as though
it is a function (this invokes the class’s __init__() method)
'''

# in python
my_new_widget = Widget("blue", "circle")

'''
Inheritance
To inherit from another class, 
we pass a reference to that class as
an argument in the class definition.

We can use the super() function to get a 
reference to the parent class, 
then invoke the desired function.
'''

class Widget:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


class Gadget(Widget):
    def __init__(self, color, shape, noise):
        super().__init__(color, shape)
        self.noise = noise


thingie = Gadget("purple", "spiral", "whrrrrrr")
print(thingie)  # <__main__.Gadget object at 0x105103d60>
print(thingie.color, thingie.shape, thingie.noise)  # purple spiral whrrrrrr

'''
Getters and setters
Getters & setters allow us to have methods that behave like properties.

They provide a convenient interface for implementing more complicated 
logic necessary for setting a class property.

They can also be useful for protecting “private” values on your class.
'''

'''
Getters
A getter allows you to define a method that behaves like a property. 
The @property decorator over a method creates a getter.

While the getter is a function, it is invoked as if it were a property.
'''

class Widget():
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    
    @property
    def info(self):
        print("in the getter!")
        return f"{self.color} {self.shape}"
    
my_widget = Widget("blue", "square")
print(my_widget.color)

# call the getter method as if we were just
# accessing a property
print(my_widget.info)

'''
Setters
A setter allows you to define a method that updates the getter “property”. 
The decorator used to create a setter is @<getter_method_name>.setter.

You can have a standalone getter, but you must have a getter in order to have a setter. 
The setter method runs when you change the getter “property.”
'''

class Widget():
    def __init__(self, color, shape, pswd):
        self.color = color
        self.shape = shape
        
        # set initial ~secret~ password
        # this calls the setter method!
        self.my_password = pswd
    
    @property
    def info(self):
        print("in the getter")
        return f"{self.color} {self.shape}"
    
    # getter for ~secret~ password
    @property
    def my_password(self):
        return self._password

    # setter for ~secret~ password
    @my_password.setter
    def my_password(self, new_val):
        print("hashing password....")
        self._password =  str(new_val) + "12345" * 3
        
my_widget = Widget("blue", "square", "beepboop")
print(my_widget.my_password)

# call the setter method as if we were
# setting my_password as a regular property
my_widget.my_password = "new thing"
print(my_widget.my_password)

'''
“Private” properties
Python does not really have private attributes. 
All properties on a class can be accessed from outside the class/instance.

Getters and setters just help us indicate that certain properties should 
not be directly accessed in this way.

Conventionally, private properties are indicated with a single underscore 
followed by the property name:

self._password
'''

'''
Duck-Typing:
    “If it looks like a duck, and quacks like a duck, it must be a duck”

What does it mean for an object to “look/quack like a duck”?
    it has the relevent “magic method” that python uses to implement a given built-in 
    function (like len() or print())
What does it mean to “be a duck”?
    that means built-in functions will be able to work on classes that you create
Why is this good?
    duck-typing means that classes that you define can work as though 
    they are already part of python!
'''

'''
Duck-typing
Using duck-typing you can:

    have your class work with the addition operator (+)
    define what equality operator (==) means for your class
    loop over an instance of your class with for ... in
    and much more!
    duck-typing is powerful!
'''

'''
Duck-typing
The default value when you print a user-defined class 
instance is not typically very helpful…
'''

class Widget:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape

my_new_widget = Widget("blue", "circle")
print(my_new_widget)  # <__main__.Widget object at 0x1071cebb0>

'''
Duck-typing
You can use the __repr__ method that will let you control what gets printed for your class.
'''

class Widget:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape


    def __repr__(self):
        return f"Widget({self.color}, {self.shape})"

my_new_widget = Widget("blue", "circle")
print(my_new_widget)  # Widget(blue, circle)

