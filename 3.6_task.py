def int_func_1(string_1):
    string_2 = string_1.upper()
    result = string_2[0:1] + string_1[1:]
    return result


def words_devision(string_1):  # функция делит строку на слова, исключая все пробелы, возвращает список
    string_1 = string_1.strip()  # метод удаляет пробельные символы в начали и конце строки
    while True:  # цикл для удаления двойных пробелов между словами
        if string_1.count('  ') > 0:
            string_1 = string_1.replace('  ', ' ')
        else:
            break
    word_list = string_1.split(' ')
    return word_list


user_string = input('Введите строку: ')
user_list = words_devision(user_string)  # получаем список слов
result_string = ''
try:
    for i in user_list:
        if i.isalpha():  # проверяем, чтобы элемент списка состоял только из букв
            result_string = result_string + ' ' + int_func_1(i)
        else:
            result_string = 1/0
            break
    print(result_string)
except ZeroDivisionError:
    print('Недопустимое значение')
