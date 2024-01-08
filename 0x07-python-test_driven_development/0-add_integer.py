def add_integer(a, b=98):
    """
    Adds two integers.

    The function takes two parameters, a and b. If a or b is not an integer or float,
    it raises a TypeError exception with the message "a must be an integer or b must be an integer".

    If a or b is a float, they are first casted to integers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float, optional): The second number. Default is 98.

    Returns:
    - int: The addition of a and b.

    Examples:
    >>> add_integer(2, 3)
    5

    >>> add_integer(-1, 1.5)
    0

    >>> add_integer(5.6, 4.3)
    10

    >>> add_integer('a', 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or b must be an integer
    """
    # Check if both a and b are either integers or floats
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Return the addition of a and b
    return a + b

