from ast import Assert
from money import Dollor


def test_multiplication():
    five: Dollor = Dollor(5)
    product: Dollor = five.times(2)
    assert product.amount == 10
    product: Dollor = five.times(3)
    assert product.amount == 15


def test_equality():
    assert Dollor(5) == Dollor(5)
