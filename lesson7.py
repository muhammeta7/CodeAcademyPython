# Print second element in list
n = [1, 3, 5]

print n[1]

# List element modification
n = [1, 3, 5]

n[1]=n[1]*5
print n

# Append to a list
n = [1, 3, 5]

n.append(4)
print n

# Removing elements from list
# Use .pop() which will return item at index, .remove() or del()
n = [1, 3, 5]

del(n[0])
print n

# Function to return 3* parameter
number = 5
def my_function(x):
    return x * 3

print my_function(number)

# Function with multiple arguments
m = 5
n = 13
def add_function(m,n):
    return m+n

print add_function(m, n)

# Strings in functions
n = "Hello"
def string_function(s):
    return s+"world"

print string_function(n)

# Passing a list into a function
def list_function(x):
    return x

n = [3, 5, 7]
print list_function(n)

# Modify element of list in a function
def list_function(x):
    x[1]= x[1]+3
    return x

n = [3, 5, 7]
print list_function(n)

# List manipulation in functions
n = [3, 5, 7]

def list_extender(list):
    list.append(9)
    return list

print list_extender(n)

# Printing out list item by item in a function
n = [3, 5, 7]
  
def print_list(x):
    for i in range(0, len(x)):
        print x[i]
   
print_list(n)

# Modify each element in a list in a function
n = [3, 5, 7]

for i in range(0, len(n)):
    n[i] = n[i] * 2

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
          
    return x
        
print double_list(n)

# ------------------------------------------------------------------------------------

""" Understanding ranges:
    01.) range(stop) so range(6) would return [0,1,2,3,4,5]
    02.) range(start,stop) so range(1,6) would return [1,2,3,4,5]
    03.) range(start,stop,step) so range(1,6,3) would return [1,4]
"""

# Passing a range into a function
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3))

# Iterating over a list in a function
n = [3, 5, 7]

def total(numbers):
    result=0
    for i in range(len(numbers)):
        result += numbers[i]
        
    return result
        
print total(n)

# Using strings in lists in functions
n = ["Michael", "Lieberman"]

def join_strings(words):
    result=""
    for i in range(len(words)):
        result=result+words[i]
        
    return result
    
print join_strings(n)