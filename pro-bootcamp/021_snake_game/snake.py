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
        # Controls
        self.screen.listen()
        self.screen.onkey(key='Right', fun=self.move_right)
        self.screen.onkey(key='Left', fun=self.move_left)
        self.screen.onkey(key='Up', fun=self.move_up)
        self.screen.onkey(key='Down', fun=self.move_down)
        # # Test piece
        self.testpiece = RawTurtle(canvas, shape='square')
        self.testpiece.goto(-20,0)
        self.testpiece.penup()
        self.testpiece.color('red')
        # To move the entire snake
        self.body = [] # An array of turtles that contains all of the pieces required to be moved
        self.body.append(self.testpiece)
        self.screen.bgcolor('black')
        self.head = self.snake


    def move_right(self):
        logger.debug(f'Moving right')
        logger.debug(f'Turtle is currently facing at angle: {self.head.heading()}')
        if self.head.heading() != 0:
            self.head.setheading(0)
            logger.debug(f'Turtle turned, new angle: {self.head.heading()}')
        turn = self.head.pos()
        logger.debug(f'Setting the turn at: {turn}')
        self.head.forward(20)
        logger.debug(f'Head position: {self.head.pos()}')
        for x in self.body:
            x.forward(20)
            if x.pos() == turn:
                x.setheading(0)
                logger.debug(f'Body piece reached turn, turning')


    def move_left(self):
        logger.debug(f'Moving left')
        logger.debug(f'Turtle is currently facing at angle: {self.head.heading()}')
        if self.head.heading() != 180:
            self.head.setheading(180)
            logger.debug(f'Turtle turned, new angle: {self.head.heading()}')
        turn = self.head.pos()
        logger.debug(f'Setting the turn at: {turn}')
        self.head.forward(20)
        logger.debug(f'Head position: {self.head.pos()}')
        for x in self.body:
            x.forward(20)
            if x.pos() == turn:
                x.setheading(180)
                logger.debug(f'Body piece reached turn, turning')


    def move_down(self):
        logger.debug(f'Moving down')
        logger.debug(f'Turtle is currently facing at angle: {self.head.heading()}')
        if self.head.heading() != 270:
            self.head.setheading(270)
            logger.debug(f'Turtle turned, new angle: {self.head.heading()}')
        turn = self.head.pos()
        logger.debug(f'Setting the turn at: {turn}')
        self.head.forward(20)
        logger.debug(f'Head position: {self.head.pos()}')
        for x in self.body:
            x.forward(20)
            if x.pos() == turn:
                x.setheading(270)
                logger.debug(f'Body piece reached turn, turning')

    
    def move_up(self):
        logger.debug(f'Moving up')
        logger.debug(f'Turtle is currently facing at angle: {self.head.heading()}')
        # First only move the head to get the turn position
        if self.head.heading() != 90:
            self.head.setheading(90)
            logger.debug(f'Turtle turned, new angle: {self.head.heading()}')
        turn = self.head.pos()
        logger.debug(f'Setting the turn at: {turn}')
        self.head.forward(20)
        logger.debug(f'Head position: {self.head.pos()}')
        for x in self.body:
            x.forward(20)
            if x.pos() == turn:
                x.setheading(90)
                logger.debug(f'Body piece reached turn, turning')


if __name__ == '__main__':
    root = Tk()
    gameboard = GameBoard(root)
    root.mainloop()