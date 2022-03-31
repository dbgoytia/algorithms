# standard library
from turtle import Turtle
import logging

# third party modules

# custom modules


# configuration
LOG_LEVEL="INFO"
ALIGNMENT="center"
STYLE=('Courier', 15, 'italic')

# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())

class Scoreboard(Turtle):

    """
    The class responsible for keeping score of the game
    """

    def __init__(self) -> None:
        """
        Initializes scoreboard on screen
        """
        super().__init__()
        self.level = 1
        self.write_score()


    def write_score(self) -> None:
        """
        Writes score on the scoreboard
        """
        self.clear()
        logger.info(f'Level: {self.level}')
        self.penup()
        self.hideturtle()
        self.goto(-200, 200)
        self.color('black')
        self.write(
            f'Level: {self.level}',
            move=True,
            align=ALIGNMENT,
            font=STYLE)
        

    def increase_score(self) -> None:
        """
        Increases the level by one
        """
        self.level += 1

    
    def game_over(self) -> None:
        """
        Writes the gameover on screen
        """
        self.clear()
        self.write(
            f'Gameover, score: {self.level}',
            move=False,
            align=ALIGNMENT,
            font=STYLE)
        


   

