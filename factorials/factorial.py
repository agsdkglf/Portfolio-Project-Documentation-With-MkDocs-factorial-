"""Provide factorial counts.

This module allows the user to count the factorial of a given number.

    >>> from factorials import factorial
    >>> factorial.number_factorial(-2)
    Traceback (most recent call last):
    ...
    ValueError: n must be >= 0

    >>> factorial.number_factorial(1)
    1

    >>> factorial.number_factorial(12)
    6

The module contains the following function:

- `number_factorial(n)` - Returns the factorial of the number n.
"""

def number_factorial(n: int) -> int:
    """Find the factorial using recursion.

    Args:
    n: A number used to count its factorial.

    Returns:
    The product of all positive integers less than or equal to n.

    Raises:
    Exception: An error occurs when the value of n is not equal or greater than 0.
    """

    if n < 0:
        raise ValueError("n must be >= 0")
    elif n == 0 or n == 1:
        return 1
    else:
        # Recursive call to the function
        return n * number_factorial(n - 1)


# Take an input from the user
n = int(input("Enter a number >= 0: "))

# Call the factorial function
result = number_factorial(n)
print(result)
