
class tutorial:
    'Optional class documentation string' # Can be accessed via tutorial.__doc__.
    #class_suite
    pass

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: " + self.name + ", Salary: " + str(self.salary))

# Creating instance objects of class
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 4000)
emp3 = Employee("Mufasa", 7500)
emp4 = Employee("HAnsu", 5600)

#Access attributes
emp1.displayEmployee()
emp2.displayEmployee()

#Functions to use for attributes
print("Has attr before set", hasattr(emp1, 'age'))
setattr(emp1, 'age', 8)
print("Get attr after set" , getattr(emp1, 'age'))
delattr(emp1, 'age')

#Modify attributes
emp1.age = 7
emp1.age = 8
del emp1.age
print("Check if age exist after delete: ",hasattr(emp1, 'age'))

#Use function from a class
print("Total Employee count: %d" % Employee.empCount)

#Built-in Class attributes
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
#print("Employee.__module__:", Employee.__module__)
#print("Employee.__bases__:", Employee.__bases__)
#print("Employee.__dict__:", Employee.__dict__)

#Python garbade collection
#Instances of classes are deleted out of memory once their reference count reaches zero.

a = 40      # Create object <40>
b = a       # Increase ref. count  of <40>
c = [b]     # Increase ref. count  of <40>

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40>
c[0] = -1   # Decrease ref. count  of <40>

#However, a class can use the __del__() method,  a destructor, that is invoked when the instance is about to be destroyed.

class Point:
    def __init( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name +  " destroyed")
pt1 = Point()
pt2 = pt1
pt3 = pt1
print("pt1 id: ",id(pt1), "pt2 id:" ,id(pt2),"pt3 id:",id(pt3))
del pt1
del pt2
del pt3

#Note: Ideally you should define your classes in a separate file and then import them in your main program using import statement.

print("--- INHHERITANCE ---")

#Class inheritance
#A class can derive from another class, and also override methods.

class Parent:
    parentAttr = 100
    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def myMethod(self):
        print("Calling parent myMethod")

    def getAttr(self):
        print("Parent attribute: ",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")

    def myMethod(self):
        print("Calling child Mymethod overrided")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
print("Is Child a subclass of Parent: ", issubclass(Child, Parent))
c.myMethod()

print("Overloading operators")
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print("Overloading the add function!")
print(v1+v2)

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#print(counter.__secretCount) < -- Hidden!
