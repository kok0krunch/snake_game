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
    
    def next_turn(self):
        if not self.running:
            return

        x, y = self.snake.coordinates[0]

        if self.direction == "up":
            y -= SPACE_SIZE
        elif self.direction == "down":
            y += SPACE_SIZE
        elif self.direction == "left":
            x -= SPACE_SIZE
        elif self.direction == "right":
            x += SPACE_SIZE
            
        self.snake.coordinates.insert(0, (x, y))
        square = self.snake.draw_segment(x, y)
        self.snake.squares.insert(0, square) 
        
        if x == self.food.coordinates[0] and y == self.food.coordinates[1]:
            self.score += 1
            self.label.config(text="Score:{}".format(self.score))
            self.canvas.delete("food")
            self.food = Food(self.canvas)
            if self.score % 5 == 0 and self.speed > 30:
                self.speed -= 10
        else:
            del self.snake.coordinates[-1]
            self.canvas.delete(self.snake.squares[-1])
            del self.snake.squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.window.after(self.speed, self.next_turn)
        
    def change_direction(self, new_direction):
        if new_direction == 'left' and self.direction != 'right':
            self.direction = new_direction
        elif new_direction == 'right' and self.direction != 'left':
            self.direction = new_direction
        elif new_direction == 'up' and self.direction != 'down':
            self.direction = new_direction
        elif new_direction == 'down' and self.direction != 'up':
            self.direction = new_direction