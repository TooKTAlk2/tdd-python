class Dollor:
    def __init__(self, amount) -> None:
        self.amount = amount

    def times(self, multiplier):
        return Dollor(self.amount * multiplier)

    def __eq__(self, __o: object) -> bool:
        return self.amount == __o.amount
