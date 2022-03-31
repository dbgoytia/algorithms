# standard library
import time
import logging
from tkinter import E
from turtle import Screen

# third party

# custom
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


class GameBoard:

    def __init__(self) -> None:
        """
        Initializes the gameboard.
        """
        self.initialize_screen()
        self.game_is_on = True
        self.game_loop()
    
    
    def game_loop(self) -> None:
        """
        Will loop until game_is_on is turned off.
        That should happen every time the turtle gets
        hit by a car.
        """
        while self.game_is_on:
            time.sleep(0.1)
            self.cars.move()
            self.screen.update()
            self.cars.create_car()
            for car in self.cars.all_cars:
                if self.playerone.is_squished(car.xcor(), car.ycor()):
                    self.scoreboard.game_over()
                    self.screen.onkey(fun=None, key='Up')
                    logger.debug("You lost!")
                if self.playerone.crossed_finish_line():
                    logger.debug(f"Won level: {self.scoreboard.level}")
                    self.cars.move_increment += 3
                    self.scoreboard.increase_score()
                    self.scoreboard.write_score()
                    self.playerone.return_to_start()

    
    def initialize_screen(self) -> None: 
        """
        Initializes the main gameboard screen
        """
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        self.screen.listen()
        self.initialize_player()
        self.initialize_controllers()
        self.initialize_cars()
        self.initialize_scoreboard()
        self.cars.create_car()


    def initialize_player(self) -> None:
        """
        Initializes the main player on screen.
        """
        self.playerone = Player()

    
    def initialize_controllers(self) -> None:
        """
        Main controllers for the player.
        The player can only move up

        Controllers:
            * Up Arrow
        """
        self.screen.onkey(fun=self.playerone.move, key='Up')

    
    def initialize_cars(self) -> None:
        """
        Initializes the cars on screen
        """
        self.cars = CarManager()

    
    def initialize_scoreboard(self) -> None:
        """
        Initializes scoreboard on screen
        """
        self.scoreboard = Scoreboard()
    

if __name__ == '__main__':
    gameboard = GameBoard()