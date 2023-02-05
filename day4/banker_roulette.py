import random

str_inp = "son, ngoc, nhat, hieu"
str_split = str_inp.split(", ")
user_picked = random.choice(str_split)
print(str_split)
print("User picked: "+user_picked)