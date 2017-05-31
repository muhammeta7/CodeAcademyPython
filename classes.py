# Intoduction to Classes
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

# Class syntax
# Use the class keyword, name of class, and inheritance in ()
# def __init__(self) initializes object
class Animal(object):
     def __init__(self, name):
        self.name = name

# Instantiating Your First Object
class Animal(object):
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
print zebra.name

# More on __init__() and self
# Class definition
class Animal(object):
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry

# Class Scope
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

# is_alive initialized within class object
print zebra.name, zebra.age, zebra.is_alive 
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

# A Methodical Approach
class Animal(object):
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Fluffy", 13)
hippo.description()

# They're Multiplying
class Animal(object):
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age
        
hippo = Animal("Fluffy", 13)
hippo.description()

sloth = Animal("Flash", 3)
ocelot = Animal("Jack", 2)

print hippo.health
print sloth.health
print ocelot.health

# It's Not all Animals and Fruits
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Moe")
my_cart.add_item("salmon", 7)

print my_cart

# Warning: Here Be Dragons
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()

# Inheritance Syntax
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
       self.side1 = side1
       self.side2 = side2
       self.side3 = side3

# Override 
# Example
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name

class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def __init__(self, hours):
        self.hours = hours
        return hours * 12

# This Looks Like a Job For
"""

class Derived(Base):
   def m(self):
       return super(Derived, self).m()

m() is a method from the base class

"""

class Employee(object): 
    def __init__(self, employee_name):
            self.employee_name = employee_name

    def calculate_wage(self, hours):
            self.hours = hours
            return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
            self.hours = hours 
            return hours * 12.00
            
    # You can directly access attributes or methods
    # of a superclass(Parent) by using super() 
    def full_time_wage(self, hours): 
            return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("milton")
print milton.full_time_wage(4)

# Class Basics
class Triangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    # Check angles to determine if actual Triangle
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

# Inheritance
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        print "This is a %s %s with %s MPG." %(self.color, self.model, str(self.mpg)) 
        
    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg   = mpg   
        self.battery_type = battery_type
        
    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
my_car.drive_car()
print my_car.condition