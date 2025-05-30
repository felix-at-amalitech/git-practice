import pytest
from math_utils import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -3) == -3
