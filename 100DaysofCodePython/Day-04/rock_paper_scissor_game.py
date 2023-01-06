rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number, you lose!")
  
else:
  print(game_images[user_choice])

  print("Computer chose:")
  computer_choice = random.randint(0, len(game_images) - 1)
  print(game_images[computer_choice])
  
  
  if user_choice == 0 and computer_choice == 1:
    result = "You Lose!"
  elif user_choice == 0 and computer_choice == 2:
    result = "You win!"
  elif user_choice == 1 and computer_choice == 0:
    result = "You win!"
  elif user_choice == 1 and computer_choice == 2:
    result = "You Lose!"
  elif user_choice == 2 and computer_choice == 0:
    result = "You Lose!"
  elif user_choice == 2 and computer_choice == 1:
    result = "You win!"
  elif user_choice == computer_choice:
    result = "It's a draw"
  else:
    result = None
  
  print(result)