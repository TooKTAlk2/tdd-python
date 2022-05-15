from money import Money


def test_multiplication():
    five = Money(5)
    five.times(2)
    assert five.amount == 10
