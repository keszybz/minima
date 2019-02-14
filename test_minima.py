import minima
import pytest

cases = [
    ([1, 4, -5, 0, 2, 1], [1, 4]),
    ([-1, -1, 0, -1],     [2]),
    ([4, 2, 1, 3, 1, 5],  [0, 3, 5]),
    ([1, 2, 2, 1],        [1,2]),
]

def test_0():
    assert minima.minima(cases[0][0]) == cases[0][1]

def test_1():
    assert minima.minima(cases[1][0]) == cases[1][1]

@pytest.mark.xfail
def test_2():
    assert minima.minima(cases[2][0]) == cases[2][1]

@pytest.mark.xfail
def test_3():
    assert minima.minima(cases[3][0]) == cases[3][1]
