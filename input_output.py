# File Input/Output

# See it ti Believe It
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

# f is file object and w stands for write
f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

# The open() Function
# r+ allows you to read and write
my_file = open("output.txt", "r+")

# Writing
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")
    
my_file.close()

# Reading use "r" as second argument
my_file = open("output.txt", "r")

print my_file.read()
my_file.close()

# Reading Between the Lines
