# std lib

# third party modules

# custom modules
from src import ui


# custom modules
def test__formatted_menu():

    menu_mocks = [
        {
            "espresso": { },
            "latte": { },
            "cappuccino": { }
        },
        {
            "espresso": {},
            "latte": {},
        },
        {
            ""
        },
        {
            "1"
        }
    ]

    expected_results = [
        "espresso/latte/cappuccino",
        "espresso/latte",
        "",
        "1"
    ]
    for i in range(len(expected_results)):
        assert ui.formatted_menu(menu_mocks[i]) == expected_results[i]


def test__brew_coffee():
    menu_mock = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            }
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
        }
    }
    resources_mock = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0,
    }
    expected_result = {
        "coffee": 76,
        "milk": 50,
        "water": 100,
        "money": 0
    }
    assert ui.brew_coffee("latte", resources_mock, menu_mock ) == expected_result



