#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end

print('Welcome to the band name Generator')
cityName = input("What's the name of the city where you grew up in ? \n")
petName = input("Enter your pet name: \n")
bandName = cityName + " " + petName
print("Your band name could be", bandName)