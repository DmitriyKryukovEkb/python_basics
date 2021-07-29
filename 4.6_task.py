from itertools import count, cycle
# первая часть задания:
try:
    start_number = int(input('Введите начальное целое число: '))
    for i in count(start_number):
        if i > 15:
            break
        print(i)
except TypeError:
    print('Неверное значениею')
# вторая часть задания:
list_1 = ['Нога', 'Колено', 'Голова', 'Плечо', 'Локоть', 'Кисть']
counter = 0
for i in cycle(list_1):
    print(i)
    counter += 1
    if counter > 10:
        break
