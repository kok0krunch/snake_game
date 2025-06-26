# 🐍 Snake Game (OOP Implementation)
The Snake Game is a classic arcade-style game where the player controls a snake that moves around the screen, collecting food to grow longer. The challenge increases as the snake grows, and the game ends if the snake collides with the walls or itself. This version uses Python and Tkinter to provide an interactive graphical interface with smooth gameplay and responsive controls. The fundamental gameplay mechanics were derived and further enhanced from the tutorial provided by @BroCode on YouTube.

In this version, the original procedural code has been refactored to incorporate the Four Fundamental Principles of Object-Oriented Programming (OOP)

# 🛠️ OOP Principles Applied:
✅ Encapsulation — Game objects such as the snake and food are represented as classes with controlled attributes and behaviors.

✅ Abstraction — Common functionality is abstracted into a base GameObject class to reduce redundancy.

✅ Inheritance — The Snake and Food classes inherit from the GameObject class to reuse common logic.

✅ Polymorphism — The draw() method is defined differently for each object (Snake segments use rectangles, Food uses ovals).

# 🎮 Features:
➥ Smooth, responsive snake movement via arrow keys

➥ Randomly placed food items to chase down

➥ Growing snake upon eating food

➥ Increasing difficulty as the score increases (speed gets faster)

➥ Collision detection (walls & self)

➥ Simple, clean GUI with Tkinter

➥ Game Over screen

# 🎨 Credits:
Original project inspiration & base code: @BroCode - Let's code a SNAKE GAME in python! 🐍

Video Link: [https://www.youtube.com/watch?v=bfRwxS5d0SI](https://www.youtube.com/watch?v=bfRwxS5d0SI)

# 📝 Notes:
This project was primarily created for educational purposes to demonstrate OOP concepts in Python with a fun, interactive game.
