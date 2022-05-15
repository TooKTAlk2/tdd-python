class Money:
    def __init__(self, amount) -> None:
        self._amount = amount

    def __eq__(self, __o: object) -> bool:
        return self._amount == __o._amount


class Dollor(Money):
    def times(self, multiplier):
        return Dollor(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)
