# calculation sum of even numbers from 1 to 100 include 1,100
sum =0
for x in range(101):
    if x%2 ==0 :
        sum +=x

print("Sum of even numbers : "+str(sum))