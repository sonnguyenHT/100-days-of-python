year = int(input("Enter year: "))

if year%4==0:
    if year%100==0:
        if year%400 ==0:
            print("Year is leap")
        else:
            print("Year is not leap")
    else:
        print("Year is leap")
else:
    print("Year is not leap")