# QUIZ SECTION: Type and Type Conversion Quiz Section

# Quiz: Total Sales
# In this quiz, you’ll need to change the types of the input and output data in order to get the result you want.

# Calculate and print the total sales for the week from the data provided. 
# Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers. 
# You’ll need to change the type of the input data in order to calculate that total.

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

mon_sales = int(mon_sales)
tues_sales = int(tues_sales)
wed_sales = int(wed_sales)
thurs_sales = int(thurs_sales)
fri_sales = int(fri_sales)

total_sales = (mon_sales + tues_sales + wed_sales + thurs_sales + fri_sales)
total_sales = str(total_sales)

print("This week's total sales:" + " " + total_sales)
