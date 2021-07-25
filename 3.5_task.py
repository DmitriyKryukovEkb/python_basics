def my_func_5(string_1):
    string_1 = string_1.strip()  # метод удаляет пробельные символы в начали и конце строки
    while True:  # цикл для удаления двойных пробелов между числами
        if string_1.count('  ') > 0:
            string_1 = string_1.replace('  ', ' ')
        else:
            break
    list_1 = string_1.split(' ')
    summary = 0
    try:
        for i in list_1:
            summary = float(summary + float(i))
        return summary
    except (ValueError, TypeError):
        print('Функция не выполнена из-за недопустимого аргумента')
        return 0


global_sum = 0
while True:
    user_string = input('Введите числа через пробел, для выхода из цикла ведите "/": ')
    if user_string[0] == '/':
        break
    elif user_string.count('/') > 0:
        user_string = user_string[0:user_string.index('/')]
        print(f'Сумма равна: {global_sum + my_func_5(user_string)}')
        break
    else:
        global_sum = global_sum + my_func_5(user_string)
        print(f'Сумма равна: {global_sum}')
