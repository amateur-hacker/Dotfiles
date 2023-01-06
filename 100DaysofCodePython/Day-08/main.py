#Day 8

# Functions with Inputs:
# Arguments & parameters:


# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Declaring the function:
def greet():
  print("Hello Sachin")
  print("How do you do?")
  print("Isn't the weather nice today?")

# greet()


# Functions that allows for input:

def greet_with_name(name): # name ==> parameter
  print(f"Hello {name}")
  print(f"How do you do {name}?")


# greet_with_name("Sachin")  # "Sachin" ==> Argument

# Functions with more than 1 input (positional Arguments):
  
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

# greet_with("Sachin", "India, Delhi")

# Functions with keyword arguments

def number(a, b, c):
  print(f"The value of a is {a}")
  print(f"The value of b is {b}")
  print(f"The value of c is {c}")

number(c=3, a=1, b=2)
  