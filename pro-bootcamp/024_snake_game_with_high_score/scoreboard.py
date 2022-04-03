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
        if not self.is_empty_scoreboard():
            self.get_high_score()
        else:
            self.high_score = 0
        self.write_score()


    def get_high_score(self) -> None:
        """
        Gets high score from file
        """
        with open(file='data.txt', mode='r') as f:
            saved_high_score = f.read()
        self.high_score = int(saved_high_score)

    
    def is_empty_scoreboard(self) -> bool:
        """
        Checks if scoreboard is empty

        Returns:
            bool: True if scoreboard is empty
        """
        with open(file='data.txt', mode='r') as f:
            if not f.read():
                return True
        return False
        

    def write_score(self) -> None:
        """
        Writes scoreboard on screen using Turtle
        """
        self.clear()
        logger.info(f'Score: {self.score}')
        self.penup()
        self.hideturtle()
        self.goto(0, SnakeConfig.height/2-SnakeConfig.offset)
        style = SnakeConfig.style
        self.color('black')
        self.write(f'Score: {self.score}, High score: {self.high_score}', move=True, align="center", font=style)


    def increase_score(self):
        """
        Increases score by one each time you eat food
        """
        self.score += 1
        self.clear()
        self.write_score()

    
    def reset(self):
        """
        Resets scoreboard on screen when you loose.
        You can loose by hitting a wall, or your own tail.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open(file='data.txt', mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.write_score()