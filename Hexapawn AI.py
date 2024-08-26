class Hexapawn:
    def __init__(self, size=3):
        self.size = size
        self.board = [['W'] * size if i == 0 else ['.'] * size if i != size - 1 else ['B'] * size for i in range(size)]
        self.current_turn = 'W'

    def is_valid_move(self, start, end):
        if self.board[end[0]][end[1]] != '.':
            return False
        if self.current_turn == 'W' and end[0] == start[0] + 1:
            return True
        if self.current_turn == 'B' and end[0] == start[0] - 1:
            return True
        return False

    def make_move(self, start, end):
        if not self.is_valid_move(start, end):
            return False
        self.board[end[0]][end[1]] = self.current_turn
        self.board[start[0]][start[1]] = '.'
        self.current_turn = 'B' if self.current_turn == 'W' else 'W'
        return True

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def is_game_over(self):
        for i in range(self.size):
            if self.board[0][i] == 'B' or self.board[self.size-1][i] == 'W':
                return True
        return False

    def play(self):
        while not self.is_game_over():
            self.display_board()
            print(f"{self.current_turn}'s move.")
            start = tuple(map(int, input("Enter start position (row col): ").split()))
            end = tuple(map(int, input("Enter end position (row col): ").split()))
            if not self.make_move(start, end):
                print("Invalid move, try again.")
        print("Game Over.")

game = Hexapawn()
game.play()
