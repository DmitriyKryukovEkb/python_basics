time_seconds = int(input(f'Введите время в секундах: '))
hours = time_seconds // 3600
remainder = time_seconds % 3600
minutes = remainder // 60
seconds = remainder % 60
print(f'{hours:0>2}:{minutes:0>2}:{seconds:0>2}')
