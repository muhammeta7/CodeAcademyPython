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

# List Slicing Syntax
# [start:end:stride]
# start - describes where slice starts(inclusive)
# end - describes where slice ends(exclusive)
# stride - describes the space between itesm in the sliced list
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2] 

# Omitting Indices
my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2] # Will print [1,3,5,7,9]

# Reversing a List
my_list = range(1, 11)
backwards = my_list[::-1]
print backwards

# Stride Length
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

# Practice Makes Perfect
to_21 = range(1,22) # Prints numbers from 1 to 21 inclusive
odds = to_21[0:22:2] # Prints only odd numbers 
middle_third = to_21[7:14] # Prints from 8 to 14 inclusive

print to_21
print odds
print middle_third

# Anonymous Functions
my_list = range(16)
# filter uses lamda to determine what to filter
print filter(lambda x: x % 3 == 0, my_list)

# Lambda Syntax
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)

# Try It
squares = [x**2 for x in range(1,11)]
print filter(lambda x: x>=30 and x<=70 , squares)

# ===============================================================

# Iterating Over Dictionaries
movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print movies.items()

# Comprehending Comprehensions
threes_and_fives = [x for x in range(1,16) if x%3 ==0 or x%5 ==0]
print threes_and_fives # [3, 5, 6, 9, 10, 12, 15]

# List Slicing
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

# Lambda Expressions
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x!='X', garbled)
print message

# ====================================================================

# Bit-Wise Operators

# The Base 2 Number System
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print 0b111   #7
print 0b1000  #8
print 0b1001  #9
print 0b1010  #10
print 0b1011  #11
print 0b1100  #12
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

# The bin() function allows for representation of integer into string
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)

# The int() When given a string containing a number and the base that number is in, 
# the function will return the value of that number converted to base ten.
print int("0b11001001",2)

"""

# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

"""

# Slide Left and Slide Right
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left<< 2

print bin(shift_right)
print bin(shift_left)

"""

A BIT of This AND That

     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

"""

print bin(0b1110 & 0b101) # Prints 0b100



