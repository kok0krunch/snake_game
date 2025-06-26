class GameObject:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.color = color
    
    def draw(self):
        raise NotImplementedError("Subclasses must implement draw()")