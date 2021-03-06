from abc import ABC
from audioop import add


class Expression(ABC):
    def reduce(self, bank, to: str = "USD"):
        pass

    def __add__(self, addend):
        pass

    def times(self, multiplier: int):
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

    def times(self, multiplier) -> Expression:
        return Money(self.amount * multiplier, self.currency)

    def __add__(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank, to: str = "USD"):
        rate = bank.rate(self.currency, to)
        return Money(self.amount / rate, to)


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to: str):
        amount = (
            self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        )
        return Money(amount, to)

    def __add__(self, addend: Expression):
        return Sum(self, addend)

    def times(self, multiplier):
        return Sum(self.augend.times(multiplier), self.addend.times(multiplier))


class Bank:
    rates = dict()

    def reduce(
        self,
        source: Expression = Money.dollor(5) or Sum(Money.dollor(1), Money.dollor(2)),
        to: str = "USD",
    ):
        return source.reduce(self, to)

    @classmethod
    def add_rate(cls, src: str, dest: str, rate: int):
        cls.rates[Pair(src, dest)] = rate

    @classmethod
    def rate(cls, src: str, dest: str):
        if src == dest:
            return 1
        return cls.rates[Pair(src, dest)]


class Pair:
    def __init__(self, src, dest) -> None:
        # private
        self.__from = src
        self.__to = dest

    def __eq__(self, __o: object) -> bool:
        return self.__from == __o.__from and self.__to == __o.__to

    def __hash__(self) -> int:
        return 0


if __name__ == "__main__":
    five_dollor = Money(5, "USD")
    five_franc = Money(5, "CHF")

    print(five_dollor.__class__.__name__)

    one_two = Pair("1", "2")
    two_one = Pair("2", "1")
    print(one_two == two_one)
