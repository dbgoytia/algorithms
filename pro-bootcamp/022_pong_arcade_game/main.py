# std library
from turtle import Screen
from turtle import exitonclick
import logging

# third party modules

# custom modules
from paddle import Paddle


# Global Setup
WIDTH = 800
HEIGHT = 600

# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())

class GameBoard:


    def __init__(self):
        """
        Initializes the gameboard
        """
        self.initialize_screen()


    def initialize_screen(self):
        """
        Creates the screen for the pong game
        """
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.listen()
        self.screen.title('Pong')
        self.screen.bgcolor('black')
        self.screen.setup(width=WIDTH, height=HEIGHT)

        self.init_players()
        self.init_controllers()

        self.game_is_on = True
        
        while self.game_is_on:
            self.screen.update()


    def init_players(self):
        """
        Initializes the players on the screen
        """
        self.playerone = Paddle(x=350, y=0)
        self.playertwo = Paddle(x=-350, y=0)


    def init_controllers(self):
        """
        Creates the controllers for the main player

        Controlls:
            * Up Arrow
            * Down Arrow
        """
        # Player one
        self.screen.onkey(fun=self.playerone.move_up, key='Up')
        self.screen.onkey(fun=self.playerone.move_down, key='Down')

        # Player two
        self.screen.onkey(fun=self.playertwo.move_up, key='w')
        self.screen.onkey(fun=self.playertwo.move_down, key='s')


if __name__ == '__main__':
    gameboard = GameBoard() 

