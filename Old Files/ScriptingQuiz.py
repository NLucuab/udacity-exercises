names =  input("Enter list of names: ").split(',')
assignments_str = input("Enter amount of missing assignments: ").split(',')
grades_str = input("Enter assignment grades: ").split(',')
# assignments = map((lambda val: int(val)),assignments_str)
assignments = [int(val) for val in assignments_str]
# grades = map((lambda val: int(val)),grades_str)
grades = [int(val) for val in grades_str]

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
# Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades.
# Use this input to create lists for names, assignments, and grades.
#Use a loop to print the message for each student with the correct values.
#The potential grade is simply the current grade added to two times the number of missing assignments.

for (name, assignment, grade) in zip(names, assignments, grades):
    new_grade = grade + (2 * assignment)
    print(message.format(name, assignment, grade, new_grade))

    
