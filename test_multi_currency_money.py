from multi_currency_money import dollar


def test_dolar_mult_by_constant():
    curret_value = dollar(5)

    product = curret_value.times(2)
    assert product.amount == 10

    product = curret_value.times(4)
    assert product.amount == 20

    product = curret_value.times(7)
    assert product.amount == 35
