def only_digit(string_1):
    """ Функция принимает строку, ищет цифровые значения в ней. Возвращает список с числами.
    Если цифровые символы в строке ничем не разделены, они склеиваются в число, иначе -
    будут отдельными элементами списка.
    """
    list_1 = list(string_1)
    list_2 = []
    previous_digit = False
    list_2_counter = 0
    for el in list_1:
        if el.isdigit():
            if previous_digit:
                list_2[list_2_counter - 1] = str(list_2[list_2_counter - 1]) + str(el)
            else:
                list_2.append(el)
                list_2_counter += 1
            previous_digit = True
        else:
            previous_digit = False
    return list_2


def sum_for_list(input_list):  # функция складывает все элементы списка в одно число
    total_sum = 0
    try:
        for el in input_list:
            total_sum = total_sum + int(el)
        return total_sum
    except TypeError:
        print('Ошибка в функции сложения элементов листа. Неверные данные на входе')
        return None


with open('5.6_file.txt', 'r', encoding="utf-8") as schedule_file:
    schedule_list = schedule_file.readlines()
    dict_1 = {}
    for item in schedule_list:
        item_list = item.split(':')
        dict_2 = {str(item_list[0]): int(sum_for_list(only_digit(item_list[1])))}
        dict_1.update(dict_2)
    print(dict_1)
