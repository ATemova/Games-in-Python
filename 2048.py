import random

def init_board():
    return [[0] * 4 for _ in range(4)]

def add_new_tile(board):
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_tiles:
        return
    i, j = random.choice(empty_tiles)
    board[i][j] = 2 if random.random() < 0.9 else 4

def compress(board):
    new_board = [[0] * 4 for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][position] = board[i][j]
                position += 1
    return new_board

def merge(board):
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] and board[i][j] != 0:
                board[i][j] *= 2
                board[i][j + 1] = 0
    return board

def reverse(board):
    return [row[::-1] for row in board]

def transpose(board):
    return [list(row) for row in zip(*board)]

def move_left(board):
    board = compress(board)
    board = merge(board)
    board = compress(board)
    return board

def move_right(board):
    board = reverse(board)
    board = move_left(board)
    board = reverse(board)
    return board

def move_up(board):
    board = transpose(board)
    board = move_left(board)
    board = transpose(board)
    return board

def move_down(board):
    board = transpose(board)
    board = move_right(board)
    board = transpose(board)
    return board

def check_game_status(board):
    for row in board:
        if 2048 in row:
            return "WON"
    for row in board:
        if 0 in row:
            return "GAME NOT OVER"
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1]:
                return "GAME NOT OVER"
    for j in range(4):
        for i in range(3):
            if board[i][j] == board[i + 1][j]:
                return "GAME NOT OVER"
    return "LOST"

def print_board(board):
    for row in board:
        print(" | ".join([str(num).ljust(4) for num in row]))
        print("-" * 21)

def game_2048():
    board = init_board()
    add_new_tile(board)
    add_new_tile(board)
    print("Welcome to 2048!")
    
    while True:
        print_board(board)
        move = input("Enter move (W/A/S/D): ").lower()

        if move == 'w':
            board = move_up(board)
        elif move == 's':
            board = move_down(board)
        elif move == 'a':
            board = move_left(board)
        elif move == 'd':
            board = move_right(board)
        else:
            print("Invalid move!")
            continue

        add_new_tile(board)

        status = check_game_status(board)
        if status == "WON":
            print("Congratulations! You won!")
            break
        elif status == "LOST":
            print("Game over! You lost.")
            break

# Run the game
game_2048()
