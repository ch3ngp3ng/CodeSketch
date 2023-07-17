# test_my_model.py

import pytest
from model import add_numbers


def main():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
