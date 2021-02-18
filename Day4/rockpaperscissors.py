# Design a rock, paper, scissors game

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

user = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors.\n"))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
else:
    print(scissors)

comp_choices = [rock, paper, scissors]

comp_final_choice = (random.choice(comp_choices))
print(comp_final_choice)

if comp_final_choice == rock and user == 1:  # paper
    print("PLAYER WINS")
elif comp_final_choice == paper and user == 2:  # scissors
    print("PLAYER WINS")
elif comp_final_choice == scissors and user == 0:  # rock
    print("PLAYER WINS")
elif comp_final_choice == rock and user == 0:
    print("TIE GAME")
elif comp_final_choice == paper and user == 1:
    print("TIE GAME")
elif comp_final_choice == scissors and user == 2:
    print("TIE GAME")
else:
    print("COMPUTER WINS!!!!!")
