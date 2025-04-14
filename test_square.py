from square import square_num
import pytest

# Test cases for the square_num function
def test_square_num_positive():
    assert square_num(2) == 4
    assert square_num(3) == 9
    assert square_num(4) == 16

def test_square_num_negative():
    assert square_num(-2) == 4
    assert square_num(-3) == 9
    assert square_num(-4) == 16

def test_square_num_zero():
    assert square_num(0) == 0
    assert square_num(0.0) == 0.0
    assert square_num(-0.0) == 0.0

