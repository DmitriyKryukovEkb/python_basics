class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.lines = len(self.matrix)  # число строк
        self.columns = len(self.matrix[0])  # число столбцов
        for el in self.matrix:
            if len(el) != self.columns:  # проверка количества элементов в каждой строке
                print('Не совпадает количество столбцов в строках матрицы')
                raise TypeError
            for i in el:
                if not type(i) in (int, float):
                    print('Матрица содержит не числовые элементы')
                    raise TypeError

    def __str__(self):
        result_string = ''
        for string_list in self.matrix:
            temp_string = ''
            for el in string_list:
                temp_string += f'{el:<7}'
            result_string += f'{temp_string.strip()}\n'
        return result_string.strip()

    def __add__(self, other):
        result_matrix = []
        for line_1, line_2 in zip(self.matrix, other.matrix):
            result_line = []
            for el_1, el_2 in zip(line_1, line_2):
                result_line.append(el_1 + el_2)
            result_matrix.append(result_line)
        return Matrix(result_matrix)


try:
    matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
    matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
except TypeError:
    print('Неверные исходные данные')
    raise SystemExit(1)
print(f'{matrix_1}\n')
print(f'{matrix_2}\n')
print(matrix_1 + matrix_2)
