# Standard library
from turtle import RawTurtle
from turtle import TurtleScreen
import logging
from tkinter import Tk
from tkinter import Label
from tkinter import Canvas

# Third party modules 

# Custom modules

# Global Setup
WIDTH = 600
HEIGHT = 600
SPEED = 5
DEBUG_MODE = True

# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


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

class Snake:

    def __init__(self, canvas):
        # Screen setup
        self.screen = TurtleScreen(canvas)
        # Snake head setup
        self.snake = RawTurtle(canvas, shape='square')
        self.snake.penup()
        self.snake.color('white')
        self.snake.speed('fastest')
        self.snake.shapesize(.5, .5,  1)
        # Controls
        self.screen.listen()
        self.screen.onkey(key='Right', fun=self.turn_right)
        self.screen.onkey(key='Left', fun=self.turn_left)
        self.screen.onkey(key='Up', fun=self.turn_up)
        self.screen.onkey(key='Down', fun=self.turn_down)
        self.screen.tracer(0)
        
        # To move the entire snake
        self.body = [] # An array of turtles that contains all of the pieces required to be moved
        self.body.append(self.snake)
        self.screen.bgcolor('black')
        self.game_is_on = True

        if DEBUG_MODE:
            # Test piece
            self.testpiece = RawTurtle(canvas, shape='square')
            self.testpiece.goto(-50,0)
            self.testpiece.penup()
            self.testpiece.color('red')
            self.testpiece.speed('fastest')
            self.testpiece.shapesize(.5, .5,  1)
            self.body.append(self.testpiece)


        while self.game_is_on:
            for seg_num in range( len(self.body) - 1 , 0 , -1):
                # Each piece moves to the position of the piece in front of it to get a good animation
                new_x = self.body[seg_num - 1].xcor()
                new_y = self.body[seg_num - 1].ycor()
                self.body[seg_num].goto(new_x, new_y)
            self.body[0].forward(SPEED)


    def turn_right(self):
        logger.debug(f'Moving right')
        for x in self.body:
            x.setheading(0)     


    def turn_left(self):
        logger.debug(f'Moving left')
        for x in self.body:
            x.setheading(180)     


    def turn_down(self):
        logger.debug(f'Moving down')
        for x in self.body:
            x.setheading(270)     

    
    def turn_up(self):
        logger.debug(f'Moving up')
        for x in self.body:
            x.setheading(90)   


if __name__ == '__main__':
    root = Tk()
    gameboard = GameBoard(root)
    root.mainloop()