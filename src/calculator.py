"""Simple calculator module for demonstrating unit tests with GitHub Actions."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If the divisor is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the given exponent."""
    return base ** exponent


def square_root(n: float) -> float:
    """Return the square root of a non-negative number.

    Raises:
        ValueError: If the number is negative.
    """
    if n < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return n ** 0.5
