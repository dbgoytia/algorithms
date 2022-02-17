# Standard Library
from turtle import RawTurtle
import random
import logging

# Third party modules

# Custom modules

# Configuration
LENGTH_FOOD_PIXELS = .5
WIDTH_FOOD_PIXELS = .5
WIDTH = 600
HEIGHT = 600
OFFSET = 15.0
LOG_LEVEL="DEBUG"

# Logging configuration
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


class Food(RawTurtle):

    '''
    Renders itself as food on the screen
    '''

    def __init__(self, canvas):
        super().__init__(canvas)
        self.penup()
        self.shapesize(stretch_len=LENGTH_FOOD_PIXELS, stretch_wid=WIDTH_FOOD_PIXELS)
        self.color('red')
        self.shape('circle')
        self.speed('fastest')
        random_x = random.randint(-WIDTH/2+OFFSET, WIDTH/2-OFFSET)
        random_y = random.randint(-HEIGHT/2+OFFSET, HEIGHT/2-OFFSET)
        self.goto(random_x, random_y)
        logger.debug(f'Food position: {self.pos()}')