import pytest
import app

def test_add():
    assert app.add(2, 3) == 5

def test_subtract():
    assert app.subtract(5, 3) == 2

def test_multiply():
    assert app.multiply(4, 3) == 12

def test_divide():
    assert app.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        app.divide(10, 0)
