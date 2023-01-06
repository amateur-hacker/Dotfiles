#Day 10:

#Functions with Outputs.
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

#Storing output in a variable.
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly.
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  # Docstrings:
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Result: {formated_f_name} {formated_l_name}"

#printing the docstring by using __doc__ keyword:
print(format_name.__doc__)

#printing the docsting by using the help method:
help(format_name)

# PythonQuiz:
# 1.
def Add(n1, n2):
  return n1 + n2

def Subtract(n1, n2):
  return n1 - n2

def Multiply(n1, n2):
  return n1 * n2

def Divide(n1, n2):
  return n1 / n2

print(Add(2, Multiply(5, Divide(8, 4))))

"""Option:
a. 10
b. 12.0
c. 0.21
d. 14
"""

#2.
def outer_function(a, b):
  def inner_function(c, d):
    return c + d
  return inner_function(a, b)

result = outer_function(5, 10)
print(result)

"""Option:
a. Syntax Error
b. 15
c. 10
d. (5, 10)
"""

#3.
def my_function(a):
  if a < 40:
    return 
    print("Terrible")
  if a < 80:
    return "Pass"
  else:
    return "Great"

print(my_function(25))

"""Option:
a. NameError
b. SyntaxError
c. None
d. "pass"
e. "Great"
"""




