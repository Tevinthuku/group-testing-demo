def fun(a, b):
    return a + b


def minus(a, b):
    return b - a


def test_addition():
    assert fun(3, 5) == 8

# test_minus


def test_minus():
    assert minus(2, 5) == 3
