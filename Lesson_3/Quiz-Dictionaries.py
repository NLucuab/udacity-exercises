# QUIZ: Dictionaries and Identity Operators Quiz Section

# Quiz: Define a Dictionary
# Define a dictionary named population that contains this data:

Keys	   Values
Shanghai	17.8
Istanbul	13.3
Karachi	    13.0
Mumbai	    12.5

# Define a Dictionary, population,
# that provides information on the world's largest cities.
# The key is the name of a city (a string), and the associated
# value is its population in millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}

# Question 2:
# Which of these could be used as the key for a dictionary? (Choose all that apply.)

(Choice 1) - str (My choice) - correct!!
(Choice 2) - list incorrect
(Choice 3) - int (My choice) - correct!!
(Choice 4) - float (My choice) - correct!!

# Reasoning: Dictionary keys must be immutable. Lists are a type of mutable
# data structure. The 3 other choices are immutable elements. 

# Question 3:
# What happens if we look up a value that isn't in the dictionary? 

(Choice 1) - The lookup returns None
(Choice 2) - The key is added to the dictionary with a default value of None
(Choice 3) - A KeyError occurs (My choice) - correct!!
(Choice 4) - Python searches the Internet for an appropriate value

# Question 4: 
# Checking for Equality vs. Identity: == vs. is
# What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

(Choice 1) - True, True, True, True - incorrect
(Choice 2) - True, False, True, False - incorrect
(Choice 3) - True, True, True, False (My choice) - correct!!
(Choice 4) - True, True, False, False - incorrect

# Reasoning: a & b are equal and identical lists. 
# Lists a, b & c are equal because they have the same contents.
# a & c are not identical objects, and thus point to two different objets. 
# There is a difference between 2 objects being equal and 2 objects being identical.

# -----------------------------
# Quiz: More with Dictionaries
# Context
# Use the dictionary below to answer ALL of the questions regarding dictionaries. 
# Consider you have a dictionary named animals that looks like this:

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}

# Question 1: 
# Match each description to the value it describes.

1) The data type of the keys in the dictionary -- My answer: strings
2) The data type of the values in the dictionary -- My answer: lists
3) the result of animals['dogs'] -- My answer: [20, 10, 15, 8, 32, 15]
4) The result of animals ['dogs'][3] -- My answer: 8
5) The result of animals[3] -- My answer: Error (A KeyError, due to the lack of key '3')
6) The result of animals['fish'] -- My answer: [0.3, 0.5, 0.8, 0.3, 1]
