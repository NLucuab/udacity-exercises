flower_dict = {}
with open('flowers.txt','r') as f:
    for line in f:
        line2 = line.split()
        letter = line2[0]
        flower_name = line2[1:]
        flower_dict[letter] = flower_name

name = input('Enter your First [space] Last name only: ')
first_letter = FirstLastName[0]
print("First letter check! => {}".format(First_Letter))

message = "Unique flower name with the first letter of your name: {}"
