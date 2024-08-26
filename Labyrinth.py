import random

def generate_maze(w, h):
    maze = [[1] * w for _ in range(h)]
    def carve_passages(cx, cy):
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        random.shuffle(directions)
        for (dx, dy) in directions:
            nx, ny = cx + dx * 2, cy + dy * 2
            if 1 <= nx < w-1 and 1 <= ny < h-1 and maze[ny][nx] == 1:
                maze[cy + dy][cx + dx] = 0
                maze[ny][nx] = 0
                carve_passages(nx, ny)
    carve_passages(1, 1)
    maze[1][0] = 0
    maze[h-2][w-1] = 0
    return maze

def solve_maze(maze):
    from heapq import heappop, heappush
    h, w = len(maze), len(maze[0])
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    start, goal = (1, 0), (h-2, w-1)
    open_set = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    while open_set:
        _, current = heappop(open_set)
        if current == goal:
            break
        for d in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + d[0], current[1] + d[1])
            if 0 <= neighbor[0] < h and 0 <= neighbor[1] < w and maze[neighbor[0]][neighbor[1]] == 0:
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristic(goal, neighbor)
                    heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

maze = generate_maze(21, 21)
solution = solve_maze(maze)
for row in maze:
    print("".join(["#" if x == 1 else " " for x in row]))
for (y, x) in solution:
    maze[y][x] = 2
print("\nSolved:\n")
for row in maze:
    print("".join(["#" if x == 1 else "X" if x == 2 else " " for x in row]))
