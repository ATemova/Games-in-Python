class KnightTour:
    def __init__(self, N):
        self.N = N
        self.board = [[-1 for _ in range(N)] for _ in range(N)]
        self.moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]
        self.board[0][0] = 0
        self.solve(0, 0, 1)

    def is_safe(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] == -1

    def solve(self, x, y, movei):
        if movei == self.N * self.N:
            self.print_board()
            return True

        for move in self.moves:
            next_x, next_y = x + move[0], y + move[1]
            if self.is_safe(next_x, next_y):
                self.board[next_x][next_y] = movei
                if self.solve(next_x, next_y, movei + 1):
                    return True
                self.board[next_x][next_y] = -1
        return False

    def print_board(self):
        for row in self.board:
            print(' '.join(str(x).zfill(2) for x in row))

tour = KnightTour(8)
