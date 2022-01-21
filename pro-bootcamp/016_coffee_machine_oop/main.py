from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


available_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def ui():

    order = input(f"What would you like? ({available_menu.get_items()}): ")

    if order == 'off':
        exit()

    if order == 'report':
        coffee_maker.report()
        money_machine.report()
        ui()

    else:     
        if not available_menu.find_drink(order):
            ui()

        if not coffee_maker.is_resource_sufficient(available_menu.find_drink(order)):
            ui()
        
        if not money_machine.make_payment(available_menu.find_drink(order).cost):
            ui()

        coffee_maker.make_coffee(available_menu.find_drink(order))
        ui()


ui()