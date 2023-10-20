import random


def computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices).title()

def determine_winner(computer, player):
    if computer == player:
        return "Game Tied"
    if player == "Rock" and computer == "Paper":
        return "You lose"
    if player == "Scissors" and computer == "Rock":
        return "You lose"
    if player == "Paper" and computer == "Scissors":
        return "You lose"
    else:
        return "You win"

while True:
    player = input("Enter your weapon or type 'I Quit' to exit the game ").title()
    if player == ('I Quit'):
        print ("Thank you for playing")
        break
    if player not in ['Rock', 'Paper', 'Scissors']:
        print ("pick Rock Paper or Scissors")
    else: 
        computer = computer_choice()
        result = determine_winner(player,computer)
        print(f'computer choice {computer}. {result} ')
