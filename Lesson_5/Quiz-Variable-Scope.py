# QUIZ: Variable Scope Quiz Section 

# Read through this code snippet:

egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

# What is the result of running this code?

 (Choice 1) egg_count equals zero - incorrect
 (Choice 2) egg_count equals 12 - incorrect
 (Choice 3) An error occurs (My choice) - correct!!

# Reasoning: The variable 'egg_count' is located outside of the function block. 
# Due to it being outside of the function's scope, it cannot perform any modifications on it (the variable).