# Advanced Topics

# Iterators for Dictionaries
my_dict = {
    'name': 'Moe',
    "age" : 27,
    'sex' : 'male'
}

# items() prints key/value pairs in no particular order
print my_dict.items()
# Prints keys 
print my_dict.keys()
# Prints Values
print my_dict.values()
# Prints key then a space, and the value stored in that key
for key in my_dict:
    print key,my_dict[key]

# Building Lists
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

# List Comprehension Syntax
# This will create a new_list populated by the numbers one to five
new_list = [x for x in range(1,6)]

# If you want those numbers doubled, you could use
new_list = [x for x in range(1,6)]

# And if you only wanted the doubled numbers that are evenly divisible by three
doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]

# Makes a list of even sqaures that are even for range 1 to 11
even_squares = [x**2 for x in range(1,11) if (x**2)%2 == 0]
print even_squares

# Now you Try
cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4 == 0]
print cubes_by_four

