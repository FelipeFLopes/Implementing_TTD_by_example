class dollar():
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return dollar(self.amount * multiplier)
