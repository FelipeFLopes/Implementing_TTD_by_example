from multi_currency_money import dollar

def test_dolar_mult_by_constant():
    curret_value = dollar(5)
    curret_value.times(2)
    assert curret_value.amount == 10

    curret_value = dollar(5)
    curret_value.times(4)
    assert curret_value.amount == 20

    curret_value = dollar(10)
    curret_value.times(7)
    assert curret_value.amount == 70