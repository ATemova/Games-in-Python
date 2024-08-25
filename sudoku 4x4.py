def print_sudoku(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    for i in range(4):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                for num in range(1, 5):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def mini_sudoku():
    board = [
        [1, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 0, 0, 3],
        [0, 4, 0, 0]
    ]
    
    print("Mini-Sudoku 4x4")
    print("Initial Board:")
    print_sudoku(board)

    if solve_sudoku(board):
        print("\nSolved Board:")
        print_sudoku(board)
    else:
        print("No solution exists.")

mini_sudoku()
