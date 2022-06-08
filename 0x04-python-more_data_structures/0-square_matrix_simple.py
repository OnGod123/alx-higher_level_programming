def square_matrix_simple(matrix=[]):
    """
    Input: 2 Dimension Matrix
    
    Return: Matrix whose element are squared the value of the input matrix
    """
    new_matrix = []

    for row in matrix:
        new_row = list(map((lambda x: x**2), row))
        new_matrix.append(new_row)

    return new_matrix
