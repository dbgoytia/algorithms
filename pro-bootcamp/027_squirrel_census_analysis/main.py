# std library

# third party
import pandas

# custom modules

pandas.options.mode.chained_assignment = None

def squirrel_colour_count(squirrel_census_dataset:pandas.DataFrame) -> pandas.Series:
    """
    Returns how many squirrels exist per fur color
    on the squirrel census dataset on a pandas.DataFrame

    Args:
        squirrel_census_dataset (pandas.DataFrame): squirrel census in a pandas.DataFrame

    Returns:
        pandas.Series: A pandas.Series containing squirrel colour count in the park
    """
    scd_trimmed = squirrel_census_dataset[['X', 'Y', 'Primary Fur Color']]
    return scd_trimmed.groupby('Primary Fur Color').count()['X']


def squirrel_age_distribuition(squirrel_census_dataset:pandas.DataFrame) -> pandas.Series:
    """
    Returns a pandas.Series containing the age distribution of the seen
    squirrels

    Args:
        squirrel_census_dataset (pandas.DataFrame): squirrel census in a pandas.DataFrame

    Returns:
        pandas.Series: A pandas.Series containing squirrel age distribution
    """

    scd_trimmed = squirrel_census_dataset[['X', 'Y', 'Age']]
    scd_trimmed['Age'].replace('?', 'Unknown', inplace=True)
    scd_trimmed['Age'].fillna('Unknown', inplace=True)
    return scd_trimmed.groupby('Age').nunique()['X']


def get_squirrel_activity(squirrel_census_dataset:pandas.DataFrame) -> pandas.DataFrame:
    """
    Returns a pandas.Series containing all the activity of squirrels

    Args:
        squirrel_census_dataset (pandas.DataFrame): squirrel census in a pandas.DataFrame
    Returns:
        pandas.DataFrame: A pandas.DataFrame containing the activity of squirrels.
    """
    all_activity = (
        squirrel_census_dataset[['Running', 'Chasing', 'Climbing', 'Eating','Foraging']].sum().reset_index()
    )
    all_activity.columns = ['Activity','Count']
    return all_activity


def get_squirrel_shift_activity(squirrel_census_dataset:pandas.DataFrame) -> pandas.Series:
    """
    Returns a pandas.Series containing the activity of squirrels per shift

    Args:
        squirrel_census_dataset (pandas.DataFrame): squirrel census in a pandas.DataFrame

    Returns:
        pandas.Series: A pandas.Series containing the activity of squirrels per shift
    """
    activity_by_shift = squirrel_census_dataset.groupby('Shift')[
        ['Running', 'Chasing', 'Climbing', 'Eating','Foraging']
    ].sum()
    return activity_by_shift


def load_squirrel_census_dataset(csv_dataset_filepath:str = './data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv') -> pandas.DataFrame:
    """
    Loads the census dataset into a pandas.DataFrame

    Returns:
        pandas.DataFrame: Dataset for the squirrel census
    """
    return pandas.read_csv(csv_dataset_filepath)


if __name__ == '__main__':
    # load dataset
    squirrel_census_dataset = load_squirrel_census_dataset()
    print(squirrel_census_dataset)
    print()
    # colour distribution
    clour_count_dataframe = squirrel_colour_count(squirrel_census_dataset)
    print(f'Number of squirrels per colour: \n {clour_count_dataframe}')
    print()
    # age distribution
    age_distribution = squirrel_age_distribuition(squirrel_census_dataset)
    print(f'Age distribution of squirrels: \n {age_distribution}')
    print()
    # activity of squirrels
    activity = get_squirrel_activity(squirrel_census_dataset)
    print(f'Activity of squirrels is: \n {activity}')
    print()
    # shift activity
    shift_activity = get_squirrel_shift_activity(squirrel_census_dataset)
    print(f'Activity of squirrel per shift is: \n {shift_activity}')
    print()

