# QUIZ SECTION: Variables & Assignment Operators Quiz Section

# Quiz: Assign and Modify Variables
# Now it's your turn to work with variables. 
# The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables.
# After each comment write a line of code that implements the instruction.

# Note that this code uses scientific notation to define large numbers. 
# 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.

# 1. The current volume of a water reservoir (in cubic meters)
reservoir_volume = 4.445e8

# 2. The amount of rainfall from a storm (in cubic meters)
rainfall = 5e6

# 3. Decrease the rainfall variable by 10% to account for runoff
rainfall-=rainfall*0.1

# 4. Add the rainfall variable to the reservoir_volume variable
reservoir_volume+=rainfall

# 5. Increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume+=reservoir_volume*0.05

# 6. Decrease reservoir_volume by 5% to account for evaporation
reservoir_volume-=reservoir_volume*0.05

# 7. subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume-=2.5e5

# print the new value of the reservior_volume variable
print(reservoir_volume)