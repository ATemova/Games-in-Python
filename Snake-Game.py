import curses
import random

def snake_game():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.keypad(1)
    screen.timeout(100)

    snake_x = curses.COLS // 4
    snake_y = curses.LINES // 2
    snake = [(snake_y, snake_x), (snake_y, snake_x - 1), (snake_y, snake_x - 2)]
    food = (random.randint(1, curses.LINES - 2), random.randint(1, curses.COLS - 2))

    screen.addch(*food, curses.ACS_PI)

    key = curses.KEY_RIGHT

    while True:
        next_key = screen.getch()
        key = key if next_key == -1 else next_key

        new_head = (snake[0][0], snake[0][1])

        if key == curses.KEY_DOWN:
            new_head = (snake[0][0] + 1, snake[0][1])
        if key == curses.KEY_UP:
            new_head = (snake[0][0] - 1, snake[0][1])
        if key == curses.KEY_LEFT:
            new_head = (snake[0][0], snake[0][1] - 1)
        if key == curses.KEY_RIGHT:
            new_head = (snake[0][0], snake[0][1] + 1)

        snake.insert(0, new_head)

        if snake[0] == food:
            food = (random.randint(1, curses.LINES - 2), random.randint(1, curses.COLS - 2))
            screen.addch(*food, curses.ACS_PI)
        else:
            tail = snake.pop()
            screen.addch(*tail, ' ')

        if (snake[0][0] in [0, curses.LINES] or
            snake[0][1] in [0, curses.COLS] or
            snake[0] in snake[1:]):
            break

        screen.addch(*snake[0], curses.ACS_CKBOARD)

    curses.endwin()

# Run the game
snake_game()
