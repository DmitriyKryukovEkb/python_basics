def fact(n):
    var_1 = 1
    for i in range(1, n + 1):
        var_1 = var_1 * i
        yield var_1


try:
    user_number = int(input('Введите число для вычисления факториала: '))
except TypeError:
    print('Неверное значение. Нужно целое число.')
print(*[el for el in fact(user_number)])
