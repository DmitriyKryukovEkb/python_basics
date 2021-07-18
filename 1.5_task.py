proceeds = int(input('Введите выручку компании, руб: '))
costs = int(input('Введите издержки компании, руб: '))
profit = proceeds - costs
if profit < 0:
    print(f'Убыток компании составил {abs(profit)} руб')
else:
    staff = int(input('Введите количество сотрудников: '))
    print(f'Прибыль компании составила {profit} руб')
    print(f'Рентабельность компании {profit / proceeds * 100:.2f}%')
    print(f'Прибыль на одного сотрудника составила {profit/staff:.2f} руб')
