# stlib
import csv

# third party
import pandas

# custom modules


def load_data_plain_open()-> list:
    """ Loads a CSV and returns it's data
    inside a list.

    If you can see this requires data requires a lot
    of cleaning because each row of the csv is still 
    comma sepparated, and still contains newlines, and
    maybe will contain all sorts of funny things.

    Returns:
        list: A list containing the data of the csv file
    """
    with open(file='./weather_data.csv', mode="r") as f:
        data = f.readlines()
    return data
    

def load_data_with_csv() -> list:
    """ Loads CSV and returns it's data inside a list.
    
    Returns:
        list: A list containing the data of the csv file
    """
    with open(file="./weather_data.csv", mode="r") as f:
        data_reader = csv.reader(f)
        data = []
        for row in data_reader:
            data.append(row)
    return data


def get_temperatures_list() -> list:
    """ Returns a list of temperatures when reading 
    weather data.

    CSV is the in-built library, still not great. If we
    had more data, it's going to be very painful to work with

    Returns:
        list: A list containing the temperatures in the weather data
    """
    with open(file="./weather_data.csv", mode="r") as f:
        data_reader = csv.reader(f)
        temperatures = []
        for row in data_reader:
            if row[1] != "temp":
                temperatures.append(int(row[1]))
        return temperatures


def load_data_with_pandas() -> list:
    """ Loads CSV data using pandas

    Returns:
        list: A list containing the weather data
    """
    data = pandas.read_csv("./weather_data.csv")
    return data



if __name__ == '__main__':
    print("____Plain open____")
    data = load_data_plain_open()
    print(type(data))
    print(data)
    print()


    print("____CSV____")
    data = load_data_with_csv()
    print(type(data))
    print(data)
    temperatures_list = get_temperatures_list()
    print(temperatures_list)
    print()

    print("____Pandas____")
    data = load_data_with_pandas()
    print(type(data))
    print(data)
    print(type(data['temp']))
    print(data['temp'])
    print("Data frame to dict")
    data_dict = data.to_dict()
    print(type(data_dict))
    print(data_dict)
    print("Series to list")
    data_temp_list = data['temp'].to_list()
    print(type(data_temp_list))
    print(data_temp_list)
