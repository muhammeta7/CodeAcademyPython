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

# Purify 
def purify(array):
    even_array=[]
    for i in array:
        if i%2 == 0:
            even_array.append(i)
    return even_array
    
print purify([2,3,4,5,6,7,8,9,20])

# Product
def product(array):
    total= 1
    for i in array:
        total *= i    
    return total
    
print product([4,5,5])

# Remove Duplicates
def remove_duplicates(array):
    new = []
    for i in array:
        if i not in new:
            new.append(i)
    return new
    
print remove_duplicates([1,1,2,3,4,4,5])

# Median
def median(array):
    new_array = sorted(array)
    length = len(new_array)
    midpoint = len(new_array)/2
    if length%2 != 0 :
        return new_array[midpoint]
    else:
        second_num = new_array[midpoint-1]
        return (new_array[midpoint]+ second_num)/2.0
        
print median([4,3,2,1])

# ===========================================================================
# Exam Statistics

# Print those Grades
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for i in grades:
        print i
        
print_grades(grades)

# The sum of scores
def grades_sum(scores):
    total = 0
    for i in scores:
        total += i
        
    return total
    
print grades_sum(grades)

# Computing the average
def grades_average(grades):
    result = grades_sum(grades)
    return result/float(len(grades))
    
print "Average: ",grades_average(grades)

# The Variance
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    length = len(scores)
    for score in scores:
        variance += (average-score) ** 2
        
    return variance/length
    
print grades_variance(grades)

# Standard Deviation
def grades_std_deviation(variance):
    return variance**0.5
    
variance = grades_variance(grades)
print grades_std_deviation(variance)