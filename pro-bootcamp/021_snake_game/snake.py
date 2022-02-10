# Standard library
# from turtle import Screen
from turtle import RawTurtle
from turtle import TurtleScreen

# Third party modules
from tkinter import Tk
from tkinter import Label
from tkinter import Canvas


# Custom modules

# Global Setup
WIDTH = 600
HEIGHT = 600


class GameBoard:
    
    
    def __init__(self, master):
        self.parent = master
        master.title('Snake')
        self.label = Label(master, text='Game on!')
        self.label.pack()
        self.canvas = Canvas(master)
        self.canvas.config(width=WIDTH, height=HEIGHT)
        self.canvas.pack()

        # Init snake
        self.init_snake()
        
    def init_snake(self):
        self.screen = TurtleScreen(self.canvas)
        self.snake = RawTurtle(self.canvas, shape='square')
        self.snake.color('white')
        self.screen.bgcolor('black')





if __name__ == '__main__':
    root = Tk()
    gameboard = GameBoard(root)
    root.mainloop()