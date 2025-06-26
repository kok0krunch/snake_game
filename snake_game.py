from snake import Snake
from food import Food

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50

class SnakeGame:
    def __init__(self, window, canvas, label):
        self.window = window
        self.canvas = canvas
        self.label = label
        self.score = 0
        self.direction = 'down'
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.running = True
        self.speed = SPEED
        
        self.window.bind('<Left>', lambda event: self.change_direction('left'))
        self.window.bind('<Right>', lambda event: self.change_direction('right'))
        self.window.bind('<Up>', lambda event: self.change_direction('up'))
        self.window.bind('<Down>', lambda event: self.change_direction('down'))

        self.next_turn()