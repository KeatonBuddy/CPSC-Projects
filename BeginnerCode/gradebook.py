"""
DISCLAIMER:
The source code contained in this file was written haphazardly in a short
amount of time during a live presentation setting. It should not be taken
as an exemplar of good design and organization of program source code!
The main purpose of the exercise was to demonstrate rapidly how the steps
of an algorithm may be transformed into Python statements.

We do not warrant against bad habits developed from studying this code.
USE AT YOUR OWN RISK!


Our little toy gradebook application to generate grades and calculate averages.
See pp 122-123 in the text for a more concise example of the same concepts.
"""

import random
import stdarray
import stdio

def generate_random_grades(num_students, num_assignments):
    """
    this function generates a table of random grades,
    :param num_students: rows
    :param num_assignments: columns
    :return: 2D array of grades
    """
    gradebook = stdarray.create2D(num_students, num_assignments, 0.0)
    for i_student in range(num_students):
        for j_assignment in range(num_assignments):
            grade = random.normalvariate(70.0, 10.0)
            gradebook[i_student][j_assignment] = grade
    return gradebook

def print_gradebook(names, gradebook, averages):
    num_students = len(names)
    num_assignments = len(gradebook[0])
    for i_student in range(num_students):
        # first print student's name
        stdio.write(names[i_student] + '\t')
        # then print their grade for each assignment
        for j_assignment in range(num_assignments):
            grade = gradebook[i_student][j_assignment]
            rounded = round(grade, 1)
            stdio.write(rounded)
            stdio.write('\t')
        # then print averages
        stdio.write(averages[i_student])
        # finish the line with a newline character
        stdio.writeln()


# seed the random number generate with a fixed value
# so that I get the same numbers every time
random.seed(12)

students = ['Alice', 'Bob ', 'Carol', 'Dave', 'Emily', 'Frank']
num_students = len(students)
num_assignments = 3

gradebook = generate_random_grades(num_students, num_assignments)

# if we wanted the average of assignment #2
total = 0.0
for i_student in range(num_students):
    # fetch A2 grade for student i
    total += gradebook[i_student][1]     # 2nd assignment is index 1 column
average_a2 = total / num_students

stdio.writeln('Average for Assignment #2 is ' + str(average_a2))

# if we anted to calculate the average for all students
student_averages = []
# for every student in the class
for i_student in range(num_students):
    # calculate the students average score
    # sum up scores from all assignments
    total = 0.0
    for j_assignment in range(num_assignments):
        total += gradebook[i_student][j_assignment]
    # divide by total assignments
    average = total / num_assignments
    # append to list of averages
    student_averages += [average]

print_gradebook(students, gradebook, student_averages)

#print(student_averages)




