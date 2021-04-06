from multi_currency_money import money, bank


def test_currency():
    assert money.dollar(5).currency() == "USD"
    assert money.franc(5).currency() == "CHF"


def test_equal_same_currency():
    assert money.dollar(5).equals(money.dollar(5))
    assert money.dollar(12).equals(money.dollar(12))
    assert not money.dollar(5).equals(money.dollar(6))


def test_equal_different_currency():
    assert not money.dollar(5).equals(money.franc(5))
    assert not money.dollar(12).equals(money.franc(12))
    assert not money.dollar(5).equals(money.franc(6))

    assert not money.franc(5).equals(money.dollar(6))


def test_dolar_mult_by_constant():
    curret_value = money.dollar(5)

    assert money.dollar(10).equals(curret_value.times(2))
    assert money.dollar(20).equals(curret_value.times(4))
    assert money.dollar(35).equals(curret_value.times(7))


def test_sum_currencies():
    current_value = money.dollar(5)

    sum = current_value.plus(money.dollar(5))

    bank_ = bank()

    reduced = bank.reduce(sum, "USD")

    assert money.dollar(10).equals(reduced)
