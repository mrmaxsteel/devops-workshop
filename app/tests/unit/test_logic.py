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

    def test_calculator_throws_e_when_out_of_bounds_low(self):
        with pytest.raises(Exception):
            Calculator(-1001,100)

    def test_calculator_throws_e_when_out_of_bounds_high(self):
        with pytest.raises(Exception):
            Calculator(-10,1001)

    def test_calculator_not_throw_e_when_in_bounds(self):
        Calculator(-10,10)

    def test_div_with_two_positive(self):
        calculator = Calculator()
        assert calculator.div(10,5) == 2

    def test_div_with_two_negative(self):
        calculator = Calculator()
        assert calculator.div(-10,-5) == 2

    def test_div_with_one_negative_one_positive(self):
        calculator = Calculator()
        assert calculator.div(-10,5) == -2
