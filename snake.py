from game_object import GameObject

BODY_PARTS = 3
SPACE_SIZE = 50
SNAKE_COLOR = "#0FFF07"

class Snake(GameObject):
    def __init__(self, canvas):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.canvas = canvas
        for i in range(0, BODY_PARTS):
            self.coordinates.append((0, 0))
            self.squares.append(self.draw_segment(0, 0))
            
    def draw_segment(self, x, y):
        return self.canvas.create_rectangle(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake"
        )