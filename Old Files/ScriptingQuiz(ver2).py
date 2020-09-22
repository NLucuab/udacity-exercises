names =  input("Please provide a list of names!")# get and process input for a list of names
assignments =  int(input("Please provide a list of the number of assignments.").split())# get and process input for a list of the number of assignments
grades = int(input("Please provide a list of grades.").split()) # get and process input for a list of grades
potential_grade = grade + (2 * assignment)
# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assigment, grade in names, assignments, grades:
    print(message.format(name, assignment, grade, potential_grade))
