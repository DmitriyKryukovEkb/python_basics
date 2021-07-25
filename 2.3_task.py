month_list = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
month_dict = {0: 'Зима', 1: 'Весна', 2: 'Лето', 3: 'Осень', 4: 'Зима'}
while True:
    try:
        month = int(input('Введите месяц числом от 1 до 12: '))
        if 1 <= month <= 12:
            month_index = int(month / 3)
            print(f'Результат через список - {month_list[month_index]}')
            print(f'Результат через словарь - {month_dict[month_index]}')
            break
        else:
            print(f'{month} не входит в промежуток от 1 до 12')
    except ValueError:
        print("Нужно числовое значение")
