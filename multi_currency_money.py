class money():
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def equals(self, currency):

        if self.currency() != currency.currency():
            return False

        return self.amount == currency.amount

    def currency(self):
        return self._currency

    def times(self, multiplier):
        return money(self.amount * multiplier, self.currency())

    @classmethod
    def dollar(self, amount):
        return money(amount, "USD")

    @classmethod
    def franc(self, amount):
        return money(amount, "CHF")
