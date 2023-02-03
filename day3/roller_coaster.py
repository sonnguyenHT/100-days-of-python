print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
money = 0
photo = False
if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if(age<12):
        money = 5
        print("Please pay"+str(money)+ "$")
    elif(age <18):
        money =7
        print("Please pay"+str(money)+ "$")
    elif(age>45 and age <55):
        print("Everything is going to be ok. Have a free ride on us!")
        exit()
    else:
        money=12
        print("Please pay "+str(money)+"$")
    photo = input("Do you want to take photos?(yes/no)")
    if (photo.lower() == "yes") | (photo.lower() == "y") :
        money +=3
    print("The total bill is "+str(money))
else:
    print("You cannot ride the rollercoaster")