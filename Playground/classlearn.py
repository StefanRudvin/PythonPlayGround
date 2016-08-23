"""RPG TEST GAME."""


class student:
    """Student class __class__."""

    static_variable = 1

    def __init__(self, n, a):
        """RPG TEST GAME."""
        self.full_name = n
        self.age = a

    def get_age(self):
        """RPG TEST GAME."""
        return self.age


class Cs_student(student):
    """extending student Cs_student."""

    def __init__(self, n, a, s):
        """Cs student init."""
        student.__init__(self, n, a)  # Call init for student
        self.section_num = s

    def get_age():
        print("Age: " + str(self.age))

    def __repr__(self):
        """String print."""
        return "My name is: " + self.full_name

f = student("fuckme", 25)

f.full_name

y = f.get_age()

print(y)

woohoo = getattr(f, "full_name")

print(woohoo)

fuckmess = getattr(f, "age")

print(fuckmess)

print(f.__doc__)

# Non method data stored by objects are called attributes
# Data attributes: Variable owned by a particular instance of the class.
# Class attributes: Owned by the class as a whole, all class instances share the same value for it.
# These are called static variables in some languages.
# Good for class wide constants and building counter how many instances of the class have been made.

# Data attributes are initialized with:
# __init__() method

# As all instances change class attributes, if any instance changes it, the value is changed for all instances.

# Class attributes are defines within a class definition and outside of any method.

# Class attributes are accessed with: self.___class___.name notation

# Classes can extend the definition of other classes. Use and extension of methods and attributes.
# To define a subclass, put the name of the superclass in the parentheses when making the class. E.g.
# Class cs_student(student):
# Python does not use extends words

# Multiple inheritance: Python has two classes, old and new
# Old style classes use depth first, left-to-right access
# New classes use dynamic, more complex dynamic approach

# To redefine a method of the parent class, include a new definition using the same name in the subclass. The old code won't get executed.

# To execute the method in the parent class in addition to new code for some method, explicitly call the parents version of method.

# parentClass.methodName(self, a, b, c) ie. change the method.

# super() avoids referring to parent class explicitly.

# To call a function that is not included in a class, use:
# student.stefan = staticmethod(student_grade)

# The parents __init__ method is executed in addition to new commands. ie. parentClass.__init__(self, x, y)

# Classes contain methods and attributes that are always included.
# Most define functionality triggered by special operators or usage of that class.

# Special methods: __repr__ specifies how to turn an instance of the class into a string.

# print f can call repr to produce a string for object f

# typing f at the REPL prompt calls __repr__ to determine what to display as output.

# __init__ = Constuctor of the class
# __cmp__ = Define how == works for class
# __len__ = Define how len (obj) works
# __copy__ = Define how to copy a class

# These attributes exist for all classes:
# __doc__ = variable for documentation string for class
# __class__ = Variable which gives you a reference to the class from any instance of it.
# __module__ = Variable which gives reference to the module in which the particular class is defined.
# __dict__ = Dictionary that is the namespace for a class.

# Useful: dir(x) returns a list of all methods and attributes defined for object x.

# Any attribute/method with two underscores in it's name(not at the end) is private and can't be accessed outside of the class.
# Two underscores in the begginning or end are for built-in mehotds or attributes.

# There is no 'protected' status in Python, so subclasses are unable to access this private data.
