import random


def computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def determine_winner(computer, player):
    if computer == player:
        return "Game Tied"
    elif player == "Rock" and computer == "Paper":
        return "You lose"
    elif player == "Scissors" and computer == "Rock":
        return "You lose"
    elif player == "Paper" and computer == "Scissors":
        return "You lose"
    else:
        return "You win"
    