from multi_currency_money import Money, Bank, Sum


def test_currency():
    assert Money.dollar(5).currency() == "USD"
    assert Money.franc(5).currency() == "CHF"


def test_equal_same_currency():
    assert Money.dollar(5).equals(Money.dollar(5))
    assert Money.dollar(12).equals(Money.dollar(12))
    assert not Money.dollar(5).equals(Money.dollar(6))


def test_equal_different_currency():
    assert not Money.dollar(5).equals(Money.franc(5))
    assert not Money.dollar(12).equals(Money.franc(12))
    assert not Money.dollar(5).equals(Money.franc(6))

    assert not Money.franc(5).equals(Money.dollar(6))


def test_dolar_mult_by_constant():
    curret_value = Money.dollar(5)

    assert Money.dollar(10).equals(curret_value.times(2))
    assert Money.dollar(20).equals(curret_value.times(4))
    assert Money.dollar(35).equals(curret_value.times(7))


def test_sum_same_currency():
    current_value = Money.dollar(5)

    bank = Bank()

    sum = current_value.plus(Money.dollar(5))

    reduced = bank.reduce(sum, "USD")
    result = bank.reduce(Money.dollar(3), "USD")

    assert Money.dollar(10).equals(reduced)
    assert Money.dollar(3).equals(result)


def test_rates():
    bank = Bank()

    rate = bank.rate("USD", "USD")

    assert 1 == rate


def test_sum_different_currency():
    current_value = Money.franc(5)

    sum = current_value.plus(Money.dollar(5))

    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    reduced = bank.reduce(sum, "USD")

    assert Money.dollar(7.5).equals(reduced)

    sum = Money.dollar(5).plus(current_value)
    reduced = bank.reduce(sum, "USD")

    assert Money.dollar(7.5).equals(reduced)


def test_sum_plus_money():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)

    sum = Sum(five_bucks, ten_francs).plus(Money.dollar(5))

    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    reduced = bank.reduce(sum, "USD")

    assert Money.dollar(15).equals(reduced)


def test_sum_times():
    five_bucks = Money.dollar(5)
    ten_francs = Money.franc(10)

    sum = Sum(five_bucks, ten_francs).times(2)

    bank = Bank()
    bank.add_rate("CHF", "USD", 2)

    reduced = bank.reduce(sum, "USD")

    assert Money.dollar(20).equals(reduced)
