#Day 9:
# Dictionaries and Nesting

programming_dictionary = { 
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary.
programming_dictionary = {}

#Edit an item in a dictionary.
programming_dictionary["Bug"] = "A moth in your computer."
programming_dictionary["Function"] = "A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result."

#Loop through a dictionary.
for key in programming_dictionary:
  #To accesing the key
  print(key)
  #To accessing the value
  print(programming_dictionary[key])

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting List in a Dictionary.
travel_log = {
  "France": ["paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgar"],
}

#Nesting Dictionary in a Dictionary.
travelLog = {
  "France": {"cities_visited": ["paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgar"], "total_visits": 5},
}
# print(travelLog["France"]["cities_visited"])

#Nesting Dictionary in a List.
travelLog = [
  {
    "country": "France",
    "cities_visited": ["paris", "Lille", "Dijon"],
    "total_visits": 12,
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgar"],
    "total_visits": 5,
  },
]
print(travelLog)

# Quiz:
order = {"starter": {1: "Salad", 2: "Soup"}, "main": {1: ["Burger", "Fries"], 2: ["Steak"]}, "desert": {1: ["Ice Cream"], 2: []}, }
print(order["main"][2][0])

