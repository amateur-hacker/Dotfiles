# Day 4: 
# Randomisation and python lists:

import random

random_integer = random.randint(1, 10)
print(random_integer)

# random method gives the float number between 0 to 1 .
# To get the float number between 0 to 5

random_float = random.random() * 5
print(random_float)

# Another Example:

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Python Lists : Data Structure

# Example:
fruits = ["mango", "banana", "orange", "lichi", "watermelon"]
print(fruits)

# Accessing the elements in list from positive indices.
print(fruits[2])

# Accessing the elements in list from negative indices.
print(fruits[-1])

# Changing the elements from their indices.
fruits[4] = "grapes"
print(fruits)

# Adding the elements from append method.
fruits.append("watermelon")
print(fruits)

# Adding the whole bunch of items from extend method.
fruits.extend(["papaya", "apple"])
print(fruits)

# Adding the elements in list from insert method.
fruits.insert(0, "coconut")
print(fruits)

# Removing the elements in list from remove method.
fruits.remove("coconut")
print(fruits)

# Removing the last element in list from pop method.
fruits.pop()
print(fruits)

# Removing all items from the list by using clear method.
# fruits.clear()
# print(fruits)

# Accessing the elements index by using index method.
print(fruits.index("orange"))

# Accessing the same other elements in list by using index method.
fruits.append("orange")
print(fruits.index("orange", 3))

# counting the elements in a list by using count method.
count_orange = fruits.count("orange")
print(count_orange)

# sorting the list by using sort method.
fruits.sort()
print(fruits)

# copying a list by using copy method.
basket1 = fruits.copy()
print(basket1)

# to find length of string by using the len method.
name = "sachin"
print(len(name))
print(len(basket1))

# Example:
# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", " Potatoes"]
# print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[1])
print(dirty_dozen[1] [1])
