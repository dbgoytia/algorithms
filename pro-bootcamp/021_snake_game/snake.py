# Standard library
import logging
from turtle import RawTurtle
from turtle import TurtleScreen
import time

# Third party modulesc

# Custom modules

# Global setup
SPEED = 5
DEBUG_MODE = True
LOG_LEVEL = 'debug'
SHAPE_WIDTH_PIXELS = .3
SHAPE_HEIGHT_PIXELS = .3

# Logging configuration
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())

class Snake:

    def __init__(self, canvas):
        # Screen setup
        self.screen = TurtleScreen(canvas)
        # Snake head setup
        self.snake = RawTurtle(canvas, shape='square')
        self.snake.penup()
        self.snake.color('white')
        self.snake.speed('fastest')
        self.snake.shapesize(SHAPE_WIDTH_PIXELS, SHAPE_WIDTH_PIXELS,  1)
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

        # Initialize the snake body      
        self.init_body(canvas)
        
        # Initialize the game
        self.init_game()
        

    def init_body(self, canvas):
        starting_positions = [(-SHAPE_WIDTH_PIXELS, 0), (-SHAPE_WIDTH_PIXELS, 0)]
        for pos in starting_positions:
            x = RawTurtle(canvas, shape='square')
            x.penup()
            x.goto(pos)
            x.color('red')
            x.speed('fastest')
            x.shapesize(SHAPE_WIDTH_PIXELS, SHAPE_WIDTH_PIXELS, 1)
            self.body.append(x)


    def init_game(self):
        while self.game_is_on:
            for seg_num in range( len(self.body) - 1 , 0 , -1):
                # Each piece moves to the position of the piece in front of it to get a good animation
                new_x = self.body[seg_num - 1].xcor()
                new_y = self.body[seg_num - 1].ycor()
                self.body[seg_num].goto(new_x, new_y)
            self.body[0].forward(SPEED)
            logger.debug(f'Head position is {self.body[0].pos()}')
            logger.debug(f'Head angle is {self.body[0].heading()}')


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
