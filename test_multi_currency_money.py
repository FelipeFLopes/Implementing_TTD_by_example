from multi_currency_money import dollar


def test_dolar_mult_by_constant():
    curret_value = dollar(5)

    product = curret_value.times(2)
    assert product.amount == 10

    product = curret_value.times(4)
    assert product.amount == 20

    product = curret_value.times(7)
    assert product.amount == 35


def test_equal_same_currency():
    assert dollar(5).equals(dollar(5))
    assert dollar(12).equals(dollar(12))
    assert not dollar(5).equals(dollar(6))
