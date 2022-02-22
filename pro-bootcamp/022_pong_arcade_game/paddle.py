# Standard library
import logging
from turtle import Turtle

# Third party modules


# Custom modules


# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


# Global Configuration
COLOR='white'
SHAPE='square'
STRETCH_WIDTH=5
STRECH_LENGTH=1
SPEED=20


class Paddle(Turtle):


    def __init__(self, x, y):
        """
        Initializes the paddle on screen

        Receives:
            x: An X coordinate to draw the center of the paddle on screen
            y: A Y coordinate to draw the paddle in
        """
        super().__init__()
        self.color(COLOR)
        self.shape(SHAPE)
        self.penup()
        self.speed('fastest')
        self.goto(x, y)
        self.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRECH_LENGTH)


    def detect_colission_with_ball(self):
        """
        Detects colission with the ball to bounce back
        """
        pass


    def move_up(self):
        logger.debug('Pressing up key')
        new_y = self.ycor() + SPEED
        self.goto(self.xcor(), new_y)


    def move_down(self):
        logger.debug('Pressing down key')
        new_y = self.ycor() - SPEED
        self.goto(self.xcor(), new_y)


