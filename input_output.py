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
my_file = open("text.txt", "r")

# If you open a file and call .readline() on the file object, 
# you'll get the first line of the file; 
# subsequent calls to .readline() will return successive lines.
print my_file.readline()
print my_file.readline()
print my_file.readline()

"""

Python doesn't flush the buffer—that is, write data to the 
file—until it's sure you're done writing. One way to do this 
is to close the file. If you write to a file without closing, 
the data won't make it to the target file.

"""
my_file.close()

# Buffering Data
# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")
# Write to the file
write_file.write("Not closing files is VERY BAD.")

# Try to read from the file
print read_file.read()

write_file.close()
read_file.close()

# The 'with' and 'as' Keywords
# with open("file", "mode") as variable:
    # Read or write to the file

with open("text.txt", "w") as textfile:
  textfile.write("Success!")

# Try it Yourself
with open("text.txt", "w") as my_file:
    my_file.write("South Park is ridiculous!")

# Case Closed
with open("text.txt", "w") as my_file:
    my_file.write("South Park is ridiculous!")
    if not my_file.closed:
        my_file.close()
        print my_file.closed