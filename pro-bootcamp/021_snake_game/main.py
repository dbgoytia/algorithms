# Standard library
from tkinter import Tk
from tkinter import Label
from tkinter import Canvas

# Third party modules 

# Custom modules
from snake import Snake

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
        Snake(self.canvas)


if __name__ == '__main__':
    root = Tk()
    gameboard = GameBoard(root)
    root.mainloop()