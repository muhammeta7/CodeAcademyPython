# Loops

## While loops executes code if some condition is true
count = 0

if count < 10:
    print "Hello, I am an if statement and count is", count
    
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1

## Condition
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False

## While you're at it
num = 1

while num<11:  # Fill in the condition
    print num**2 # Print num squared
    num +=1 # Increment num 

## Simple Errors
choice = raw_input('Enjoying the course? (y/n)')

while choice !="y" and choice !="n": 
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")

## An infinite loop can happen if the loop never exits
count = 0

while count < 10: 
    print count
    count +=1  # lets say -= was the case it would never break out of loop