# 🚨 Don't change the code below 👇
height = input("Enter your height in foot: ")
weight = input("Enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_in_metre = float(height) * 0.3048
metre_square = height_in_metre * height_in_metre
BodyMassIndex = int(weight)/ metre_square
print(BodyMassIndex)
