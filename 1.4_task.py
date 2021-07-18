number = input('Введите целое положительное число ')
i = len(number)
biggest_numeral = 0
while i > 0:
    if biggest_numeral < int(number[i-1]):
        biggest_numeral = int(number[i-1])
    i -= 1
print(f'Наибольшая цифра в числе равна {biggest_numeral}.')
