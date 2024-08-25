import random

def generate_maze(n):
    maze = [['#'] * n for _ in range(n)]
    stack = [(0, 0)]
    visited = set((0, 0))
    maze[0][0] = 'S'

    while stack:
        current = stack[-1]
        neighbors = []

        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                neighbors.append((nx, ny))

        if neighbors:
            next_cell = random.choice(neighbors)
            stack.append(next_cell)
            visited.add(next_cell)
            maze[(current[0] + next_cell[0]) // 2][(current[1] + next_cell[1]) // 2] = ' '
            maze[next_cell[0]][next_cell[1]] = ' '
        else:
            stack.pop()

    maze[-1][-1] = 'E'
    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

def solve_maze(maze, start, end, path=[]):
    if start == end:
        return path
    x, y = start
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if maze[nx][ny] == ' ' or maze[nx][ny] == 'E':
            if (nx, ny) not in path:
                new_path = solve_maze(maze, (nx, ny), end, path + [(nx, ny)])
                if new_path:
                    return new_path
    return None

def maze_game():
    n = 21
    maze = generate_maze(n)
    print("Generated Maze:")
    print_maze(maze)
    solution = solve_maze(maze, (0, 0), (n-1, n-1))
    if solution:
        print("Solution Found!")
    else:
        print("No Solution Found.")

# Run the game
maze_game()
