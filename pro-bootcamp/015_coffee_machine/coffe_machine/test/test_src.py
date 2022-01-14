# std lib

# third party modules
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

