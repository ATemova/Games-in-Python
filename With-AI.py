import random

def rock_paper_scissors():
    moves = ['rock', 'paper', 'scissors']
    ai_move = random.choice(moves)

    print("Welcome to Rock, Paper, Scissors!")
    player_move = input("Enter your move (rock, paper, or scissors): ").lower()

    if player_move not in moves:
        print("Invalid move! You lose by default.")
        return

    print(f"AI chose {ai_move}.")

    if player_move == ai_move:
        print("It's a draw!")
    elif (player_move == 'rock' and ai_move == 'scissors') or \
         (player_move == 'scissors' and ai_move == 'paper') or \
         (player_move == 'paper' and ai_move == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Run the game
rock_paper_scissors()
