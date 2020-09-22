QUIZ: Compound Data Structures Quiz Section

# Quiz: Adding Values to Nested Dictionaries
# Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' 
# to each dictionary in the elements dictionary. 
# After inserting the new entries you should be able to perform these lookups:
# >>> print(elements['hydrogen']['is_noble_gas'])
# False
# >>> print(elements['helium']['is_noble_gas'])
# True

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True
print(elements['helium']['is_noble_gas'])
print(elements['hydrogen']['is_noble_gas'])
elements['neon'] = {'number': 4, 'weight': 3.0909, 'symbol': 'Ne', 'is_noble_gas': True} 
print(elements)

# Question 2: 
# Check the attributes of a collection for which using a Pythno list would be appropriate.

(Choice 1) The order in which you add items doesn't matter ' - incorrect # lists are ordered- so the order in which you add items DOES matter.
(Choice 2) Items are always indexed with numbers starting at 0 (My choice) - correct!!
(Choice 3) Sortable - (My choice) - correct!!
(Choice 4) Add items with .append (My choice) - correct!!
(Choice 5) Add items with .add - incorrect #this method is not used with lists; it is used with sets.

# Question 3:
# Check the attributes of a collection for which using a Python set would be appropriate.

(Choice 1) Order in which items appear can be inconsistent (My choice) - correct!!
(Choice 2) You can have the same entry multiple times - incorrect # Sets do not allow duplicate values- if a duplicate is added, it is ignored and the set remains unchanged.
(Choice 3) Mutable (you can change it) (My choice) - correct!!
(Choice 4) Add items with .add (My choice) - correct!!
(Choice 5) Sortable - incorrect # Sets are unordered, so sorting is not possible.

# Question 4: 
# Check the attributes of a collection for which using a Python dictionary would be appropriate.

(Choice 1) Each item contains two parts (My choice) - correct!!
(Choice 2) Add items with .append - incorrect # .append is a list method, and is not used for dictionaries.
(Choice 3) Order in which items appear can be inconsistent (My choice) - correct!!
(Choice 4) Sortable - incorrect # dictionaries are unordered, so sorting is not possible. 
(Choice 5) Can be nested (My choice) - correct!!