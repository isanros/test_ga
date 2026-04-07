"""Unit tests for the calculator module."""
import pytest

from src.calculator import add, subtract, multiply, divide, power, square_root


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-1, -4) == -5

    def test_add_zero(self):
        assert add(0, 0) == 0

    def test_add_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_add_mixed_sign(self):
        assert add(-3, 5) == 2


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(10, 4) == 6

    def test_subtract_resulting_negative(self):
        assert subtract(3, 7) == -4

    def test_subtract_same_numbers(self):
        assert subtract(5, 5) == 0

    def test_subtract_floats(self):
        assert subtract(3.5, 1.5) == pytest.approx(2.0)


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative_numbers(self):
        assert multiply(-2, -3) == 6

    def test_multiply_mixed_sign(self):
        assert multiply(-2, 4) == -8

    def test_multiply_floats(self):
        assert multiply(2.5, 4.0) == pytest.approx(10.0)


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_resulting_float(self):
        assert divide(1, 3) == pytest.approx(0.333, rel=1e-2)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero."):
            divide(10, 0)

    def test_divide_negative(self):
        assert divide(-10, 2) == -5.0


class TestPower:
    def test_power_positive_exponent(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_one_exponent(self):
        assert power(7, 1) == 7

    def test_power_negative_exponent(self):
        assert power(2, -1) == pytest.approx(0.5)


class TestSquareRoot:
    def test_square_root_perfect_square(self):
        assert square_root(9) == pytest.approx(3.0)

    def test_square_root_zero(self):
        assert square_root(0) == pytest.approx(0.0)

    def test_square_root_float(self):
        assert square_root(2.0) == pytest.approx(1.41421, rel=1e-4)

    def test_square_root_negative_raises(self):
        with pytest.raises(ValueError, match="Cannot compute square root of a negative number."):
            square_root(-1)
