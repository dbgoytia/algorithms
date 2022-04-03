# Standard library
from turtle import Screen
import logging
import time
import sys


# Third party modules 

# Custom modules
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from config import SnakeConfig


# Logging configuration
FORMAT =  '%(asctime)s:%(levelname)s:%(message)s'
DATEFMT = '%m/%d/%Y %I:%M:%S %p'
logging.basicConfig(format=FORMAT, datefmt=DATEFMT)
logger = logging.getLogger()
LOG_LEVEL='INFO'
logger.setLevel(LOG_LEVEL.upper())


class GameBoard:
    """
    Class responsible for the game UI
    """

    def __init__(self):
        self.init_screen()
        self.snake = Snake()
        self.food = Food()
        self.game_is_on = True
        self.init_controls()
        self.scoreboard = Scoreboard()
        self.init_game()


    def init_screen(self):
        # self.screen = TurtleScreen(self.canvas)
        self.screen = Screen()
        self.screen.setup(width=SnakeConfig.width, height=SnakeConfig.height)
        self.screen.tracer(0)
        

    def init_game(self):
        logger.info('Starting snake game')
        while self.game_is_on:
            self.screen.update()
            self.snake.move()
            self.detect_colision()
            time.sleep(0.1)


    def init_controls(self):
        # Controls, could be moved to a better configuration file
        self.screen.listen()
        self.screen.onkey(key='Right', fun=self.snake.turn_right)
        self.screen.onkey(key='Left', fun=self.snake.turn_left)
        self.screen.onkey(key='Up', fun=self.snake.turn_up)
        self.screen.onkey(key='Down', fun=self.snake.turn_down)


    def detect_colision(self):

        # Detect collission with food
        if self.snake.head.distance(self.food) < 5:
            self.scoreboard.increase_score()
            self.food.refresh()
            self.snake.extend()

        if SnakeConfig.width/2  - abs(self.snake.head.xcor()) < SnakeConfig.shape_width_pixels \
            or SnakeConfig.height/2 - abs(self.snake.head.ycor()) < SnakeConfig.shape_height_pixels:
            logger.info('You lose')
            self.game_is_on = False
            self.scoreboard.game_over()


        # Detect colission with own tail
        for segment in self.snake.body[1:]:
            if self.snake.head.distance(segment) < 5:
                logger.debug(f'distance: {self.snake.head.distance(segment)}')
                logger.debug(f'head: {self.snake.head.pos()}, segment: {segment.pos()}')
                self.game_is_on = False
                self.scoreboard.game_over()
        
    
if __name__ == '__main__':
    gameboard = GameBoard()
