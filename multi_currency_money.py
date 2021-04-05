from abc import ABC, abstractmethod


class money(ABC):
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def equals(self, currency):

        if type(self) != type(currency):
            return False

        return self.amount == currency.amount

    def currency(self):
        return self._currency

    @abstractmethod
    def times(self, multiplier):
        pass

    @classmethod
    def dollar(self, amount):
        return dollar(amount, "USD")

    @classmethod
    def franc(self, amount):
        return franc(amount, "CHF")


class dollar(money):

    def times(self, multiplier):
        return money.dollar(self.amount * multiplier)


class franc(money):

    def times(self, multiplier):
        return money.franc(self.amount * multiplier)
