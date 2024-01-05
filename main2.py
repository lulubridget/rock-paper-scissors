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
game_images = [rock, paper, scissors]

def user_play():
    while True:
        try:
            user_input = int(input("What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
            if user_input >=3 or user_input <0:
                print("out of range. ")
                continue
            return user_input
            
        except ValueError:
            print("invalid input")
            continue

def computer_play():
    computer_input = random.randint(0,2)
    return computer_input

def play_game():
    while True:
        user = user_play()
        computer = computer_play()
        print(f"You choose: {game_images[user]}")
        print(f"computer choose:\n {game_images[computer]}")

        if computer== user:
            print("tie")
        elif computer == 2 and user == 0:
            print("you win")
        elif computer == 0 and user == 2:
            print("you lose")
        elif computer > user:
            print("you lose")
        elif computer < user:
            print("you win")
        
        continue_play = input("do you want to play again? (y/n): ").lower()
        if continue_play == "n":    
            print("Thank you for playing.")
            break
   
play_game()

