print("Welcome to Pizza Deliverries")
bill =0
size = input("What size do you want? S,M or L:")
if(size == "S"):
    bill += 15
elif size == "M":
    bill +=20
else: 
    bill +=25
add_pepperoni = input("Do you want pepperoni ?Y or N:")
if(add_pepperoni.lower() == "y"):
    if(size == "S"):
        bill +=2
    else:
        bill +=3
extra_cheese = input("Do you want cheese ? Y or N:")
if(extra_cheese.lower()=="y"):
    bill += 1

print("Total bill is "+str(bill))