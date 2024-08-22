"""Rock Paper Scissors Game"""
import random

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

materials = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n "))

print(materials[choice])

print("Computer chose:\n")

computer_choice = random.choice(materials)
print(computer_choice)

if materials[choice] == computer_choice:
    print("It's a draw")

if (materials[choice] == rock and computer_choice == scissors or
   materials[choice] == paper and computer_choice == rock or
   materials[choice] == scissors and computer_choice == paper):
    print("You win!")

if (materials[choice] == rock and computer_choice == paper or
   materials[choice] == paper and computer_choice == scissors or
   materials[choice] == scissors and computer_choice == rock):
    print("You loss!")

