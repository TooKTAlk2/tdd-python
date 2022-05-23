from locale import currency


class Money:
    def __init__(self, amount, currency) -> None:
        self._amount = amount
        self._currency: str = currency

    def __eq__(self, __o: object) -> bool:
        return self._amount == __o._amount and self.currency == __o.currency

    @staticmethod
    def dollor(amount):
        return Dollor(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    @property
    def currency(self):
        return self._currency

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"

    def times(self, multiplier):
        return Money(self._amount * multiplier, self.currency)


class Dollor(Money):
    def __init__(self, amount, currency) -> None:
        super().__init__(amount, currency)


class Franc(Money):
    def __init__(self, amount, currency) -> None:
        super().__init__(amount, currency)


if __name__ == "__main__":
    five_dollor = Money.dollor(5)
    five_franc = Money.franc(5)

    print(five_dollor.__class__.__name__)
