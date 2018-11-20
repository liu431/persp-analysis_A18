import p1
def test_smallest_factor():
    assert p1.smallest_factor(1) == 1
    assert p1.smallest_factor(2) == 2
    assert p1.smallest_factor(3) == 3
    assert p1.smallest_factor(4) == 2
    assert p1.smallest_factor(5) == 5
    assert p1.smallest_factor(6) == 2
    assert p1.smallest_factor(9) == 3
    assert p1.smallest_factor(100) == 2

