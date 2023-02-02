a = input("Input a 2 characters number :")
sum = int(int(a)/10) + int(a)%10    # change type string of a to int then take the first character + second character
print("Character sum: "+str(sum))

### second way
firstDigit = a[0]
secondDigit = a[1]
sum = int(firstDigit) + int(secondDigit)
print("Character sum: "+ str(sum))