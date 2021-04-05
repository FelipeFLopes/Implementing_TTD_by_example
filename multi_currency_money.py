from abc import ABC, abstractmethod


class money(ABC):
    def __init__(self, amount):
        self.amount = amount

    def equals(self, currency):

        if type(self) != type(currency):
            return False

        return self.amount == currency.amount

    @abstractmethod
    def times(self, multiplier):
        pass

    @classmethod
    def dollar(self, amount):
        return dollar(amount)

    @classmethod
    def franc(self, amount):
        return franc(amount)


class dollar(money):
    def times(self, multiplier):
        return dollar(self.amount * multiplier)


class franc(money):
    def times(self, multiplier):
        return franc(self.amount * multiplier)
