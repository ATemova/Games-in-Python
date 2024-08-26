import random

class Game2048:
    def __init__(self):
        self.board = [[0] * 4 for _ in range(4)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.board[r][c] == 0]
        r, c = random.choice(empty_cells)
        self.board[r][c] = random.choice([2, 4])

    def move(self, direction):
        def slide(row):
            new_row = [i for i in row if i != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row[i + 1] = 0
            return [i for i in new_row if i != 0] + [0] * (4 - len(new_row))

        if direction == 'up':
            self.board = [list(row) for row in zip(*[slide(list(row)) for row in zip(*self.board)])]
        elif direction == 'down':
            self.board = [list(row) for row in zip(*[slide(list(row)[::-1])[::-1] for row in zip(*self.board)])]
        elif direction == 'left':
            self.board = [slide(row) for row in self.board]
        elif direction == 'right':
            self.board = [slide(row[::-1])[::-1] for row in self.board]
        self.add_new_tile()

    def display(self):
        for row in self.board:
            print("\t".join(str(num) if num != 0 else '.' for num in row))

    def play(self):
        while True:
            self.display()
            move = input("Enter move (up/down/left/right): ")
            self.move(move)
            if all(cell != 0 for row in self.board for cell in row):
                print("Game Over")
                break

game = Game2048()
game.play()
