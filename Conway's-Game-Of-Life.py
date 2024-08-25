import random
import time
import os

def init_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    os.system('clear')
    for row in grid:
        print("".join(['█' if cell else ' ' for cell in row]))
    time.sleep(0.5)

def count_neighbors(grid, row, col):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            count += grid[r][c]
    return count

def next_generation(grid):
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[r][c] = 0
            elif grid[r][c] == 0 and neighbors == 3:
                new_grid[r][c] = 1
            else:
                new_grid[r][c] = grid[r][c]
    return new_grid

def game_of_life():
    rows, cols = 20, 50
    grid = init_grid(rows, cols)
    
    while True:
        print_grid(grid)
        grid = next_generation(grid)

# Run the game
game_of_life()
