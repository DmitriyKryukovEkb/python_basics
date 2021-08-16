class Com_number:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary < 0:
            return f'z = {self.real} - {-self.imaginary}i'
        else:
            return f'z = {self.real} + {self.imaginary}i'

    def __add__(self, other):
        return Com_number(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Com_number(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary +
                          self.imaginary * other.real)


n_1 = Com_number(9, 5)
n_2 = Com_number(-5, 6)
print(n_1)
print(n_2)
print(f'Результат сложения: {n_1 + n_2}')
print(f'Результат умножения: {n_1 * n_2}')
