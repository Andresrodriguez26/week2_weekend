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
    
player_score = 0
computer_score = 0

while True:
    player_input = input("Enter your weapon or type 'I Quit' to exit the game ").title()
    if player_input == ('I Quit'):
        print ("Thank you for playing")
        break
    if player_input not in ['Rock', 'Paper', 'Scissors']:
        print ("pick Rock Paper or Scissors")
    else: 
        computer = computer_choice()
        result = determine_winner(computer, player_input)
        print(f'computer choice {computer}. {result} ')

        if result == "You win":
            player_score += 1
        elif result == "You lose":
            computer_score += 1
    print(f"Your score: {player_score} | Computer score: {computer_score} ")

