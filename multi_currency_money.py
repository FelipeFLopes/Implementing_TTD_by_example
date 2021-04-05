class money():
    def __init__(self, amount):
        self.amount = amount

    def equals(self, currency):

        if type(self) != type(currency):
            return False

        return self.amount == currency.amount


class dollar(money):
    def times(self, multiplier):
        return dollar(self.amount * multiplier)


class franc(money):
    def times(self, multiplier):
        return franc(self.amount * multiplier)


if __name__ == "__main__":
    franc_value = franc(5)

    test = franc_value.times()
