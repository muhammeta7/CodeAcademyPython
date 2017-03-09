# Create a string by surrounding it with quotes
string = "Hello there "

# For words with apostrophe's us a backslash \
print "There isn\'t flying, this is falling with style!"

# Accesing by index 
print fifth_letter = "MONTY"[4] # Will return Y

# String methods
parrot = "Parrot"

print len(parrot) # will return number of letters in a string which in this case is 6
print parrot.lower() # will return parrot with all lowercase letters
print parrot.upper() # will return PARROT with all captialized letters

pi = 3.14
print str(pi) # will turn non-strings into strings

# String Concatenation
print "Green Eggs " + "and " + "ham!" # Must take into account spaces

# String formatting with % 
name = "Moe"
state = "New Jersey"
print "Hello my name is %s! I am from %s" %(name, state)

# String concatination with raw_inputs
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

# \ is simply a continuation marker
print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

# Getting current data and time
from datetime import datetime

now = datetime.now
print now # will print date in following format year-month-day 23:43:37.127290
print now.year # will return current year
print now.month # will return current month
print now.day # will return current day

# To properly format everything simply use %s
print "%s/%s/%s" % (now.month, now.day, now.year)
# Same can be done for time using hour, minute, second
