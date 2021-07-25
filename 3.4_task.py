def my_func_1(x, y):
    try:
        x, y = float(x), int(y)
    except ValueError:
        return 'Недопустимое значение аргумента'
    result = 1
    if y < 0:
        for i in range(abs(y)):
            result = result / x
    else:
        for i in range(y):
            result = result * x
    return result


def my_func_2(x, y):
    try:
        x, y = float(x), int(y)
    except ValueError:
        return 'Недопустимое значение аргумента'
    result = x ** y
    return result


number = input('Введите число: ')
exponent = input('Введите степень: ')
print(f'Результат возведения первой функции: {my_func_1(number, exponent):.10f}')
print(f'Результат возведения второй функции: {my_func_2(number, exponent):.10f}')
