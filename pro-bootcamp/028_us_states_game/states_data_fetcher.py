# std lib

# third party

import pandas

# custom modules


def is_state(guess:str, states:pandas.DataFrame) -> bool:
    """
    Returns true if the guess is a state

    Args:
        guess (str): a string, which could be a US state
        states (DataFrame): contains data for US. states.

    Returns:
        bool: True if it is a state, False otherwise.
    """
    return True if guess in states['state'].unique() else False
        
   
def get_coordinates(guess:str, states:pandas.DataFrame) -> pandas.DataFrame:
    """
    Returns the coordinates of a state inside the map.

    Args:
        guess (str): a string, which is a US state.
        states (DataFrame): contains data for US. states.

    Returns:
        pandas.DataFrame: (state, x, y) pandas.DataFrame containing metadata of state.
    """
    if not is_state(guess, states):
        return []
    metadata = states[states.state == guess]
    return(metadata)
    


def load_csv_data(filepath:str="./data/us_states.csv") -> pandas.DataFrame:
    """
    Loads CSV data into a pandas.DataFrame.

    Args:
        filepath (str, optional): Path to state data. Defaults to "./data/50_states.csv".

    Returns:
        DataFrame: Contains coordinates of each state on a given map.
    """
    return pandas.read_csv(filepath)
