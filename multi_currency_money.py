from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(self, to):
        pass


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        return Money(self.augend.amount + self.augend.amount, to)


class Money():
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
        return Money(self.amount * multiplier, self.currency())

    def plus(self, adder):
        return Sum(self, adder)

    def reduce(self, to):
        return self

    @classmethod
    def dollar(self, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(self, amount):
        return Money(amount, "CHF")


class Bank():
    def __init__(self):
        pass

    def reduce(self, source, to):
        return source.reduce(to)
