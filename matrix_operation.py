import numpy as np


def rotate_matrix(matrix):
    width, height = matrix.shape[:2]
    if width != height:
        raise ValueError("Matrix needs to be square!")

    new_matrix = np.zeros(matrix.shape, dtype=matrix.dtype)
    for x in range(width):
        for y in range(height):
            new_matrix[x][y] = matrix[height - 1 - y][x]

    return new_matrix


def pretty_print(matrix, digits=2):
    str_value = "{:%d} " % digits

    result = ""

    width, height = matrix.shape[:2]
    for x in range(width):
        for y in range(height):
            result += str_value.format(matrix[x][y])
        result += "\n"

    print(result)


def test_rotate_matrix():
    width, height = 5, 5
    matrix = np.arange(width * height).reshape((width, height))
    pretty_print(matrix)

    new_matrix = rotate_matrix(matrix)
    pretty_print(new_matrix)


if __name__ == '__main__':
    test_rotate_matrix()
