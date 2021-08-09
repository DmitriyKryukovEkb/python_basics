from abc import ABC, abstractmethod


def summary_list(input_list):  # результат функции - сумма элементов в списке
    result = 0
    for el in input_list:
        result += el
    return result


clothes_list = []


class Clothes:
    def __init__(self, param):
        self.param = param
        clothes_list.append(self)

    @property
    def param(self):
        return self.__param

    @param.setter
    def param(self, param):
        if param < self.min_param:
            self.__param = self.min_param
        elif param > self.max_param:
            self.__param = self.max_param
        else:
            self.__param = param

    @abstractmethod
    def calculate(self):
        pass


class Suits(Clothes):
    min_param = 1.40
    max_param = 2.30

    def calculate(self):
        self.expense = 2 * self.param + 0.3
        return self.expense


class Coats(Clothes):
    min_param = 32
    max_param = 70

    def calculate(self):
        self.expense = self.param / 6.5 + 0.5
        return self.expense


suit_1 = Suits(1.2)
print(f'{suit_1.calculate():.2f} м')
coat_1 = Coats(70)
print(f'{coat_1.calculate():.2f} м')
coat_2 = Coats(78)
print(f'{coat_2.calculate():.2f} м')

expense_list = []
for item in clothes_list:
    expense_list.append(item.expense)

print(f'Общие затраты ткани составят {summary_list(expense_list):.2f} метров')
