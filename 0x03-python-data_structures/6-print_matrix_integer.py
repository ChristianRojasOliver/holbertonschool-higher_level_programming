#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix is None:
        return
    for r in range(len(matrix)):
        for x in range(len(matrix[r])):
            if (x < len(matrix[r]) - 1):
                print("{:d}".format(matrix[r][x]), end=" ")
            else:
                print("{:d}".format(matrix[r][x]))
    print()
