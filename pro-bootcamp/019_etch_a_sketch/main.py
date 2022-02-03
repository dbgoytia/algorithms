# std
from turtle import Turtle, Screen, clear
import logging

# third party modules

# custom modules


# Configuration
tim = Turtle()
screen = Screen()
SPEED = 10

# Logging configuration
LOG_LEVEL = "DEBUG"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


def move_forward():
    logger.debug(f"Moving Tim forward with speed: {SPEED}")   
    tim.forward(SPEED)


def move_backwards():
    logger.debug(f"Moving Tim backwards with speed: {SPEED}")
    tim.backward(SPEED)


def rotate_clockwise():
    logger.debug(f"Rotating Tim clockwise with speed: {SPEED}")
    tim.right(SPEED)
    logger.debug(f"Tim is heading: {tim.heading()}")


def rotate_counter_clockwise():
    logger.debug(f"Rotating Tim clockwise with speed: {SPEED}")
    tim.left(SPEED)
    logger.debug(f"Tim is heading: {tim.heading()}")


def clear_screen():
    logger.debug(f"Cleaning up screen.")
    tim.clear()
    tim.penup()
    tim.home()



logger.info("Strating etch-a-sketch!")
logger.debug(tim.heading())
logger.debug(f"speed: {SPEED}")
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()