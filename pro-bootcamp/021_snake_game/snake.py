# Standard library
import logging
from turtle import RawTurtle

# Third party modulesc

# Custom modules

# Global setup
SPEED = 10
DEBUG_MODE = True
LOG_LEVEL = 'INFO'
SHAPE_WIDTH_PIXELS = .5
SHAPE_HEIGHT_PIXELS = .5

# Logging configuration
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())

class Snake(RawTurtle):
    '''
    Controls the snake in the game
    '''

    body = []
    screen = None

    def __init__(self, canvas):
        super().__init__(canvas)
        self.canvas = canvas
        self.init_body()
        self.head = self.body[0]
    

    def init_body(self):
        starting_positions = [(0, 0), (-SHAPE_WIDTH_PIXELS, 0), (-SHAPE_WIDTH_PIXELS, 0)]
        for pos in starting_positions:
            self.add_segment(pos)
            

    def add_segment(self, pos):
        x = RawTurtle(self.canvas, shape='square')
        x.penup()
        x.goto(pos)
        x.color('white')
        x.speed('fastest')
        x.shapesize(SHAPE_WIDTH_PIXELS, SHAPE_WIDTH_PIXELS, 1)
        x.screen.bgcolor('black')
        self.body.append(x)


    def extend(self):
        self.add_segment(self.body[-1].pos())

    def move(self):
        for seg_num in range( len(self.body) - 1 , 0 , -1): # Start with a three segment snake
            # Each piece moves to the position of the piece in front of it to get a good animation
            new_x = self.body[seg_num - 1].xcor()
            new_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(new_x, new_y)
        self.body[0].forward(SPEED)
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
