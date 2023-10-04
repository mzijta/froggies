from example import add, subtract


def test_ex_add():
    assert add(3, 4) == 7
    assert add(2, 8) == 10


def test_ex_sub():
    assert subtract(4, 3) == 1
    assert subtract(2, 8) == -6
