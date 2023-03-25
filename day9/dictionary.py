first_dict = {
    "a": "help",
    "c": -4,
    3: "hell"
}


#retrieving Data 
print(first_dict)
print(first_dict["c"])
print(first_dict[3])

# add new data
first_dict["osn"] = "help me"
print(first_dict)

# loop through the dictionary
for key in first_dict:
    print(key)
    print("values is:")
    print(first_dict[key])