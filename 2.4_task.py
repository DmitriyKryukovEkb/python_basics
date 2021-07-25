user_str = input('Введите несколько слов: ')
user_str = user_str.strip()  # метод удаляет пробельные символы в начали и конце строки
while True:  # цикл для удаления двойных пробелов между словами
    if user_str.count('  ') > 0:
        user_str = user_str.replace('  ', ' ')
    else:
        break
word_count = user_str.count(' ') + 1
count_edit = 0
for i in range(1, word_count):
    index_space = user_str.index(' ')
    if index_space > 10:  # проверяем длину слова, если больше 10 символов - выводим только до 10 символа
        print(f'{i + count_edit}. {user_str[0:10]}')
    else:
        print(f'{i + count_edit}. {user_str[0:index_space]}')
    user_str = user_str[index_space + 1:]
print(f'{word_count + count_edit}. {user_str[0:10]}')  # печатаем последнее слово
