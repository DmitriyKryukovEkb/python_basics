from random import randint


class MyError (Exception):

    def __init__(self, txt):
        self.txt = txt


numerator = randint(1, 1000)
denominator = input(f'Числитель {numerator}. Введите знаменатель: ')
try:
    if int(denominator) == 0:
        raise MyError('Хватит толкать меня на математическое правонарушение!')
    result = (numerator / int(denominator))
except ValueError:
    print('Может быть Вы прекратите издеваться?')
except MyError as situation:
    print(situation)
else:
    print(f'{numerator} / {denominator} = {result}')
