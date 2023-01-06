# 🚨 Don't change the code below 👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# 1.8

height_as_float = float(height)
BMI = round(int(weight) / height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif 25 > BMI > 18.5:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 30 > BMI > 25:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 35 > BMI > 30:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

