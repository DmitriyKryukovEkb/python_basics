list_1 = [7, 5, 3, 3, 2,]
user_item = 1
while user_item >= 0:
    print(f'Текущий рейтинг: {list_1}')
    try:
        user_item = int(input(f'Введите новый элемент рейтинга. Для выхода из цикла введите отрицательное число: '))
    except ValueError:
        print('Недопустимый элемент')
        continue
    if user_item < 0:
        break
    if list_1[-1] > user_item:
        list_1.append(user_item)  # если значение меньше последнего элемента в рейтинге, добавляем его в конец
    else:
        for item in list_1:
            if item < user_item:
                list_1.insert(list_1.index(item), user_item)
                break
