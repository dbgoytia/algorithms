# std lib
from unittest.mock import Mock, patch

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


def test__purchase_drink_fail():
    assert ui.purchase_drink("latte", 0.01) == False


def test__purchase_drink_success():
    assert ui.purchase_drink("latte", 80) == True


def test__total_coins():
    input_mock_quarters = Mock()
    input_mock_quarters.return_value = 1
    input_mock_dimes = Mock()
    input_mock_dimes.return_value = 3
    input_mock_nickles = Mock()
    input_mock_nickles.return_value = 2
    input_mock_pennies = Mock()
    input_mock_pennies.return_value = 30

    input_mock = Mock()

    input_mock.side_effect = [
        input_mock_quarters.return_value,
        input_mock_dimes.return_value,
        input_mock_nickles.return_value,
        input_mock_pennies.return_value,
    ]

    with patch('builtins.input', input_mock) as mock_input:
        assert ui.total_coins() == 0.95



