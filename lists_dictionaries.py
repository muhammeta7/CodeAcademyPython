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

