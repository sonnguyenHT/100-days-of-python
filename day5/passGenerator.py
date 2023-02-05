import string
import random
lower_list = string.ascii_lowercase
upper_list = string.ascii_uppercase
character_list = lower_list + upper_list
special_characters = "!@#$%^&*()-+?_=,<>/"
num_password = int(input("How length you want your password: ")) #length of your password
password = ''
num_specCharacter = int(input("How many special characters you want to input: ")) #quantity of special character in your password string

num_number = int(input("How many number characters you want to input: "))#quantity of number character in your password
num_normalCharacter = num_password - num_specCharacter - num_number

## easy level
## fdhsajfldjs!@#$@$234
pass_list = list()
for x in range(num_password):
    if x < num_normalCharacter:
        x = random.choice(character_list)
        pass_list.append(x)
    elif x >= num_normalCharacter and x<(num_normalCharacter+num_specCharacter):
        x = random.choice(special_characters)
        pass_list.append(x)
    else:
        x = random.randint(0,9)
        pass_list.append(x)
print(pass_list)
print("################")
## hard level
## fdsaf$#2$%fjdsk#!123 
pass_out = ""
## create a string full of normal character
for x in range(num_normalCharacter):
    x = random.choice(character_list)
    pass_out += x
## add special characters to string
for x in range(num_specCharacter):
    x = random.choice(special_characters)
    print("x:" +x)
    y = random.randint(0,len(pass_out))
    print("y:"+str(y))
    # print(type(y))
    pass_out = pass_out[:y] + x + pass_out[y:]
## add number character to string
for x in range(num_number):
    x = random.randint(0,9)
    print("x:" +str(x))
    y = random.randint(0,len(pass_out))
    print("y:"+str(y))
    # print(type(y))
    pass_out = pass_out[:y] + str(x) + pass_out[y:]
print(pass_out)
print("#######################")
## second way
## add all character to a list -> change the order of item in list 
## can use random.shuffle() function to shuffle the list

pass_list1 = []
for x in range(num_normalCharacter):
    pass_list1.append(random.choice(character_list))
for x in range(num_specCharacter):
    pass_list1.append(random.choice(special_characters))
for x in range(num_number):
    pass_list1.append(random.randint(0,9))
print(pass_list1)
random.shuffle(pass_list1)
print(pass_list1)
password1 = ""
for x in pass_list1:
    password1 = password1 + str(x)
print(password1)