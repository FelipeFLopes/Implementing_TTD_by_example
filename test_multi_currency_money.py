from multi_currency_money import dollar, franc


def test_equal_same_currency():
    assert dollar(5).equals(dollar(5))
    assert dollar(12).equals(dollar(12))
    assert not dollar(5).equals(dollar(6))
    assert franc(5).equals(franc(5))
    assert franc(12).equals(franc(12))
    assert not franc(5).equals(franc(6))


def test_equal_different_currency():
    assert not dollar(5).equals(franc(5))
    assert not dollar(12).equals(franc(12))
    assert not dollar(5).equals(franc(6))
    assert not franc(5).equals(dollar(5))
    assert not franc(12).equals(dollar(12))
    assert not franc(5).equals(dollar(6))


def test_dolar_mult_by_constant():
    curret_value = dollar(5)

    assert dollar(10).equals(curret_value.times(2))

    assert dollar(20).equals(curret_value.times(4))

    assert dollar(35).equals(curret_value.times(7))


def test_franc_mult_by_constant():
    curret_value = franc(5)

    assert franc(10).equals(curret_value.times(2))

    assert franc(20).equals(curret_value.times(4))

    assert franc(35).equals(curret_value.times(7))
