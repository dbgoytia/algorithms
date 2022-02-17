# std library
from turtle import RawTurtle
import logging

# third party modules

# custom modules

# configuration
WIDTH = 600
HEIGHT = 600
OFFSET = 30
LOG_LEVEL="INFO"
ALIGNMENT="center"
STYLE=('Courier', 15, 'italic')

# Logging configuration
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())

class Scoreboard(RawTurtle):

    '''
    Renders as a scoreboard on the canvas
    '''


    def __init__(self, canvas):
        super().__init__(canvas)
        self.score = 0
        self.write_score()


    def write_score(self):
        logger.info(f'Score: {self.score}')
        self.penup()
        self.hideturtle()
        self.goto(0, HEIGHT/2-OFFSET)
        style = STYLE
        self.color('white')
        self.write(f'Score: {self.score}', move=True, align="center", font=style)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()


    def game_over(self):
        self.color('white')
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=STYLE)