from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
cm = CoffeeMaker()
mm = MoneyMachine()
m = Menu()

if __name__ == "__main__":
    while is_on:
        user_input = input(f"Choose coffee ({m.get_items()}): ")
        if user_input == "espresso" or user_input == "cappuccino" or user_input == "latte":
            drink = m.find_drink(user_input)
            if cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)
        elif user_input == "report":
            cm.report()
        else:
            print("Wrong input!")