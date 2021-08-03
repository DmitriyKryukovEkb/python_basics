with open('5.3_file.txt', 'r') as input_file:
    list_1 = []
    all_lines = input_file.readlines()
    summary = 0
    for string in all_lines:
        string_list = string.split(' ')
        list_1.append(string_list)
        if int(string_list[1].strip()) < 20000:
            print(string_list[0])
        summary += int(string_list[1].strip())
print(f'Средний оклад сотрудника {summary/len(list_1):.2f}')
