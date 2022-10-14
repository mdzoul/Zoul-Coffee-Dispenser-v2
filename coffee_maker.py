class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk": 500,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def refill(self):
        """Refills the ingredients in the coffee dispenser"""
        resources_ingredient = input("\nWhat do you want to refill? ").lower()
        refill_amount = int(input(f"How much \33[32m{resources_ingredient}\33[0m do you want to refill? "))
        self.resources[resources_ingredient] += refill_amount

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Insufficient \33[31m{item}\33[0m. Please choose another drink.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your \33[34m{order.name}\33[0m ☕. Enjoy!")

    @staticmethod
    def make_another_coffee():
        another_coffee = input("\nWould you like to purchase another coffee? \33[32mY\33[0m/\33[31mN\33[0m\n")
        if another_coffee == "n":
            print("\n\33[31mTurning coffee machine off...\33[0m")
            exit()
        elif another_coffee == "y":
            return
