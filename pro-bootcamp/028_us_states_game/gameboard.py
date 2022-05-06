# standard library
from turtle import Screen, hideturtle
from turtle import Turtle

# third party
import pandas

# custom
from config import Config
import states_data_fetcher


class GameBoard():

    """
    Class that represents the US states game
    """

    def __init__(self):
        """
        Initializes the Gameboard
        """
        self.init_config()
        self.init_screen()
        self.init_turtle()
        answer_state = self.screen.textinput(title='Guess the state', prompt='What is another state game?')
        self.states_data = states_data_fetcher.load_csv_data()
        if states_data_fetcher.is_state(answer_state, self.states_data):
            coordinates = states_data_fetcher.get_coordinates(answer_state, self.states_data)
            self.update_answered_state(answer_state, coordinates)
        self.screen.mainloop()


    def init_turtle(self):
        """
        Initializes the python.Turtle on screen
        which holds the map
        """
        self.turtle_map = Turtle()
        self.turtle_map.shape(self.config.map_image)


    def update_answered_state(self, state:str, coordinates:pandas.DataFrame):
        """
        Updates the map with the correct answer

        Args:
            state(string): The name of a state
            coordinates(pandas.DataFrame): Pandas dataframe with x, y coordinates
        """
        t = Turtle(visible=False)
        t.penup()
        t.goto(int(coordinates['x']), int(coordinates['y']))
        t.write(state, move=True, align="center", font=self.config.style)
    
    def init_screen(self):
        """
        Initializes the python screen
        """
        self.screen = Screen()
        self.screen.title("U.S. States Game")
        self.screen.addshape(self.config.map_image)



    def init_config(self):
        """
        Initializes all configuration settings
        shared across the game
        """
        self.config = Config()


    def get_mouse_click_coor(self, x, y):
        """
        This function prints the click location
        on screen. To be called with 
        Python.Screen.onscreenclick()

        Args:
            x (int): Value received through Turtle
            y (int): Value received through Turtle
        """
        print(x, y)

    




