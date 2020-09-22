names =  input("Please provide a list of names:").split(',')# get and process input for a list of names
assignments_str =  input("Please provide a list of the number of assignments:").split(',')# get and process input for a list of the number of assignments
assignments = [int(assignment) for assignment in assignments_str]
grades_str = input("Please provide a list of grades:").split(',')
grades = [int(grade) for grade in grades_str]

#Breakdown: Split up the strings for assignments_str & grades_str and feed into loops that will convert the separated numbers into ints(?)
#Those individual numbers will be fed into the for loop that will put out the message (printed)
#You can't convert a list into an interger. So you have to split it up into separate elements

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for (name, assignment, grade) in zip(names, assignments, grades):
    potential_grade = grade + (2 * assignment)
    print(message.format(name, assignment, grade, potential_grade))
