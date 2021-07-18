my_str = 'Строчный тип данных'
my_number = 55
my_list = [1, 2, 3, 'пельмень', 5.54, True, {1: 'один', 2: 'два', 3: 'три'}, (3, 2, 3, 6), {5, 5, 5, 5, 7, 9, 3, 4}]
for item in my_list:
    print(item)
    print(type(item))
my_set_2 = {3, 2, 1}
print(my_list[8].intersection(my_set_2))
name = input('Как вас зовут? ')
age = int(input(f'{name}, сколько вам лет? '))
i = 0
friends_list = []
print('Напишите имена трёх своих друзей:')
while i < 3:
    friend = input(f'Введите имя {i+1}-го друга: ')
    friends_list.append(friend)
    i += 1
print(f'Вас зовут {name}, вам {age} лет и трёх ваших друзей зовут {friends_list}')
