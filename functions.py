# def keyword and then the name of the function followed by any parameters the function requires

# Squared function
def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared) # %d is used for decimals instead of %s for strings
    return squared

square(10)

# Power function
def power(base, exponent): 
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)

# You can also call a function withing another function
def cube(number):
    return number**3
    
def by_three(number):
    if number%3 == 0:
        return cube(number)
    else:
        return False
               
print by_three(18)

# Importing math module
import math
print math.sqrt(25) # sqrt function within math moule

# This method just imports the sqrt function from math module
from math import sqrt
print sqrt(25)

# Import *everything* from the math module
from math import *
print sqrt(25) 

# math module built-in functions
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

#-----------------------------------------------------------------------

# Some functions are built in and don't need any imports
maximum = max(1,2,3,4,5,6,7)
print maximum # Will return biggest number in list

minimum = min(15,3,5,1,19)
print minimum # Will return smallest number in list

absolute = abs(-42)
print absolute # Absolute value of number

# Print out the types of an integer, a float, and a string on separate lines below.
print type (45) # <type 'int'>
print type(4.2222) # <type 'float'>
print type('spam') # <type 'str'>

#--------------------------------------------------------------------------

# Review Functions

# Shut down function
def shut_down(s):
    if s=="yes":
        return "Shutting down"
    elif s=="no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print shut_down("yes")

# Built-In functions
def distance_from_zero(arg):
    if type(arg) == int or type(arg) == float:
        return abs(arg)
    else:
        return "Nope"
             
print distance_from_zero(7.455)

#----------------------------------------------------------------------------

# Take a Vacation
def hotel_cost(nights):
    return 140 * nights
    
print hotel_cost(3)

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475

def rental_car_cost(days):
    cost = 40*days
    if days >= 7:
        return cost-50
    elif days >=3:
        return cost-20
    else:
        return cost
        
def trip_cost(city,days,spending_money):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+spending_money
        
print trip_cost("Los Angeles",5,600) # Parameters input for testing



