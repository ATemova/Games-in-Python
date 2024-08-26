import random

class QuantumTicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_turn = "X"

    def display_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, x, y):
        if self.board[x][y] == " ":
            self.board[x][y] = self.current_turn
            if self.check_winner():
                print(f"{self.current_turn} wins!")
                return True
            self.current_turn = "O" if self.current_turn == "X" else "X"
        else:
            print("Invalid move")
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def play(self):
        while True:
            self.display_board()
            x, y = map(int, input("Enter your move (row col): ").split())
            if self.make_move(x, y):
                break

game = QuantumTicTacToe()
game.play()
