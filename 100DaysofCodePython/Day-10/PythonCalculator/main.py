#Calculator:
from art import logo
from replit import clear

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  for operation in operations:
    print(operation)
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    next_step = input(f"Type 'y' to continue calculating with {answer}, or type 's' to start a new calculation or to n to exit: ")
    if next_step == "y":
      num1 = answer
    elif next_step == "s" :
      should_continue = False
      clear()
      calculator()
    else:
      should_continue = False

calculator()