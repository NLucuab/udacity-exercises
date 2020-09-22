QUIZ: Sets Quiz Section

# Question 1:
# What would the output of the following code be? 
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))

My answer: 6

# QUIZ: add and pop
# Consider the following code:
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop()

# After executing this code, will the number 5 be a part of the set b?

(Choice 1) Yes - incorrect
(Choice 2) No - incorrect
(Choice 3) Maybe (My choice) - correct!!
(Choice 4) No, an error is generated - incorrect

# Reasoning for choice: When you pop an element from a set a random element is removed.
# With that being said, there is a chanc that the number 5 may or may not be removed
# from the set. 