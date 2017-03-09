# To create a variable to store data simply set it equal to the value you wish to store

# Variable for numerical amount
my_variable = 10

# Variable to store boolean value
boolean_variable = False

# Proper indentation is important in python
def spam():
    eggs = 12
    return eggs
        
print spam()

# Multi-line comments
""" You simply use three quotations marks """

# Math operators
addition = 25 + 30
subtraction = 100 - 25
multiplication = 8 * 9
division = 90 / 9
exponent = 10 ** 2 # 10 to the power of 2
modulo = 6 % 5 # Should return remainder of 1


# Tip Calcultor
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)