"""
Lists are a datatype to store collection of information.
Can include strings, numbers, booleans
Similar to arrays in JS
"""

# You can access individual items by its index
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2] # 5 + 7
print "Adding the numbers at indices 1 and 3..."
print numbers[1]+numbers[3] # 6 + 8

# Simply set the index to a new value to change item in list
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
zoo_animals[2] = "hyena"
zoo_animals[3] = "cheetah"
print zoo_animals

# To add new items to a list use .append 
suitcase = [] 
suitcase.append("sunglasses")
suitcase.append("shirt")
suitcase.append("pants")
suitcase.append("shoes")

list_length = len(suitcase) # Length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# List slicing: to access portion of list
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)
print first # returns ['sunglasses' , 'hat']
print middle # returns ['passport' , 'laptop']
print last # returns ['suit', 'shoes']

## Slicing strings 
animals = "catdogfrog"
cat  = animals[0:3] 
dog  = animals[3:6]            
frog = animals[6:10]           

print cat
print dog
print frog

# Using .index to find index of specific list item
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"
print duck_index
animals.insert(duck_index,"cobra") # Use insert to add "cobra" to index 2 
print animals # ['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox']

#----------------------------------------------------------------------------

# Introduction to For Loops to iterate through a list
for variable in list_name:
  # Do stuff


# Example where it doubles each value in list
my_list = [1,9,3,8,5,7]
for number in my_list:
  print 2*number # will print 2, 18, 6, 16, 10, 14

# You can use the .sort() helper to clean up your mess
animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
    print animal # will return ant bat cat

# Loop that iterates over start_list & appends to squared_list 
start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    square_list.append(x**2)
    square_list.sort() # Returns squared list from leat to greatest

# Removing items from a list
list_name.remove(item)



# -------------------------------------------------------------------------

# Intro to key value pairs ( dictionary )
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Sloth'] # Will return 105

# Inputting a new entry to a dictionary
 menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 
print menu['Chicken Alfredo']

menu['Spam']=2.50
menu['Apples']=1.00
menu['Steak']=11.00

print "There are " + str(len(menu)) + " items on the menu." # 4 items
print menu

# Items can be removed from a dictionary using the 'del' command
del dict_name[key_name]

# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

# Removing the 'Unicorn' entry.
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']

zoo_animals['Rockhopper Penguin']='Something Else'

print zoo_animals

# ------------------------------------------------------------------------------

# Dictionary Review
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
inventory['pocket']=['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']=550

print inventory

# -----------------------------------------------------------------------------------

# BeFOR we Begin
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for item in names:
    print item

# Major KEY
webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print webster[key]

# For Loop to print only even numbers in a list
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a:
    if item%2 ==0:
        print a[item]

# Fizz count function with for loop
def fizz_count(x):
     count = 0 # initialize count
     for item in x:
         if item=="fizz":
             count= count+1 # increment count
             
     return count

print fizz_count(["fizz", "cat", "fizz"])

# String Looping
for letter in "Codecademy":
    print letter # will return each letter in string
    
print # Empty lines to make the output pretty
print 

word = "Programming is fun!"

for letter in word:
    if letter == "i": # Will print out any instances of the letter i
        print letter

# -----------------------------------------------------------------------------

# A Day at the SuperMarket
prices = {
    "banana":4,
    "apple":2,
    "orange":1.5,
    "pear":3
}

stock = {
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15
}

total = 0 # initialize total
for key in prices:
    print key
    print "price: %s" %prices[key]
    print "stock: %s" %stock[key]
    total += prices[key]*stock[key] 

print total # will print total amount of all stock

# Create shopping list and make function to compute_bill

shopping_list = ["banana", "orange", "apple"]

def compute_bill(food):
    total=0
    for item in food:
      if stock[item] > 0:
        total=total+prices[item]
        stock[item] -= 1 # decrement stock when someone purchases item
        
    return total

print compute_bill(shopping_list)
print stock

