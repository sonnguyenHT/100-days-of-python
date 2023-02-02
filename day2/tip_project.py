print("Welcome to the tip calculation")
total = input("What was the total bill ?\n")
percen = input("What percentage tip would you like to give? 10,12 or 15\n")
people_num = input("How many people to split bill?\n")

pay = float(total) * (1+float(percen)/100) / (float(people_num))
print("Each person should pay: "+str(round(pay,2)))