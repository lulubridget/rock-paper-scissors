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
import random
image = [rock, paper, scissors]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player_choice >2 or player_choice < 0:
    print("invalid input")
else:
    print(image[player_choice])
    computer_choice = random.randint(0,2)
    print(image[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("player win")
    elif player_choice ==2 and computer_choice == 0:
        print("player lose")
    elif player_choice==computer_choice:
        print("tie")
    elif player_choice > computer_choice:
        print("player win")
    elif player_choice < computer_choice:
        print("player lose")

