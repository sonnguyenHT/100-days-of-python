height = input("Enter your height(m): ")
weight = input("Enter your weight(kg): ")

bmi = float(weight) / (float(height) ** 2)
print("Your BMI is "+str(round(bmi)))   # round() is a function to round the number