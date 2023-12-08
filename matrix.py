import numpy as np

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

    def sum_of_elements(self):
        total_sum = sum(sum(row) for row in self.matrix)
        return total_sum

    def display(self):
        for row in self.matrix:   
            print(row)

    def _check_dimensions(self, other, operation):
        if operation == "сложение матриц" and (self.rows != other.rows or self.cols != other.cols):
            raise ValueError(f"Невозможно выполнить {operation}. Размеры матриц не совпадают.")


class MatrixOperations:
    @staticmethod
    def add_matrices(matrix1, matrix2):
        matrix1._check_dimensions(matrix2, "сложение матриц")
        result = Matrix(matrix1.rows, matrix1.cols)
        for i in range(matrix1.rows):
            for j in range(matrix1.cols):
                result.matrix[i][j] = matrix1.matrix[i][j] + matrix2.matrix[i][j]
        return result

    @staticmethod
    def multiply_matrices(matrix1, matrix2):
        matrix1._check_dimensions(matrix2, "умножение матриц")

        result = Matrix(matrix1.rows, matrix2.cols)
        for i in range(matrix1.rows):
            for j in range(matrix2.cols):
                for k in range(matrix1.cols):
                    result.matrix[i][j] += matrix1.matrix[i][k] * matrix2.matrix[k][j]
        return result

    @staticmethod
    def scalar_multiply(matrix, scalar):
        result = Matrix(matrix.rows, matrix.cols)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.matrix[i][j] = matrix.matrix[i][j] * scalar
        return result

    @staticmethod
    def transpose(matrix):
        result = Matrix(matrix.cols, matrix.rows)
        for i in range(matrix.rows):
            for j in range(matrix.cols):
                result.matrix[j][i] = matrix.matrix[i][j]
        return result

    @staticmethod
    def determinant(matrix):
        if matrix.rows != matrix.cols:
            raise ValueError("Матрица должна быть квадратной для вычисления определителя.")

        # Преобразуем матрицу в массив NumPy и используем np.linalg.det
        numpy_matrix = np.array(matrix.matrix)
        determinant_value = np.linalg.det(numpy_matrix)

        # Округляем значение до двух знаков после запятой
        rounded_determinant = round(determinant_value, 2)

        return rounded_determinant

    @staticmethod
    def inverse(matrix):
        determinant_value = MatrixOperations.determinant(matrix)
        if determinant_value == 0:
            raise ValueError("Матрица вырожденная, обратной матрицы не существует.")

        # Преобразуем матрицу в массив NumPy и используем np.linalg.inv
        numpy_matrix = np.array(matrix.matrix)
        inverse_matrix = np.linalg.inv(numpy_matrix)

        rounded_inverse_matrix = np.round(inverse_matrix, decimals=2)

        # Преобразуем результат обратно в объект Matrix
        result_matrix = Matrix(matrix.rows, matrix.cols)
        result_matrix.matrix = rounded_inverse_matrix.tolist()

        return result_matrix