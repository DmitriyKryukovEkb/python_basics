with open('5.1_file.txt', 'w') as my_file:
    counter = 1
    while True:
        my_string = input(f'Введите {counter} строку: ')
        my_file.write(f'{my_string} \n')
        if len(my_string) < 1:
            break
        elif counter > 20:
            break
        counter += 1
