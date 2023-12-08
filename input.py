from matrix import Matrix, MatrixOperations

def get_matrix_from_input():
    while True:
        try:
            rows = int(input("Введите количество строк матрицы: "))
            cols = int(input("Введите количество столбцов матрицы: "))
            if rows <= 0 or cols <= 0:
                raise ValueError("Количество строк и столбцов должно быть натуральным числом.")
            break  # Если ввод корректен, выходим из цикла
        except ValueError as e:
            print(f"Ошибка ввода: {e}")

    matrix = Matrix(rows, cols)

    print("Введите элементы матрицы:")
    for i in range(rows):
        for j in range(cols):
            while True:
                try:
                    value = float(input(f"Элемент [{i}][{j}]: "))
                    break  # Если ввод корректен, выходим из цикла
                except ValueError as e:
                    print(f"Ошибка ввода: Введите числовое значение.")

            matrix.matrix[i][j] = value

    return matrix

def main():
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение матриц")
        print("2. Умножение матриц")
        print("3. Умножение матрицы на скаляр")
        print("4. Транспонирование матрицы")
        print("5. Вычисление определителя матрицы")
        print("6. Вычисление обратной матрицы")
        print("0. Выйти")

        choice = input("Введите номер операции: ")

        if choice == "0":
            print("Программа завершена.")
            break

        if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Неверный выбор операции. Попробуйте снова.")
            continue

        num_matrices = 2 if choice in ["1", "2"] else 1

        matrices = []
        for i in range(num_matrices):
            print(f"\nВведите матрицу {i + 1}:")
            matrix = get_matrix_from_input()

            if matrix is not None:
                matrices.append(matrix)

        if choice == "1":
            # Сложение матриц
            if len(matrices) < 2:
                print("Для сложения матриц необходимо ввести как минимум две матрицы.")
                continue

            result_sum = matrices[0]
            for matrix in matrices[1:]:
                result_sum = MatrixOperations.add_matrices(result_sum, matrix)

            print("\nРезультат сложения матриц:")
            result_sum.display()

        elif choice == "2":
            # Умножение матриц
            if len(matrices) < 2:
                print("Для умножения матриц необходимо ввести как минимум две матрицы.")
                continue

            result_product = matrices[0]
            for matrix in matrices[1:]:
                result_product = MatrixOperations.multiply_matrices(result_product, matrix)

            print("\nРезультат умножения матриц:")
            result_product.display()

        elif choice == "3":
            # Умножение матрицы на скаляр
            if len(matrices) != 1:
                print("Для умножения матрицы на скаляр необходимо ввести только одну матрицу.")
                continue

            scalar = float(input("Введите скаляр: "))

            result_scalar_multiply = MatrixOperations.scalar_multiply(matrices[0], scalar)

            print("\nРезультат умножения матрицы на скаляр:")
            result_scalar_multiply.display()

        elif choice == "4":
            # Транспонирование матрицы
            if len(matrices) != 1:
                print("Для транспонирования матрицы необходимо ввести только одну матрицу.")
                continue

            result_transpose = MatrixOperations.transpose(matrices[0])

            print("\nРезультат транспонирования матрицы:")
            result_transpose.display()

        elif choice == "5":
            # Вычисление определителя матрицы
            if len(matrices) != 1:
                print("Для вычисления определителя матрицы необходимо ввести только одну матрицу.")
                continue

            det = MatrixOperations.determinant(matrices[0])

            print(f"\nОпределитель матрицы: {det}")

        elif choice == "6":
            # Вычисление обратной матрицы
            if len(matrices) != 1:
                print("Для вычисления обратной матрицы необходимо ввести только одну матрицу.")
                continue

            try:
                result_inverse = MatrixOperations.inverse(matrices[0])
                print("\nРезультат вычисления обратной матрицы:")
                result_inverse.display()
            except ValueError as e:
                print(f"Ошибка!")

if __name__ == "__main__":
    main()
