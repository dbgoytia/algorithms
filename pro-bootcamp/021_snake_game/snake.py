# Standard library
import logging
from turtle import RawTurtle
from turtle import TurtleScreen
import time

# Third party modulesc

# Custom modules

# Global setup
SPEED = 10
DEBUG_MODE = True
LOG_LEVEL = 'debug'
SHAPE_WIDTH_PIXELS = .5
SHAPE_HEIGHT_PIXELS = .5

# Logging configuration
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())

class Snake:


    body = []
    game_is_on = True
    screen = None


    def __init__(self, canvas):
        self.init_screen(canvas)
        self.init_controls()
        self.init_body(canvas)
        self.init_game()
    

    def init_screen(self, canvas):
        self.screen = TurtleScreen(canvas)


    def init_controls(self):
        # Controls, could be moved to a better configuration file
        self.screen.listen()
        self.screen.onkey(key='Right', fun=self.turn_right)
        self.screen.onkey(key='Left', fun=self.turn_left)
        self.screen.onkey(key='Up', fun=self.turn_up)
        self.screen.onkey(key='Down', fun=self.turn_down)
        self.screen.tracer(0) # Not sure if this is affecting the environment.


    def init_body(self, canvas):
        starting_positions = [(0, 0), (-SHAPE_WIDTH_PIXELS, 0), (-SHAPE_WIDTH_PIXELS, 0)]
        for pos in starting_positions:
            x = RawTurtle(canvas, shape='square')
            x.penup()
            x.goto(pos)
            x.color('white')
            x.speed('fastest')
            x.shapesize(SHAPE_WIDTH_PIXELS, SHAPE_WIDTH_PIXELS, 1)
            self.screen.bgcolor('black')
            self.body.append(x)


    def init_game(self):
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.1)
            self.move()
            

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
