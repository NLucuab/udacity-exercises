# QUIZ: For Loops Quiz Section

# Quiz: Create Usernames

# Question 1:
# Write a for loop that iterates over the names list to create a usernames list. To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

should create the list:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

# Write your code below.

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ","_"))

print(usernames)

# Question 2:
# Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)

(Choice 1) Modifies the names list so that each name is lowercase and separated by underscores
(Choice 2) Causes a runtime error
(Choice 3) The printed output for names list will look exactly like it did in the first line (My choice) - correct!!
(Choice 4) Deletes the list

# Reasoning: During each iteration, the name variable is set to a string taken from the list.
# Then the assignment statement creates a new string and changes the name variable to that string.
# It doesn't modify the contents of the names list at all.
# In order to modify the list you must operate on the list itself, using range, as you saw earlier.

# -------------------------------------
# Quiz: Modify the Usernames with range

# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
# Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. 
# After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should change to this:

usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]


# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(' ', '_')
print(usernames)

# Quiz: Tag Counter

# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
# XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
# Keep track of the number of tags using the variable count.

# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' or token[-1] == '>':
        count += 1
    else:
        count += 0

print(count)

# -------------------------
# Quiz: Create an HTML list
# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. 
# For example, if the list is items = ['first string', 'second string'], printing html_str should output:

# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>

# That is, the string's first line should be the opening tag <ul>. 
# Following that is one line per element in the source list, surrounded by <li> and </li> tags. 
# The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
html_str = '<ul>\n'

for item in items: 
    html_str = html_str + "<li>" + item + "</li>\n"
html_str = html_str + "</ul>"

print(html_str)