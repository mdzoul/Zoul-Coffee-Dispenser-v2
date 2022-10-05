class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=35, milk=250, coffee=18, cost=2.5),
            MenuItem(name="espresso", water=35, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=35, milk=150, coffee=18, cost=3),
            MenuItem(name="flat white", water=35, milk=100, coffee=18, cost=2.5),
            MenuItem(name="macchiato", water=35, milk=50, coffee=18, cost=2.5),
            MenuItem(name="cafe au lait", water=115, milk=115, coffee=58, cost=3),
            MenuItem(name="cortado", water=40, milk=40, coffee=20, cost=2),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
