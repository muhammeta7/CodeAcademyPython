# Student becomes the Teacher
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Print all students with grades
students = [lloyd,alice, tyler]
for student in students:
    print student["name"],"\n",student["homework"],"\n",student["quizzes"],"\n",student["tests"]
    print # Just spacing in between each student

# Create average function
def average(numbers):
     total = sum(numbers)
     total = float(total)
     total = total/len(numbers)
     return total

# Get average for specific student function
def get_average(student):
    homework=average(student["homework"])*0.1
    quizzes=average(student["quizzes"])*0.3
    tests=average(student["tests"])*0.6
    return homework+quizzes+tests

# Letter grade functions
def get_letter_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
        
print get_letter_grade(get_average(lloyd))
print get_letter_grade(get_average(alice))
print get_letter_grade(get_average(tyler))

# Get the class average function
def get_class_average(students):
    results = []
    for student in students:
        current_result = get_average(student)
        results.append(current_result)
    return average(results)
    
print get_class_average(students)
print get_letter_grade(get_class_average(students))