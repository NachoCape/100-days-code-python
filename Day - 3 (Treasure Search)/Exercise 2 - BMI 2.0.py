# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(int(weight) / (float(height)*float(height)))
print(f"Your BMI is {bmi}, you ", end="")
if bmi < 18.5:
    print("are underweight.")
elif bmi > 18.5 and bmi <=25:
    print("have a normal weight.")
elif bmi > 25 and bmi <= 30:
    print("are slightly overweight.")
elif bmi > 30 and bmi <= 35:
    print("are obese.")
else:
    print("you are clonically obese.")
