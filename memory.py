import random

def print_board(board, revealed):
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            if revealed[i][j]:
                row.append(board[i][j])
            else:
                row.append('*')
        print(" ".join(row))

def memory_match():
    cards = list("AABBCCDD")
    random.shuffle(cards)
    board = [cards[i:i+4] for i in range(0, len(cards), 4)]
    revealed = [[False] * 4 for _ in range(4)]
    matches = 0
    turns = 0

    print("Memory Match Game")
    print("Try to find matching pairs of cards.")
    
    while matches < 8:
        print_board(board, revealed)
        try:
            row1, col1 = map(int, input("Enter the coordinates of the first card (row col): ").split())
            row2, col2 = map(int, input("Enter the coordinates of the second card (row col): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers for coordinates.")
            continue

        if revealed[row1][col1] or revealed[row2][col2]:
            print("One or both cards are already revealed.")
            continue
        
        revealed[row1][col1] = True
        revealed[row2][col2] = True
        print_board(board, revealed)
        
        if board[row1][col1] == board[row2][col2]:
            print("It's a match!")
            matches += 1
        else:
            print("Not a match.")
            revealed[row1][col1] = False
            revealed[row2][col2] = False
        
        turns += 1

    print(f"Congratulations! You've matched all pairs in {turns} turns.")

memory_match()
