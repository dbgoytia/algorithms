# Standard library
from tkinter import Tk
from tkinter import Label
from tkinter import Canvas
import time
from turtle import TurtleScreen


# Third party modules 

# Custom modules
from snake import Snake
from food import Food

# Global Setup
WIDTH = 600
HEIGHT = 600
LENGTH_FOOD_PIXELS = .3
WIDTH_FOOD_PIXELS = .3

class GameBoard:

    
    def __init__(self, master):
        self.parent = master
        master.title('Snake')
        self.label = Label(master, text='Game on!')
        self.label.pack()
        self.canvas = Canvas(master)
        self.canvas.config(width=WIDTH, height=HEIGHT, background='black')
        self.canvas.pack()
        # Init the screen
        self.init_screen()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.game_is_on = True
        self.init_controls()
        self.init_game()


    def init_screen(self):
        self.screen = TurtleScreen(self.canvas)
        self.screen.tracer(0)


    def init_game(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.snake.move()
            self.detect_colision()
    

    def init_controls(self):
        # Controls, could be moved to a better configuration file
        self.screen.listen()
        self.screen.onkey(key='Right', fun=self.snake.turn_right)
        self.screen.onkey(key='Left', fun=self.snake.turn_left)
        self.screen.onkey(key='Up', fun=self.snake.turn_up)
        self.screen.onkey(key='Down', fun=self.snake.turn_down)


    def detect_colision(self):
        if self.snake.head.distance(self.food) < 10:
            self.food.refresh()



if __name__ == '__main__':
    root = Tk()
    # root.attributes('-alpha',0.5)
    gameboard = GameBoard(root)
    root.mainloop()
