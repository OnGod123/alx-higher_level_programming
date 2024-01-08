# 2_matrix_divided.py

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The divisor.

    Returns:
    - list of lists: A new matrix with elements rounded to 2 decimal places after division.

    Examples:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    >>> matrix_divided([[1, 2, 3], [4, 5, 'a']], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], '2')
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    """
    # Your matrix division implementation goes here

if __name__ == "__main__":
    # If the module is run as a script, run the doctests
    import doctest
    doctest.testmod()

