class Money:
    def __init__(self, amount) -> None:
        self._amount = amount

    def __eq__(self, __o: object) -> bool:
        money = Money(__o)
        return self._amount == money._amount


class Dollor(Money):
    def times(self, multiplier):
        return Dollor(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
