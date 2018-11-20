import p2
def test_month_length():
    assert p2.month_length("January") == 31
    assert p2.month_length("February") == 28
    assert p2.month_length("February",leap_year=True) == 29
    assert p2.month_length("March") == 31
    assert p2.month_length("April") == 30
    assert p2.month_length("May") == 31
    assert p2.month_length("June") == 30
    assert p2.month_length("July") == 31
    assert p2.month_length("August") == 31
    assert p2.month_length("September") == 30
    assert p2.month_length("October") == 31
    assert p2.month_length("November") == 30
    assert p2.month_length("December") == 31
    assert p2.month_length("empty") == None



