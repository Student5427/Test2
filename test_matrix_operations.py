import numpy as np
import unittest
from matrix import Matrix, MatrixOperations

class TestMatrixOperations(unittest.TestCase):
    def test_sum_of_elements(self):
        matrix = Matrix(2, 2)
        matrix.matrix = [[1, 2], [3, 4]]
        result = matrix.sum_of_elements()
        self.assertEqual(result, 10, "Sum of elements calculation is incorrect")

    def test_add_matrices(self):
        matrix1 = Matrix(2, 2)
        matrix1.matrix = [[1, 2], [3, 4]]
        matrix2 = Matrix(2, 2)
        matrix2.matrix = [[5, 6], [7, 8]]
        result = MatrixOperations.add_matrices(matrix1, matrix2)
        self.assertEqual(result.matrix, [[6, 8], [10, 12]])

    def test_multiply_matrices(self):
        matrix1 = Matrix(2, 2)
        matrix1.matrix = [[1, 2], [3, 4]]
        matrix2 = Matrix(2, 2)
        matrix2.matrix = [[5, 6], [7, 8]]
        result = MatrixOperations.multiply_matrices(matrix1, matrix2)
        self.assertEqual(result.matrix, [[19, 22], [43, 50]])

    def test_scalar_multiply(self):
        matrix = Matrix(2, 2)
        matrix.matrix = [[1, 2], [3, 4]]
        scalar = 2
        result = MatrixOperations.scalar_multiply(matrix, scalar)
        self.assertEqual(result.matrix, [[2, 4], [6, 8]])

    def test_transpose(self):
        matrix = Matrix(2, 3)
        matrix.matrix = [[1, 2, 3], [4, 5, 6]]
        result = MatrixOperations.transpose(matrix)
        self.assertEqual(result.matrix, [[1, 4], [2, 5], [3, 6]])

    def test_determinant(self):
        matrix = Matrix(2, 2)
        matrix.matrix = [[1, 2], [3, 4]]
        result = MatrixOperations.determinant(matrix)
        self.assertEqual(result, -2)

    def test_inverse(self):
        # Create a matrix
        matrix = Matrix(2, 2)
        matrix.matrix = [[4, 7], [2, 6]]

        # Calculate the inverse using the inverse method
        result_inverse = MatrixOperations.inverse(matrix)

        # Expected result for the given matrix
        expected_result = [[0.6, -0.7], [-0.2, 0.4]]

        # Check if the result matches the expected inverse matrix
        self.assertEqual(result_inverse.matrix, expected_result)

    def test_determinant_non_square_matrix(self):
        matrix = Matrix(2, 3)
        with self.assertRaises(ValueError):
            MatrixOperations.determinant(matrix)

# Интеграционные тесты
class TestIntegrationMatrixOperations(unittest.TestCase):
    def test_multiply_matrices_and_scalar_multiply(self):
        matrix1 = Matrix(2, 2)
        matrix1.matrix = [[1, 2], [3, 4]]
        matrix2 = Matrix(2, 2)
        matrix2.matrix = [[5, 6], [7, 8]]
        result_multiply = MatrixOperations.multiply_matrices(matrix1, matrix2)
        scalar = 2
        result = MatrixOperations.scalar_multiply(result_multiply, scalar)
        self.assertEqual(result.matrix, [[38, 44], [86, 100]])

    def test_transpose_and_determinant(self):
        matrix = Matrix(3, 3)
        matrix.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result_transpose = MatrixOperations.transpose(matrix)
        print(result_transpose)
        result_determinant = MatrixOperations.determinant(result_transpose)
        self.assertEqual(result_determinant, 0)
