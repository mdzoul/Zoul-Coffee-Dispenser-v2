class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "10c": 0.10,
        "20c": 0.20,
        "50c": 0.50,
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"\33[1mProfit\33[0m: \33[1;32m{self.CURRENCY}{self.profit:.2f}\33[0m")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.\n")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"{coin} coins: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"\nYour change is \33[32m{self.CURRENCY}{change:.2f}\33[0m.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("\n\33[31mInsufficient amount. Refunding coins...\33[0m")
            self.money_received = 0
            return False
