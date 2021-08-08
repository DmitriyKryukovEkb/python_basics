"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)


    def get_full_name(self):
        print(f'Имя сотрудника {self.name} {self.surname}.')

    def get_total_income(self):
        print(f'{self.name} заработал {int(self._income["wage"]) + int(self._income["bonus"])} руб')


seller = Position('Василий', 'Тёркин', 'продавец', {"wage": 30000, "bonus": 7500})
seller.get_full_name()
seller.get_total_income()
