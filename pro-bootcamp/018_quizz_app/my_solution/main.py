# std library
import requests
import logging

# third party modules

# custom modules
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


# Logging configuration
LOG_LEVEL = "INFO"
FORMAT = '%(levelname)s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__file__)
logger.setLevel(LOG_LEVEL.upper())


def start_game(question_bank: list = None) -> None:
    """
    Starts the game for the user

    Args:
        question_bank (list, optional): [Question bank to be used for the game]. Defaults to None.
    """

    if question_bank is None:
        question_bank = []
        for question in question_data:
            question_bank.append(
                Question(question['text'], question['answer']))

    quizbrain = QuizBrain(question_bank)

    while quizbrain.has_next_question():
        quizbrain.next_question()

    print("Quiz completed!")
    print(f"Your score is: {quizbrain.score}/{len(question_bank)}")


def fetch_questions(configuration: dict = None) -> list:
    """
    Fetches the opentriviadb for trivia questions (boolean)
    https://opentdb.com/api_config.php

    Returns:
        list: the question bank containing the questions for the game
    """

    if configuration is None:
        opentriviadb = requests.get(
            'https://opentdb.com/api.php?amount=10&type=boolean')

    else:
        url = construct_url(configuration)
        opentriviadb = requests.get(url)

    question_bank = []
    for question in opentriviadb.json()['results']:
        logger.debug(question)
        question_bank.append(
            Question(question['question'], question['correct_answer']))
    return question_bank


def construct_url(configuration) -> str:
    url = "https://opentdb.com/api.php?"

    # Add ammount of questions
    if configuration.get('number_of_questions'):
        url += f"amount={configuration['number_of_questions']}"
    else:
        url += f"amount=10"

    if configuration.get('difficulty'):
        url += f"&difficulty={configuration['difficulty']}"
    
    if configuration.get('category'):
        url += f"&category={configuration['category']}"
    logger.debug(url)
    return url


def configure() -> dict:
    """
    Configures the current game setup for fetching the trivia from
    https://opentdb.com/api_config.php. For using default value,
    leave blank (enter)

    Available questions include:
        * number_of_questions
        * category (32 available categories)
            * 1. Any 
            * 2. General knowledge
            * 3. Entertainment: books
            * 4. Entertainment: films
            * 5. Entertainment: music
            * 6. Entertainment: theater & musicals
            * 7. Science and Nature
            * 8. Science and computers
            * 9. Sports
            * 10. Mythology
            * 11. History
            * 12. Politics
            * 13. Art
            * 14. Vehicles
        * difficulty (easy/medium/hard)

    Returns:
        dict: A dictionary containing the configuration for the game
        example:
        {
            "number_of_questions" = "10",
            "difficulty" = "medium"
        }
    """
    configuration = {}
    available_categories = [
        "Any",  # 0
        "General knowledge",  # 1
        "Entertainment: books",  # 2
        "Entertainment: films",  # 3
        "Entertainment: music",  # 4
        "Entertainment: theater & musicals",  # 5
        "Science and nature",  #  6
        "Science and computers",  # 7
        "Sports",  #  8
        "Mythology",  # 9
        "History",  # 10
        "Politics",  # 11
        "Art",  # 12
        "Vehicles"  #  13
    ]
    category_mapping_in_api = {
        "1": "9", # General knowledge
        "2": "11" # 
    }

    number_of_questions = input("How many questions?: ")
    configuration['number_of_questions'] = number_of_questions
    difficulty = input("Difficulty (easy/medium/hard): ")
    print("Available categories:")
    for i in range(len(available_categories)):
        print(f"{i} - {available_categories[i]}")
    
    selected_category = input()

    if int(selected_category) < 0 or int(selected_category) > len(available_categories):
        logger.info("That category is not available.")
    
    category = category_mapping_in_api.get(selected_category)
    logger.debug(f"Selected category: {available_categories[int(selected_category)]}")
    configuration['category'] = category

    configuration['difficulty'] = difficulty
    
    logger.debug(configuration)
    return configuration


if __name__ == '__main__':
    configuration = configure()
    questions = fetch_questions(configuration)
    start_game(questions)
