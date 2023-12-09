import numpy as np


def adjoint(matrix):
    # Find the transpose of the matrix
    transpose = np.transpose(matrix)

    # Find the determinant of the matrix
    determinant = np.linalg.det(matrix)

    # Divide the transpose by the determinant to find the adjoint
    adjoint = transpose / determinant

    return adjoint


# Example usage
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
adjoint = adjoint(matrix1)
print(adjoint)
