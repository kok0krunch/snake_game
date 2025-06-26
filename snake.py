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