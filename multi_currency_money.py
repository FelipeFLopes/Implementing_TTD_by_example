class money():
    def __init__(self, amount):
        self.amount = amount

    def equals(self, currency):
        return self.amount == currency.amount

    def times(self, multiplier):
        return dollar(self.amount * multiplier)


class dollar(money):
    pass


class franc(money):
    pass
