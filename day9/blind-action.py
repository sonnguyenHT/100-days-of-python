from replit import clear

winner_name = ""
max = 0
lis =list()
while True:
    name =input("What is your name? ")
    bid = int(input("What you want to bid? "))
    dic = {
        "name": name,
        "bid": bid
    }
    lis.append(dic)
    if(dic["bid"] > max): 
        winner_name=name
        max = dic["bid"]
    end = input("Do you want to end? ")
    if( end == "yes"):
        clear()
        break
    else:
        clear()
        continue

print("The winner is " + winner_name + " with the bid is "+ str(max))