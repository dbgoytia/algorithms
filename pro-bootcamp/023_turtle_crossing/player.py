# standard library
from turtle import Turtle
import logging

# third party

# custom 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


class Player(Turtle):

    """
    A Class that represents the main player of the
    Turtle Crossing game
    """
    
    def __init__(self) -> None:
        """
        Constructor method
        """
        super().__init__()
        self.setheading(90)
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])

    
    def move(self) -> None:
        """
        Moves the player up by MOVE_DISTANCE value
        """
        logger.debug("Pressing up key!")
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    
    def is_squished(self, car_xcor, car_ycor) -> bool:
        """
        Returns true when the main player is squished

        Returns:
            bool: True when you've lost the game (squish!)
        """
        return abs(self.xcor() - car_xcor) < 30 and abs(self.ycor() - car_ycor) < 20

    
    def crossed_finish_line(self) -> bool:
        """
        Returns true when the player crossed the finish line

        Returns:
            bool: True when player crossed finish line (win)
        """
        return self.ycor() > FINISH_LINE_Y

    
    def return_to_start(self) -> None:
        """
        Returns player to the starting position for new level
        """
        self.goto(STARTING_POSITION[0], STARTING_POSITION[1])



        
        
