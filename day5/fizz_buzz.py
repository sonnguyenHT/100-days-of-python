for x in range(1,101):
    if x%3 ==0 :
        if x%15 == 0 :
            print("FizzBuzz")
        else:
            print("Fizz")
    else:       
        if x%5==0:
            if x%15 != 0 :
                print("Buzz")
        else:
            print(x)

## second way
for x in range(1,101):
    if x%5 ==0 and x%3==0:
        print("FizzBuzz")
    elif x%3==0:
        print("Fizz")
    elif x%5==0:
        print("Buzz")
    else:
        print(x)