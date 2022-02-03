# std
from turtle import Turtle, Screen, clear
import logging
import random
# third party modules

# custom modules


# Game configuration
screen = Screen()
HEIGHT=400
WIDTH=500
screen.setup(width=WIDTH, height=HEIGHT)
SPEED = 10
SHAPE = "turtle"
STARTING_POSITIONS = [
    [-240, 0],
    [-240, 50],
    [-240, 100],
    [-240, -50],
    [-240, -100]
]
# Available collors for the user
COLORS = {'red', 'blue', 'green', 'yellow', 'orange'}


# Logging configuration
LOG_LEVEL = "INFO"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


def init_user(color: str) -> Turtle:
    """
    Initializes the user Turtle, picking
    up a color in the prompt, and always
    starting it in the center of the screen

    Args:
        color (str): A color from the rainbow
    
    Returns:
        Turtle: The main user turtle

    """
    if color not in COLORS:
        logger.info(f'The color {color} is not available')
        exit()
    tim = Turtle()
    tim.shape(name=SHAPE)
    tim.color(color)
    tim.penup()
    tim.goto(STARTING_POSITIONS[0])
    return tim


def init_challengers(user_color:str) -> list:
    """ Generates all the challengers in the race.
    Leaving the color that the user chose as the
    turtle in the center position

    Args:
        user_color (str): The color chosen by the user

    Returns:
        list: A list of turtles to race
    """
    logger.debug(f'User is: {user_color}')
    colors = COLORS
    colors.remove(user_color)
    colors_list = list(colors)
    logger.debug(f'Using {colors_list} as the colors for challengers.')
    challengers = []
    for i in range(len(colors_list)):
        challenger = Turtle()
        challenger.shape(name=SHAPE)
        challenger.color(colors_list[i])
        challenger.penup()
        challenger.goto(STARTING_POSITIONS[i + 1])
        challengers.append(challenger)
    return challengers


def is_winner(player:Turtle) -> bool:
    """ Returns true when player has won the game

    Args:
        player (Turtle): A turtle player from the board

    Returns:
        bool: True when the turtle crossed the finished line first
    """
    if player.pos()[0] > WIDTH/2:
        return True
    return False


def race(turtles) -> Turtle:
    """ Starts the race

    Args:
        turtles (list(Turtle)): A list of challengers for the race.

    Returns:
        Turtle: The winner of the race
    """
    is_race_on = True
    while is_race_on:
        for turtle in turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            logger.debug(f'{turtle.color()} at {turtle.position()}')
            if is_winner(turtle):
                is_race_on = False
                logger.info(f'{turtle.color()} won the race!')
                return turtle


def is_bet_won(user_bet:str, winner:Turtle) -> bool:
    """ Determines if the user won the bet

    Returns:
        bool: True when the bet matches the color of the winning turtle
    """
    return user_bet == winner.color()


if __name__ == '__main__':
    logger.info("Strating turtle race!")
    color_prompt = "Which turtle will win the race? Enter a color: "
    user_bet = screen.textinput(title="Make your bet", prompt=color_prompt)
    logger.info(f"You're betting on: {user_bet}!")
    tim = init_user(user_bet)
    challengers = init_challengers(user_bet)
    challengers.append(tim)
    logger.debug(challengers)
    winner = race(challengers)
    if is_bet_won(user_bet, winner):
        logger.info(f'You won the bet!!')
    else:
        logger.info(f'You lost the bet :(... try again.')
    logger.info('Click on the screen to finish the game.')
    screen.exitonclick()