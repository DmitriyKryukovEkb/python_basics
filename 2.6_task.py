main_list = []
names_list = []
prices_list = []
amounts_list = []
units_list = []
try:
    tuple_amount = int(input('Введите количество товаров: '))
    if tuple_amount < 0:
        tuple_amount = 1 / 0  # не может быть отрицательное количество товаров
    i = 0
    while i < tuple_amount:
        i += 1
        product_name = input(f'Введите наименование {i} товара: ')
        try:
            product_price = float(input(f'Введите цену для {product_name}: '))
            if product_price < 0:  # цена не может быть отрицательной
                product_price = 1 / 0
        except (ValueError, ZeroDivisionError):
            print('Нужно положительное число')
            i -= 1  # в случае ошибки заново начинаем запись характеристик этого товара
            continue
        try:
            product_amount = int(input(f'Введите количесство для {product_name}: '))
            if product_amount < 0:  # количество не может быть отрицательным
                product_amount = 1 / 0
        except (ValueError, ZeroDivisionError):
            print('Нужно положительное число')
            i -= 1  # в случае ошибки заново начинаем запись характеристик этого товара
            continue
        product_unit = input(f'Введите единицы измерения количества для {product_name}: ')
        main_list.append((i, {"Наименование": product_name, "Цена": product_price, "Количество": product_amount,
                          "Ед. измерения": product_unit}))
        names_list.append(product_name)
        prices_list.append(product_price)
        units_list.append(product_unit)
        amounts_list.append(product_amount)
    print(main_list)
    names_dict = {"Наименование": names_list}
    print(names_dict)
    prices_dict = {"Цена": prices_list}
    print(prices_dict)
    units_dict = {"Ед. измерения": units_list}
    print(units_dict)
    amounts_dict = {"Количество": amounts_list}
    print(amounts_dict)
except (ValueError, ZeroDivisionError):
    print('Необходимо целое положительное число')
