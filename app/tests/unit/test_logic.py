import pytest
from unittest import TestCase
from calculator.logic import Calculator


class CalculatorTests(TestCase):
    def test_mul_with_two_positive_numbers(self):
        calculator = Calculator()
        assert calculator.mul(5,10) == 50

    def test_mul_with_two_negative_numbers(self):
        calculator = Calculator()
        assert calculator.mul(-5,-10) == 50

    def test_mul_with_one_negative_one_positive(self):
        calculator = Calculator()
        assert calculator.mul(-5,10) == -50

    def test_calculator_throws_e_when_out_of_bounds(self):
        with pytest.raises(Exception) as e_info:
            calculator = Calculator(-1001,100)

    def test_div(self):
        pass
