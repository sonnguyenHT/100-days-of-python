height = input("Enter your height(m): ")
weight = input("Enter your weight(kg): ")

bmi = float(weight) / (float(height) ** 2)
print("Your BMI is "+str(round(bmi)))   # round() is a function to round the number

if(bmi<18.5):
    print("You are underweight")
elif bmi<=25:
    print("You are normal")
elif bmi<=30:
    print("Your are overweight")
elif bmi<=35:
    print("You are obese")
else:
    print("You are clinically obese")