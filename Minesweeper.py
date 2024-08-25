import random

def init_board(size, mines):
    board = [[0] * size for _ in range(size)]
    mine_positions = random.sample([(r, c) for r in range(size) for c in range(size)], mines)
    for r, c in mine_positions:
        board[r][c] = 'X'
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if 0 <= r + dr < size and 0 <= c + dc < size and board[r + dr][c + dc] != 'X':
                    board[r + dr][c + dc] += 1
    return board, mine_positions

def print_board(board, revealed):
    for r in range(len(board)):
        row = []
        for c in range(len(board)):
            if (r, c) in revealed:
                row.append(str(board[r][c]))
            else:
                row.append('.')
        print(" ".join(row))

def minesweeper_game():
    size = 8
    mines = 10
    board, mine_positions = init_board(size, mines)
    revealed = set()

    while True:
        print_board(board, revealed)
        r, c = map(int, input("Enter row and column to reveal: ").split())
        
        if (r, c) in mine_positions:
            print("Boom! You hit a mine!")
            break
        
        revealed.add((r, c))
        if len(revealed) == size * size - mines:
            print("Congratulations! You cleared the minefield!")
            break

# Run the game
minesweeper_game()
