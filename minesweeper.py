import random

class Minesweeper:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[0 for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.place_mines()

    def place_mines(self):
        for _ in range(self.num_mines):
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            while self.board[x][y] == "M":
                x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            self.board[x][y] = "M"
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < self.size and 0 <= y + dy < self.size and self.board[x+dx][y+dy] != "M":
                        self.board[x+dx][y+dy] += 1

    def display_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.revealed[i][j]:
                    print(self.board[i][j], end=" ")
                else:
                    print("-", end=" ")
            print()

    def reveal(self, x, y):
        if self.board[x][y] == "M":
            print("Game Over")
            return True
        self.revealed[x][y] = True
        if self.board[x][y] == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if 0 <= x + dx < self.size and 0 <= y + dy < self.size and not self.revealed[x+dx][y+dy]:
                        self.reveal(x+dx, y+dy)
        return False

    def play(self):
        while True:
            self.display_board()
            x, y = map(int, input("Enter your move (row col): ").split())
            if self.reveal(x, y):
                break
        print("Game Over")
        self.display_board()

game = Minesweeper(5, 5)
game.play()
