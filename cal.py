def div(a: int | float, b: int | float) -> float:
    """
    Divide two numbers and return the result.
    Args:
        a (int | float): Numerator
        b (int | float): Denominator
    Returns:
        float: Result of division
    Raises:
        TypeError: If a or b is not a number
        ZeroDivisionError: If b is zero

    Author:
        Dhruv Koli <googldhruv@gmail.com>
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers.")

    if b == 0:
        raise ZeroDivisionError("divide by zero.")

    return a / b

def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers and return the result.

    Args:
        a (float): First number
        b (float): Second number

    Returns:
        float: Product of a and b

    Author: Amritanshu Aditya 23BCS013
    """
    return a * b

def sub(a: int | float, b: int | float) -> float:
    """
    Subtract two numbers and return the result.
    Args:
        a (int | float): Minuend
        b (int | float): Subtrahend
    Returns:
        float: Result of subtraction
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numbers.")

    return a - b
