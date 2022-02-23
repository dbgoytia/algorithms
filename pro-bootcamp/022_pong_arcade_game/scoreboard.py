# standard library
from turtle import Turtle
import logging

# third party modules

# custom modules


# configuration
WIDTH = 800
HEIGHT = 600
OFFSET = 30
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
    

    def __init__(self) -> None:
        """
        Initializes scoreboard on screen
        """
        super().__init__()
        self.playerone_score = 0
        self.playertwo_score = 0
        self.write_score()


    def write_score(self):
        logger.info(f'Scoreboard: {self.playerone_score} | {self.playertwo_score}')
        self.penup()
        self.hideturtle()
        self.goto(0, HEIGHT/2-OFFSET)
        self.color('white')
        self.write(
            f'Scoreboard: {self.playerone_score} | {self.playertwo_score}',
            move=True,
            align="center",
            font=STYLE,
        )
    

    def playerone_point(self):
        """
        Increases score of player one by one
        """
        self.playerone_score += 1
        self.clear()
        self.write_score()


    def playertwo_point(self):
        """
        Increases the score of player two by two
        """
        self.playertwo_score += 1
        self.clear()
        self.write_score()

