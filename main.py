from tkinter import *
from snake_game import SnakeGame

GAME_WIDTH = 700
GAME_HEIGHT = 700
BACKGROUND_COLOR = "#000000"

def main():
    window = Tk()
    window.title("Snake game")
    window.resizable(False, False)

    score = 0

    label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    game = SnakeGame(window, canvas, label)

    window.mainloop()