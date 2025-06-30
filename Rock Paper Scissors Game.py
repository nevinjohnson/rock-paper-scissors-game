#Ask the user to make a choice
#If the choice is not valid
# Print an error
#Let the computer make a choice
#print choices(emojis)
#Determine the winner
#Ask the user if they want to continue
#If not
# Terminate

import random

ROCK ='r'
SCISSORS = 's'
PAPER = 'P'

emojis = {'ROCK':'🪨','PAPER':'🗞️','SCISSORS':'✂️'}
choices = tuple(emojis.keys())
def get_user_choice():
   while True:
    user_choice = input('Rock,Paper,Scissors ??? (r/p/s):').lower()
    if user_choice in choices:
        return user_choice
    else:
        print('invalid choice')
        
    
def display_choices(user_choice, computer_choice):
    print(f'You chose: {emojis[user_choice]}')
    print(f'I chose: {emojis[computer_choice]}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
     print('ohhh its a tie')
    elif(
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == ROCK)):
     print('you won')
    else:
       print('you lose')

def play_game():
 while True:    
    user_choice = get_user_choice()

    computer_choice = random.choice(choices)
    
    display_choices(user_choice, computer_choice)
    determine_winner(user_choice, computer_choice)

    should_continue=input('Wanna play one more ??? (y/n): ').lower()
    if should_continue == 'n':
       break

play_game()