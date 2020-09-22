# QUIZ: Check for Understading- Data Structures Quiz Section

# Question 1: 
# Which of the following statements about tuples are true? Select all that apply.

(Choice 1) A tuple is a mutable data structure. - incorrect # (tuples are immutable)
(Choice 2) A tuple is an ordered data structure. (My choice) - correct!!
(Choice 3) A tuple can be indexed and sliced like a list. (My choice) - correct!!
(Choice 4) A tuple is defied by listing a sequence of elements
separated by commas and contained within curly braces: {} - incorrect # (this describes a dictionary.)

# Question 2:
# Which of the following statements about sets are true? Select all that apply.

(Choice 1) A set is a mutable data structure (My choice) - correct!!
(Choice 2) A set is an ordered data structure - incorrect # (A set is an unordered data structure.)
(Choice 3) A set can be indexed and sliced like a list - incorrect # (Due to sets being unordered data structures, you can't index or slice elements like a list.)
(Choice 4) A set does not contain duplicate elements (My choice) - correct!!

# Question 3:
# Is the following statement true or false? 
A set is the only data structure defined with curly braces: {}
My answer: False - correct!!
# Dictionaries are another data structure that is defined with curly braces

# Question 4: 
# Which of the following statements about dictionaries are true? Select all that apply. 
(Choice 1) A dictionary is a mutable data structure. (My choice) - correct!!
(Choice 2) A dictionary is an ordered data structure. - incorrect # A dictionary is an unordered data structure, making this false. 
(Choice 3) A dictionary can be indexed using keys (My choice) - correct!!
(Choice 4) The keys of a dictionary are unique. (My choice) - correct!!
(Choice 5) Any data type can be used as a key in a dictionary. # Dictionary keys must be immutable, meaning a list - a mutable data structure - cannot be used, therefore making this false. 

# Quiz: Identify the Problem
# Run the code below - it should break. Take alook at the error message and try to figure out what the issue is. Then, answer the quiz question below the editor. 

# invalid dictionary - this should break
room_numbers = {
    ['Freddie', 'Jen']: 403,
    ['Ned', 'Keith']: 391,
    ['Kristin', 'Jazzmyne']: 411,
    ['Eugene', 'Zach']: 395
}

# My solution
room_numbers = {'Freddie'and 'Jen': 403,
'Ned' and 'Keith': 391, 'Kristin'and 'Jazzmyne': 411, 'Eugene' and 'Zach': 395}
print(room_numbers)

# Question 6:
# What's wrong with the code above? 

(Choice 1) The dictionary can not use a container for its keys. - incorrect 
(Choice 2) The dictionary is using a mutable datatype for its keys. (My choice) #lists are mutable, and thus makes this statement True.
(Choice 3) There are too many values in each dictionary key. - incorrect

