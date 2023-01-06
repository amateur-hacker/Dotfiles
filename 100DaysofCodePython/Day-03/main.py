# Conditional Statements, Logical Operators, Code Blocks and Scope.

# Control flow with if/else and conditional operators:

# Comparison Operator:

# 1. > (Greater than)
# 2. < (Less than)
# 3. >= (Greater than or equal to)
# 4. <= (Less than or equal to)
# 5. == (Equal to)
# 6. != (Not equal to)

# Logical operators:
# and or &&
# or  or |
# not 

# Example with:
# if else statements, Nested if statements and elif statements,  Multiple If Statements in Succession, logical operators:
# 1 foot = 30.48 centimeter

print("Welcome to the rollercoaster!")
height = float(input("What is your height in foot? "))
bill = 0
height = height * 30.48

if height >= 120:
  print("Yes, You can ride the rollercoaster!")
  age = int(input("What is Your age? "))
  
  if age <= 18:
    if age < 12:
      bill = 5
      print("You have to just pay $5, as you are child.")
    else:
      bill = 7
      (print("You have to pay $7, as you are youth"))
      
  elif age >= 45 and age <= 100:
    print("Everything is going to be okay. Have a free ride on us.")
  else:
    bill = 12
    print("You have to pay $12, as you are adult.")

  wants_photo = input("Do you want a photo taken? Y or N. ").lower()
  if wants_photo == "y":
    bill += 3
  
  print(f"Your final bill is ${bill}")
    
else: 
	print("Sorry, you have to grow taller before you can ride.")
