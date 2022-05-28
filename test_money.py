from money import Money, Bank, Expression, Sum


def test_multiplication():
    five: Money = Money.dollor(5)
    assert five.times(2) == Money.dollor(10)
    assert five.times(3) == Money.dollor(15)


def test_equality():
    assert Money.dollor(5) == Money.dollor(5)
    assert Money.dollor(5) != Money.dollor(6)
    assert Money.franc(6) != Money.dollor(6)


def test_franc_multiplication():
    five: Money = Money.franc(5)
    assert five.times(2) == Money.franc(10)
    assert five.times(3) == Money.franc(15)


def test_currency():
    assert "USD" == Money.dollor(10).currency
    assert "CHF" == Money.franc(10).currency


def test_simple_addition():
    bank = Bank()
    sum: Sum = Money.dollor(5) + Money.dollor(5)
    reduced = bank.reduce(sum, "USD")
    assert Money.dollor(10) == reduced


def test_plus_returns_sum():
    five: Money = Money.dollor(5)
    sum: Sum = five + five
    assert five == sum.augend
    assert five == sum.addend


def test_reduce_sum():
    sum: Expression = Sum(Money.dollor(3), Money.dollor(2))
    bank = Bank()
    result: Money = bank.reduce(sum, "USD")
    assert result == Money.dollor(5)


def test_reduce_money():
    five: Money = Money.dollor(5)
    bank = Bank()
    result: Money = bank.reduce(five, "USD")

    assert Money.dollor(5) == result


def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result: Money = bank.reduce(Money.franc(2), "USD")
    assert result == Money.dollor(1)


def test_identity_rate():
    assert 1 == Bank().rate("USD", "USD")
