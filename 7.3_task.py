class Cell:
    def __init__(self, length):
        self.length = length

    def __add__(self, other):
        return Cell(self.length + other.length)

    def __sub__(self, other):
        if self.length == other.length:
            print('Попытка вычитания клеток с равным количеством ячеек:')
        return Cell(abs(self.length - other.length))

    def __mul__(self, other):
        return Cell(self.length * other.length)

    def __truediv__(self, other):
        return Cell(int(self.length // other.length))

    def make_order(self, line_length):
        number_lines = self.length // line_length
        remain = self.length % line_length
        return ('*' * line_length + '\n') * number_lines + '*' * remain


cell_1 = Cell(3)
cell_2 = Cell(5)
cell_3 = Cell(5)
cell_4 = Cell(17)
print(f'Сложение:\n{(cell_1 + cell_2).make_order(8)}\n')
print(f'Вычитание:\n{(cell_4 - cell_2).make_order(8)}\n')
print(f'Умножение:\n{(cell_1 * cell_2).make_order(8)}\n')
print(f'Деление:\n{(cell_4 / cell_1).make_order(8)}\n')
print(f'{(cell_3 - cell_2).make_order(8)}\n')
