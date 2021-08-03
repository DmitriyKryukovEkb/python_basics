numbers_dict = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять'}
with open('5.4_file_1.txt', 'r') as input_file, open('5.4_file_2.txt', 'w') as output_file:
    list_1 = input_file.readlines()
    for el in list_1:
        string_list = el.split(' - ')
        try:
            rus_number = numbers_dict[string_list[0].lower()]
        except KeyError:
            print('Проверьте входные данные')
            break
        print(f'{rus_number.title()} - {string_list[1].strip()}', file=output_file)