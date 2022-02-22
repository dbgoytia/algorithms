# Standard library
from turtle import Turtle
import logging
from math import pi

# Third party modules

# Custom modules


# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


# Global Configuration
SHAPE='circle'
COLOR='red'
SPEED=10

class Ball(Turtle):

    
    def __init__(self) -> None:
        """
        Creates the ball on screen
        """
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()

    
    def move(self) -> None:
        """
        Moves the ball on screen
        """
        new_x = self.xcor() + SPEED
        new_y = self.ycor() + SPEED
        self.goto(new_x, new_y)

