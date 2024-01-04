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

student_heights = [180, 124, 165, 173, 189, 169, 146]
total_heights = 0
for height in student_heights:
    total_heights += height
print(f"total heights is {total_heights}")

total_students = 0
for student in student_heights:
    total_students += 1
print(f"total student is {total_students}")

average_height = round(total_heights/total_students,)
print(f"the average weight is {average_height}")

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for letter in range(1,nr_letters+1):
     password+= random.choice(letters)

for symbol in range(1,nr_symbols+1):
    password += random.choice(symbols)

for number in range(1,nr_numbers +1):
    password+=random.choice(numbers)
random.shuffle(password)

final_password = ""
for char in password:
    final_password += char
print(f"Your password is {final_password}")
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_world = random.choice(word_list)
lives = 6
print(chosen_world)

display = []
for letter in range(0,len(chosen_world)):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("make a guess").lower()
    for position in range(len(chosen_world)):
        letter = chosen_world[position]
        if letter == guess:
            display[position] = letter

    print(display)
    if guess not in chosen_world:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("lose")
    if "_" not in display:
        end_of_game = True
        print("win")

import math
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height*width)/cover)
    print(f"you will need {number_of_cans} can of paint.")


test_h = int(input("height of wall:"))
test_w = int(input("width of wall:"))
coverage = 5
