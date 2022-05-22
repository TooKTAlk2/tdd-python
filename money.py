class Money:
    def __init__(self, amount) -> None:
        self._amount = amount

    def __eq__(self, __o: object) -> bool:
        return (
            self._amount == __o._amount
            and self.__class__.__name__ == __o.__class__.__name__
        )

    @staticmethod
    def dollor(amount):
        return Dollor(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)


class Dollor(Money):
    def times(self, multiplier):
        return Dollor(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)


if __name__ == "__main__":
    five_dollor = Money.dollor(5)
    five_franc = Money.franc(5)

    print(five_dollor.__class__.__name__)
