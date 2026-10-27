"""
Simple calculator module - Lab 6 (Automatic Build using PyBuilder)
Author: Firyal Al Sharabati
"""
import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y


# ---------------- Graded exercise: new functions ----------------

def modulus(x, y):
    """Return the remainder of x divided by y."""
    if y == 0:
        raise ValueError("Cannot take modulus by zero.")
    return x % y


def power(base, exponent):
    """Return base raised to the power of exponent."""
    return base ** exponent


def square_root(x):
    """Return the square root of x (x must be non-negative)."""
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)
