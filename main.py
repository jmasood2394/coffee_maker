from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
resources = CoffeeMaker()
menu = Menu()


is_on = True
while is_on:
    users_choice = input(f"What would you like? {menu.get_items()}: ")
    if users_choice == "off".lower():
        is_on = False
        print("Maintenance Mode")
        break
    elif users_choice == "report".lower():
        money_machine.report()
        resources.report()
    else:
        drink = menu.find_drink(users_choice)
        if resources.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            resources.make_coffee(drink)
