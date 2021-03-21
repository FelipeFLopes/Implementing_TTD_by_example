from multi_currency_money import dollar

def test_dolar_mult_by_constant():
    curret_value = dollar(5)
    curret_value.times(2)
    assert curret_value.amount == 10
