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

  
