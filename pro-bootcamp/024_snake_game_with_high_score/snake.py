# Standard library
import logging
from turtle import Turtle
from collections import deque

# Third party modulesc

# Custom modules
from config import SnakeConfig

# Logger
logger = logging.getLogger(__file__)


class Snake(Turtle):
    '''
    Controls the snake in the game
    '''

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.body = []
        self.init_body()
        self.head = self.body[0]
    

    def init_body(self):
        starting_positions = [(0, 0), (-0.5, 0), (-1, 0)]
        for pos in starting_positions:
            self.add_segment(pos)

    
    def reset(self):
        for seg in self.body:
            seg.goto(1000, 1000)
        self.body.clear()
        self.init_body()
        self.head = self.body[0]
        

    def add_segment(self, pos:list):
        """
        Adds a segment on screen represting a piece of the snake

        Args:
            pos (list): A touple containing x, y coordinates
        """
        x = Turtle(shape='square')
        x.penup()
        x.goto(pos)
        x.color('grey', 'blue')
        x.speed('fastest')
        x.shapesize(SnakeConfig.shape_width_pixels, SnakeConfig.shape_height_pixels, 1)
        self.body.append(x)


    def extend(self):
        self.add_segment(self.body[-1].pos())


    def move(self):        
        for seg_num in range( len(self.body) - 1 , 0 , -1): # Start with a three segment snake
            # Each piece moves to the position of the piece in front of it to get a good animation
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.body[0].forward(SnakeConfig.speed)
        logger.debug(f'Head position is {self.body[0].pos()}')
        logger.debug(f'Head angle is {self.body[0].heading()}')


    def turn_right(self):
        logger.debug(f'Moving right')
        if self.body[0].heading() != 180:
            for x in self.body:
                x.setheading(0)     


    def turn_left(self):
        logger.debug(f'Moving left')
        if self.body[0].heading() != 0:
            for x in self.body:
                x.setheading(180)


    def turn_down(self):
        logger.debug(f'Moving down')
        if self.body[0].heading() != 90:
            for x in self.body:
                x.setheading(270)   

    
    def turn_up(self):
        logger.debug(f'Moving up')
        if self.body[0].heading() != 270:
            for x in self.body:
                x.setheading(90)   
