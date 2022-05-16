from money import Dollor, Franc


def test_multiplication():
    five: Dollor = Dollor(5)
    assert five.times(2) == Dollor(10)
    assert five.times(3) == Dollor(15)


def test_equality():
    assert Dollor(5) == Dollor(5)
    assert Dollor(5) != Dollor(6)
    assert Franc(6) == Franc(6)
    assert Franc(6) != Franc(7)
    assert Franc(6) != Dollor(6)


def test_franc_multiplication():
    five: Franc = Franc(5)
    assert five.times(2) == Franc(10)
    assert five.times(3) == Franc(15)
