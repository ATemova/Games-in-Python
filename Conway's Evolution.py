import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class GameOfLife:
    def __init__(self, size):
        self.size = size
        self.grid = np.random.choice([1, 0], size * size, p=[0.2, 0.8]).reshape(size, size)

    def update(self, _):
        new_grid = self.grid.copy()
        for i in range(self.size):
            for j in range(self.size):
                total = (self.grid[i, (j-1)%self.size] + self.grid[i, (j+1)%self.size] +
                         self.grid[(i-1)%self.size, j] + self.grid[(i+1)%self.size, j] +
                         self.grid[(i-1)%self.size, (j-1)%self.size] + self.grid[(i-1)%self.size, (j+1)%self.size] +
                         self.grid[(i+1)%self.size, (j-1)%self.size] + self.grid[(i+1)%self.size, (j+1)%self.size])
                if self.grid[i, j] == 1:
                    if (total < 2) or (total > 3):
                        new_grid[i, j] = 0
                else:
                    if total == 3:
                        new_grid[i, j] = 1
        self.grid = new_grid
        plt.cla()
        plt.imshow(self.grid, cmap='binary')

    def animate(self):
        fig = plt.figure()
        ani = animation.FuncAnimation(fig, self.update, interval=200)
        plt.show()

game = GameOfLife(100)
game.animate()
