from money import Franc
from money import Money


def test_multiplication():
    five: Money = Money.dollor(5)
    assert five.times(2) == Money.dollor(10)
    assert five.times(3) == Money.dollor(15)


def test_equality():
    assert Money.dollor(5) == Money.dollor(5)
    assert Money.dollor(5) != Money.dollor(6)
    assert Money.franc(6) == Money.franc(6)
    assert Money.franc(6) != Money.franc(7)
    assert Money.franc(6) != Money.dollor(6)


def test_franc_multiplication():
    five: Money = Money.franc(5)
    assert five.times(2) == Money.franc(10)
    assert five.times(3) == Money.franc(15)


def test_currency():
    assert "USD" == Money.dollor(10).currency
    assert "CHF" == Money.franc(10).currency
    pass


def test_different_class_equality():
    assert Money(10, "CHF") == Franc(10, "CHF")
