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
SPEED=30
OFFSET=30

class Ball(Turtle):

    
    def __init__(self) -> None:
        """
        Creates the ball on screen
        """
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    
    def bounce_y(self):
        """
        bounces the ball on the top and bottom portions of the screen
        """
        self.y_move *= -1

    
    def bounce_x(self) -> list:
        """
        bounces the ball on the left and right portions of the screen
        """
        self.x_move *= -1
        self.move_speed * 0.9 # Gives speed each time a paddle hits the ball


    def reset_ball(self) -> None:
        """
        Resets the ball position and sends it to the center of the screen
        """
        self.goto((0,0))
        self.bounce_x()
        self.move_speed = 0.1
    
    def move(self) -> None:
        """
        Moves the ball on screen
        """
        logger.debug(f'Ball position: {self.pos()}')
        logger.debug(f'X move: {self.x_move}')
        logger.debug(f'Y move: {self.y_move}')
    
        if self.ycor() > (300 - OFFSET) and self.ycor() > (-300 + OFFSET):
            self.bounce_y()
        
        if self.ycor() < (-300 + OFFSET) and self.ycor() < (300 - OFFSET):
            self.bounce_y()

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


