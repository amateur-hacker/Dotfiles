# Day 2:
# Data types, Numbers, Operations, Type coversion, F-Strings.

# Data Types:

# String:

# Accessing a string character through indexing.
print("Hello"[0])

# Example:
street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# Integer:

# Example:
print(123 + 345)

# Use of underscore(_) in large number to visualize the human easily:
print(123_456_789)

# Float:
pi = 3.14
print(pi)


# Boolean:

# True and False are two boolean values.
print(True)
print(False)

# Typecasting:

# Conversion of integer into string: 

num_char = len(input("What is your name? "))
print("Your name has " + str(num_char) + " characters.")

# Conversion of string into float:
print(70 + float("100.5"))

# Use of type method:

# Example 1:
num1 = 314
print(type(num1))

# Example 2:
a = int("5") / int(2.7)
print(a)

# Operators in python:
print(3 + 2)
print(13 - 11)
print(10 * 11)
print(6 / 3)
print(6 // 3)
print(2 ** 3)

# PEMDASLR
# P = Paranthensis  ()
# E = Exponential **
# M = Multiplication *
# D = Division /
# A = Addition + 
# S = Subtraction -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
print(6 * 4 / 2 - (1 * 2))

# Decimal roundoff by using round method:

print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.666666, 2))

# Use of floor division which is used to convert float into integer.

print(type(8 // 3))
result = 4 / 2
result /= 2
print(result)

# Assignment Operator:

# = (Assignment)- Used to assign a value from right side operand to left side operand.
# += (Addition Assignment)- To store to sum of both the operands to the left side operand.
# -= (Subtraction Assignment)- To store the difference of both the operands to the left side operand.
# *= (Multiplication Assignment) – To store the product of both the operands to the left side operand.
# /= (Division Assignment) – To store the division of both the operands to the left side operand.
# %= (Remainder Assignment) – To store the remainder of both the operands to the left side operand.

# Example:
score = 0 

# User scores a point
score += 1
print(score)

# Use of f-String
score = 2
height = 1.8
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
