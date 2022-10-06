from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from prettytable import PrettyTable


def menu_table():
    table = PrettyTable()
    table.add_column("Coffee", menu.get_items())
    table.add_column("Price", menu.get_price())
    table.align["Coffee"] = 'l'
    print(table)


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

logo()
print("\n\33[32mTurning coffee machine on...\33[0m\n")
menu_table()

coffeeChosen = False
options = menu.get_items()
while not coffeeChosen:
    choice = input(f"\nWhat would you like? ").lower()

    if choice == "off":
        off = True
        print("\n\33[31mTurning coffee machine off...\33[0m")
        exit()

    elif choice == "menu":
        menu_table()

    elif choice == "report":
        coffee_maker.report()
        print("---")
        money_machine.report()

    elif choice == "refill":
        coffee_maker.refill()

    else:
        coffee = menu.find_drink(choice)
        print(f"\33[34m{choice.capitalize()}\33[0m: \33[32m${coffee.cost:.2f}\33[0m")
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
            coffee_maker.make_another_coffee()
