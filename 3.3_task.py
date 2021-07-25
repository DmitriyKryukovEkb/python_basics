def my_func(a, b, c):  # первый метод решения
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        if a < b and a < c:
            return b + c
        elif b < a and b < c:
            return a + c
        else:
            return a + b
    except ValueError:
        return '"Нужны числовые аргументы"'


def my_func_2(a, b, c):  # второй метод решения
    try:
        func_list = [a, b, c]
        func_list.remove(min(func_list))
        return float(func_list[0]) + float(func_list[1])
    except TypeError:
        return '"Нужны числовые аргументы"'


def my_print(a, b, c, list_element):  # функция для вывода результатов
    print(f'Для {list_element} результат 1 функции: {my_func(a, b, c)}, результат 2 функции: {my_func_2(a, b, c)}.')


while True:
    answer_1 = input('У меня уже есть раздичные комбинации чисел, но Вы можете задать значения вручную. Хотите?(y/n): ')
    if answer_1 == 'y':
        user_list = []
        for i in range(1, 4):
            user_list.append(input(f'Введите {i}-е число: '))
        my_print(*user_list, user_list)
        break
    elif answer_1 == 'n':
        list_1 = [[3, 3, 1], [4, 2, 4], [3, 5, 5], [43, 'размер', 'ноги']]  # список с готовыми значениями
        for i in list_1:
            my_print(*i, list_element=i)
        break
