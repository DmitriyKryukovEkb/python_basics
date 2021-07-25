def division(a, b):
    try:
        result = float(a) / float(b)
        return result
    except ZeroDivisionError:
        print('Деление на 0.')
    except ValueError:
        print('Нужны числовые значения.')


number_1 = input('Введите числитель: ')
number_2 = input('Введите знаменатель: ')
print(f'{division(number_1, number_2):.2f}')
