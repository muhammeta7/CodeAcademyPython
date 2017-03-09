# Operators
# Equal to ==
# Not Equal to !=
# Less Than <
# Less Than or Equal To <=
# Greater Than >
# Greater Than or Equal to >=

"""
     Boolean Operators
------------------------      
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

not is evaluated first;
and is evaluated next;
or is evaluated last.

"""

# Conditionals use if, elif, else with : and indent
def greater_less_equal_5(answer):
    if answer>5:
        return 1
    elif answer<5:          
        return -1
    else:
        return 0

# PygLatin Problem
print 'Welcome to the Pig Latin Translator!'

pyg = 'ay'
original = raw_input("Enter a word:")
# isalpha() ensures that the user inputs only alphabetical characters 
# example: j3728gh would return false
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:len(word)]+first+pyg
    print new_word
else:
    print 'empty'