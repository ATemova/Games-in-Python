import random

class World:
    def __init__(self, size):
        self.map = [['.' for _ in range(size)] for _ in range(size)]
        self.generate(size)

    def generate(self, size):
        for _ in range(size * size // 4):
            x, y = random.randint(0, size-1), random.randint(0, size-1)
            self.map[y][x] = random.choice(['T', 'M', 'C'])

    def display(self):
        for row in self.map:
            print(" ".join(row))

class RPG:
    def __init__(self):
        self.size = 10
        self.world = World(self.size)
        self.player_pos = [self.size // 2, self.size // 2]
        self.hp = 10
        self.inventory = []

    def move(self, direction):
        if direction == 'up':
            self.player_pos[0] -= 1
        elif direction == 'down':
            self.player_pos[0] += 1
        elif direction == 'left':
            self.player_pos[1] -= 1
        elif direction == 'right':
            self.player_pos[1] += 1
        self.resolve_encounter()

    def resolve_encounter(self):
        x, y = self.player_pos
        tile = self.world.map[x][y]
        if tile == 'M':
            if random.random() < 0.5:
                self.hp -= 2
                print("You fought a monster and lost 2 HP.")
            else:
                print("You fought a monster and won.")
            self.world.map[x][y] = '.'
        elif tile == 'C':
            print("You found a chest with a potion!")
            self.inventory.append('potion')
            self.world.map[x][y] = '.'
        elif tile == 'T':
            print("You encountered a trap and lost 3 HP.")
            self.hp -= 3
            self.world.map[x][y] = '.'

    def play(self):
        while self.hp > 0:
            self.world.display()
            move = input("Move (up/down/left/right): ").strip()
            self.move(move)
            print(f"HP: {self.hp}, Inventory: {self.inventory}")
        print("Game over.")

game = RPG()
game.play()
