# Day-16 :
# Object Oriented Programming (OOPS):

from turtle import Turtle, Screen
from prettytable import PrettyTable

# Assigning the new object
timmy = Turtle()
print(timmy)
# Giving a shape of turtle by using shape method.
timmy.shape("turtle")

# Giving a color for turtle by using turtle library
timmy.color("coral")

# Moving 100 step forward turtle by using forward method.
timmy.forward(100)

# Accessing/calling the attributes from turtle module
my_screen = Screen()
print(my_screen.canvheight)

# Accessing/calling the methods from turtle module
my_screen.exitonclick()

# Constructing a table by using prettytable module.

table = PrettyTable()

# Adding column to pokemon-name:
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

# Adding another column to pokemon-type:
table.add_column("Type", ["Electric", "Water", "Fire"])

# Using an align attribute to change the alignment of table.
table.align = "l"
print(table)
