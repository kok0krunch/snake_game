import random
from game_object import GameObject

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
FOOD_COLOR = "#FF0000"

class Food(GameObject):
    def __init__(self, canvas):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        super().__init__(canvas, x, y, SPACE_SIZE, FOOD_COLOR)
        self.coordinates = (x, y)
        self.oval = self.draw()