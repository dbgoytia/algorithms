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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def formatted_menu(menu: dict = None) -> str:
    """
    Returns the available drinks in the menu for the coffee machine

    Args:
        dict: (Optional), if not provided will use environment provided MENU.

    Returns:
        (str) a string containing the drinks in the menu in the form of:
        a/b/c
    """
    if menu is None:
        drinks = ('/'.join(str(x) for x in MENU))
    else:
        drinks = ('/'.join(str(x) for x in menu))
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
        user_prompt()

    if user_input not in MENU:
        print("we can't do that")
        user_prompt()

    if not check_resources_sufficient(user_input):
        user_prompt()

    purchase_drink(user_input)

    user_prompt()


def brew_coffee(drink: str, resources: dict = None, menu: dict = None) -> dict:
    """
    Reduces the resources required from brewing a drink

    Args:
        menu:
        resources:
        drink: A drink from the MENU

    Returns:
        (dict) A dictionary containing the remaining resources for  the coffee machine
    """

    if resources is None:
        resources = RESOURCES

    if menu is None:
        menu = MENU

    for ingredient in menu.get(drink).get('ingredients'):
        resources[ingredient] = resources[ingredient] - menu.get(drink).get('ingredients').get(ingredient)

    return resources


def purchase_drink(drink: str):
    """
    Asks the user to insert coins into the machine. Checks if there's enough money
    and if there is so, returns the required change. Otherwise, refunds money.

    Args:
        drink: A drink from the MENU
    """
    inserted_coins = input("Enter your coins:")
    total = total_coins(inserted_coins)
    if total < MENU.get(drink).get('cost'):
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = calculate_change(drink, total)
        print(f"Here's ${round(change, 2)} dollars in change.")
        total = total - change
        cash_money(total)
        brew_coffee(drink)


def calculate_change(drink: str, coins: str) -> float:
    """
    Calculates the money change for the client.

    Args:
        drink: A drink from the menu
        coins: Total money for the operation

    Returns:
        (float): Total change for the client

    """
    return coins - MENU.get(drink).get('cost')


def cash_money(coins: str):
    RESOURCES["money"] += coins
    return


def total_coins(coins: str) -> float:
    """
    Calculates the total based on the input from the user

    :return:
    (float) total value for the coins inserted in the machine
    """
    coin_values = {
        "pennies": 0.01,
        "nickel": 0.05,
        "dimes": 0.10,
        "quarter": 0.15
    }
    coins = coins.split(', ')
    total = 0
    for val in coins:
        total_per_coin = val.split(' ')
        subtotal = float(total_per_coin[0]) * coin_values.get(total_per_coin[1])
        total += subtotal
    return round(total, 2)


def check_resources_sufficient(drink: str) -> bool:
    """
    Checks if resources are sufficient to make a drink

    :input:
    (str) A drink from the menu

    :return:
    (bool) Wether it's possible to brew the drink
    """
    ingredients = MENU.get(drink).get('ingredients')
    for ingredient in ingredients:
        if ingredients.get(ingredient) > RESOURCES.get(ingredient):
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def get_report():
    """
    Prints a formatted report of the current machine status
    """
    print(f"Water: {RESOURCES.get('water')}ml")
    print(f"Milk: {RESOURCES.get('milk')}ml")
    print(f"Coffee: {RESOURCES.get('coffee')}g")
    print(f"Money: ${RESOURCES.get('money')}")
    return


def turn_off():
    """
    Turns of the coffee machine by entering off in the prompt.
    Code ends execution when this happens
    """
    exit()
