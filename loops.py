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

## Break is to break out of a loop in a conditional
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break

## While / else
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else: ## executes any time the loop condition is evaluated False
    print "You win!"

## Your own while / else 
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print random_number

guesses_left = 3

while guesses_left > 0: # Starts game
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1
    print guesses_left
else:
    print "You lose."

# Censor
def censor(text, word):
    text = text.split()
    count = len(word)
    new_text = ''
    for index in text:
        if index == word:
            new_text = new_text + " " + ("*" * count) 
        else: 
            new_text = new_text + " " + index 
    return new_text.lstrip(" ")

print censor("hey hey hey", "hey")

# Count 
def count(sequence,item):
    num_counter = 0
    for i in sequence:
        if i == item:
            num_counter = num_counter+1
    return num_counter
    
print count([2,3,4,3,4,5,3],3)