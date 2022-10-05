from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo


def restart():
    global off
    another_coffee = input("\nWould you like to purchase another coffee? \33[32mY\33[0m/\33[31mN\33[0m\n")
    if another_coffee == "n":
        print("\n\33[31mTurning coffee machine off...\33[0m")
        off = True
    elif another_coffee == "y":
        return


menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

logo()
print("\n\33[32mTurning coffee machine on...\33[0m\n")
# TODO: Make a class for a table of the menu items and their prices
# menu()
off = False
while not off:
    coffeeChosen = False
    options = menu.get_items()
    while not coffeeChosen:
        choice = input(f"\nWhat would you like? ({options}): ").lower()

        if choice == "off":
            break

        elif choice == "menu":
            menu()

        elif choice == "report":
            coffee_maker.report()
            print("---")
            money_machine.report()

        # TODO: Make a class for refill
        # elif choice == "refill":
        #     resourcesIngredient = input("\nWhat do you want to refill? ").lower()
        #     refillAmount = int(
        #         input(f"How much \33[32m{resourcesIngredient}\33[0m do you want to refill? "))
        #     resources[resourcesIngredient] += refillAmount

        else:
            coffee = menu.find_drink(choice)
            print(f"\33[34m{choice.capitalize()}\33[0m: \33[32m${coffee.cost:.2f}\33[0m")
            if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
                coffee_maker.make_coffee(coffee)
                restart()

    if choice == "off":
        off = True
        print("\n\33[31mTurning coffee machine off...\33[0m")
    else:
        restart()
