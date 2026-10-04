import pytest
from src import calculator


def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(2, -1) == 0.5


def test_factorial():
    assert calculator.factorial(0) == 1
    assert calculator.factorial(1) == 1
    assert calculator.factorial(5) == 120


def test_factorial_invalid():
    with pytest.raises(ValueError):
        calculator.factorial(-3)
    with pytest.raises(ValueError):
        calculator.factorial(2.5)
    with pytest.raises(ValueError):
        calculator.factorial("5")


def test_sigmoid():
    assert calculator.sigmoid(0) == 0.5
    assert calculator.sigmoid(2) == pytest.approx(0.8808, abs=1e-4)
    assert calculator.sigmoid(-2) == pytest.approx(0.1192, abs=1e-4)
    assert calculator.sigmoid(1000) == pytest.approx(1.0)
    assert calculator.sigmoid(-1000) == pytest.approx(0.0)


def test_invalid_inputs():
    with pytest.raises(ValueError):
        calculator.power("2", 3)
    with pytest.raises(ValueError):
        calculator.sigmoid("a")
