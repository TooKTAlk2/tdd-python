from locale import currency


class Money:
    def __init__(self, amount, currency) -> None:
        self._amount = amount
        self._currency: str = currency

    def __eq__(self, __o: object) -> bool:
        return (
            self._amount == __o._amount
            and self.__class__.__name__ == __o.__class__.__name__
        )

    @staticmethod
    def dollor(amount):
        return Dollor(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def currency(self):
        return self._currency


class Dollor(Money):
    def __init__(self, amount, currency) -> None:
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollor(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency) -> None:
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)


if __name__ == "__main__":
    five_dollor = Money.dollor(5)
    five_franc = Money.franc(5)

    print(five_dollor.__class__.__name__)
