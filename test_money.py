from ast import Assert
from money import Dollor


def test_multiplication():
    five: Dollor = Dollor(5)
    assert five.times(2) == Dollor(10)
    assert five.times(3) == Dollor(15)


def test_equality():
    assert Dollor(5) == Dollor(5)
