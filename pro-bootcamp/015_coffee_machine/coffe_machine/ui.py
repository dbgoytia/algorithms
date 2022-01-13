MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def formatted_menu() -> str:
    """
    Returns the available drinks in the menu for the coffee machine

    :return:
    (str) a string containing the drinks in the menu in the form of:
    a/b/c
    """
    drinks = ('/'.join(str(x) for x in MENU))
    return drinks


def user_prompt() -> str:
    """
    Prompts the user by asking "What would you like", and displaying
    the current menu on the terminal

    :return:
    (str) returns a string containing the user's answer.
    """
    # order = input("What would you like (espresso / latte / cappuccino):")
    menu = formatted_menu()
    user_input = input(f"What would you like ({menu}):")

    if user_input == "off":
        turn_off()

    if user_input == "report":
        get_report()

    if user_input not in MENU:
        print("we can't do that")
        exit()

    if not check_resources_sufficient(user_input):
        exit()

    insert_coins()


def insert_coins():
    {
        "pennies": 0.01,
        "nickel": 0.05,
        "dimes" : 0.10,
        "quarter": 0.15
    }
    coins = input("Enter your coins:")
    coins = coins.split(',')
    for val in coins:
        total = (val.split(' '))
        print(total)




def check_resources_sufficient(drink: str) -> bool:
    """
    Checks if resources are sufficient to make a drink

    :input:
    (str) A drink from the menu

    :return:
    (bool) Wether it's possible to brew the drink
    """
    ingredients = MENU.get(drink).get('ingredients')
    print(ingredients)

    for ingredient in ingredients:
        if ingredients.get(ingredient) > resources.get(ingredient):
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def get_report():
    """
    Prints a formatted report of the current machine status
    """
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")
    print(f"Money: ${resources.get('money')}")


def turn_off():
    """
    Turns of the coffee machine by entering off in the prompt.
    Code ends execution when this happens
    """
    exit()



