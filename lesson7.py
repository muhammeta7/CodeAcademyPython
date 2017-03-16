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