user_list = list(input('Введите список: '))
print(user_list)
len_count = len(user_list)
for i in range(0 , len_count - 1):
    if i % 2 == 0:
        user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
print(user_list)
