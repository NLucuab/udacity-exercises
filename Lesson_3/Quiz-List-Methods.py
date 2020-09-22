# QUIZ SECTION: List Methods Quiz Section

# QUIZ: len, max, min, and Lists

# What would the output of the following code be? 
# (Treat the comma in the multiple choice answers as newlines.)

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

(Choice 1) 200, 1  - incorrect
(Choice 2) 4, 2  - (My choice) correct!!
(Choice 3) 300, 14 - incorrect
(Choice 4) 2, 3 - incorrect

# QUIZ: sorted, join, and lists
# What would the output of the following code be? (Treat the comma in the multiple choice answers as newlines.)

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

(Choice 1) Albert, Ben, Carol, Donna - incorrect
(Choice 2) Carol & Albert & Ben & Donna - incorrect
(Choice 3) & Albert & Ben & Carol & Donna & - incorrect
(Choice 4) Albert & Ben & Carol & Donna (My choice) - correct!!

# QUIZ: append and Lists
# What would the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

(Choice 1) Albert & Ben & Carol & Donna & Eugenia - incorrect
(Choice 2) ["Carol","Albert","Ben","Donna"] - incorrect
(Choice 3) ['Albert','Ben','Carol','Donna','Eugenia'] (My choice) - correct!!
(Choice 4) ["Eugenia","Carol","Albert","Ben","Donna"] - incorrect