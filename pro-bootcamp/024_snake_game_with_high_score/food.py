# Standard Library
from tkinter import OFF
from turtle import Turtle
import random
import logging

# Third party modules

# Custom modules
from config import SnakeConfig

# Logging configuration
logger = logging.getLogger(__file__)


class Food(Turtle):

    '''
    Renders itself as food on the screen
    '''

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=SnakeConfig.len_food_pixels, stretch_wid=SnakeConfig.width_food_pixels, outline=1)
        self.color('gray', 'green')
        self.shape('square')
        self.speed('fastest')
        random_x = self.random_food(-SnakeConfig.width/2+SnakeConfig.offset, SnakeConfig.width/2-SnakeConfig.offset)
        random_y = self.random_food(-SnakeConfig.height/2+SnakeConfig.offset, SnakeConfig.height/2-SnakeConfig.offset)
        self.goto(random_x, random_y)
        logger.debug(f'Food position: {self.pos()}')


    def random_food(self, min, max, base=10):
        x = random.randint(min, max)
        return base * round(x/base)


    def refresh(self):
        random_x = self.random_food(-SnakeConfig.width/2+SnakeConfig.offset, SnakeConfig.width/2-SnakeConfig.offset)
        random_y = self.random_food(-SnakeConfig.height/2+SnakeConfig.offset, SnakeConfig.height/2-SnakeConfig.offset)
        self.goto(random_x, random_y)