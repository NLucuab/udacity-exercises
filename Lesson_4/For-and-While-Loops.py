# Check for Understanding: For and While Loops Section 

# Question 1:
# There are certain requirements you want to consider addng into a while loop. 
# Which of these requirements must be met? (Select all that apply)
(Choice 1) The condition for exiting the while loop should be included (My choice) - correct!!
(Choice 2) Check if the iteration codition is met (My choice) - correct!!
(Choice 3) Body of the loop should change the value of condition variables (My choice) - correct!!

# Question 2: 
# What type of loop should we use? 
# You need to write a llop that takes the numbers in a given list: 
# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. 
# If there are fewer than 5 odd numbers, add all of the odd numbers. 

# Would you use a while loop or a for loop to write this code? 

#Enter and test your code below. 

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

index = 0
odd_sum = 0
odd_count = 0

while odd count < 5 and index < len(num_list):
    curr_val = num_list[index]
    if curr_val % 2 == 1:
        odd_sum += curr_val
        odd_count += 1
    index += 1
print(odd_sum)
