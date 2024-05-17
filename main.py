from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

if __name__ == "__main__":
    while is_on:
        user_input = input(f"Choose coffee ({menu.get_items()}): ")
        if user_input == "espresso" or user_input == "cappuccino" or user_input == "latte":
            drink = menu.find_drink(user_input)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        elif user_input == "report":
            coffee_maker.report()
        elif user_input == "off":
            is_on = False
        else:
            print("Wrong input!")