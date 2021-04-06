from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def reduce(self, bank, to):
        pass


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to):

        #rate = bank.rate(self.augend.currency(), self.addend.currency())

        augend = self.augend.reduce(bank, to)
        addend = self.addend.reduce(bank, to)

        return Money(augend.amount + addend.amount, to)

    def plus(self, addend):
        pass


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

    def reduce(self, bank, to):
        rate = bank.rate(self.currency(), to)

        return Money(self.amount / rate, to)

    @classmethod
    def dollar(self, amount):
        return Money(amount, "USD")

    @classmethod
    def franc(self, amount):
        return Money(amount, "CHF")


class Bank():
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):

        return source.reduce(self, to)

    def rate(self, from_, to):
        if from_ == to:
            return 1

        pair = (from_, to)

        return self.rates[pair]

    def add_rate(self, from_, to, rate):
        pair = (from_, to)
        self.rates[pair] = rate
