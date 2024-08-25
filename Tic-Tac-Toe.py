def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    
    for _ in range(9):
        print(f"Player {current_player}'s turn.")
        row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
        
        if board[row][col] == " ":
            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                return
            
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That spot is already taken!")

    print("It's a draw!")

# Run the game
tic_tac_toe()
