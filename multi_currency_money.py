class dollar():
    def __init__(self, amount):
        self.amount = amount

    def equals(self, currency):
        return self.amount == currency.amount

    def times(self, multiplier):
        self.amount *= multiplier
