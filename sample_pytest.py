import pytest
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests

import pytest

# Function to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test cases
def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-3, -5) == -8

def test_subtract_numbers():
    assert subtract(10, 4) == 6

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add_parametrized(a, b, result):
    assert add(a, b) == result