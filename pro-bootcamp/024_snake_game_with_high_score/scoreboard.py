# std library
from turtle import Turtle
import logging

# third party modules

# custom modules
from config import SnakeConfig
from snake import Snake

# Logging configuration
logger = logging.getLogger(__file__)

class Scoreboard(Turtle):

    '''
    Renders as a scoreboard on the canvas
    '''


    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()


    def write_score(self):
        self.clear()
        logger.info(f'Score: {self.score}')
        self.penup()
        self.hideturtle()
        self.goto(0, SnakeConfig.height/2-SnakeConfig.offset)
        style = SnakeConfig.style
        self.color('black')
        self.write(f'Score: {self.score}', move=True, align="center", font=style)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()


    def game_over(self):
        self.color('white')
        self.goto(0,0)
        self.write('GAME OVER', align=SnakeConfig.allignment, font=SnakeConfig.style)