from abc import ABC, abstractmethod
from ast import Expr
from re import M


class Expression(ABC):
    def reduce(self, bank, to: str = "USD"):
        pass


class Money(Expression):
    def __init__(self, amount, currency) -> None:
        self._amount = amount
        self._currency: str = currency

    @staticmethod
    def dollor(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    def __eq__(self, __o: object):
        return self.amount == __o.amount and self.currency == __o.currency

    def __str__(self) -> str:
        return f"{self.amount} {self.currency}"

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def __add__(self, __o: object) -> Expression:
        return Sum(self, __o)

    def reduce(self, bank, to: str = "USD"):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str):

        amount = self.augend.amount + self.addend.amount
        rate = bank.rate(self.augend.currency, to)
        return Money(amount / rate, to)


class Bank:
    def reduce(
        self,
        source: Expression = Money.dollor(5) or Sum(Money.dollor(1), Money.dollor(2)),
        to: str = "USD",
    ):
        return source.reduce(self, to)

    def add_rate(self, src, dest, rate):

        pass

    def rate(self, src: str, dest: str):
        if src == "CHF" and dest == "USD":
            return 2
        return 1


if __name__ == "__main__":
    five_dollor = Money(5, "USD")
    five_franc = Money(5, "CHF")

    print(five_dollor.__class__.__name__)
