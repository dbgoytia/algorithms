# standard library
from turtle import Turtle
import random

# third party

# custom modules


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    """
    The class responsible for building the cars that
    may collide with the turtle.
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.all_cars = []
        self.move_increment = MOVE_INCREMENT

    
    def create_car(self) -> None:
        """
        Creates a new car on the total cars on the screen
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            random_y = random.randint(-250, 250)
            new_car.goto(280, random_y)
            self.all_cars.append(new_car)

    
    def move(self) -> None:
        """
        Move each of the cars on screen for the turtle
        to avoid
        """
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + self.move_increment)
        



        
