output_list = []
output_file = open('5.5_file.txt', 'w')
# print(f'{[el for el in range(1, 33)]}', file=output_file)
list_1 = [el for el in range(1, 33)]
string_1 = ''
for el in list_1:
    str5ing_1 = string_1 + ' ' + str(el)
print(string_1.strip(), file=output_file)
output_file.close()

total_sum = 0
with open('5.5_file.txt', 'r') as input_file:
    file_string = input_file.read()
    file_string = file_string.strip()
    file_list = file_string.split(' ')
    print(file_list)
    for el in file_list:
        total_sum = total_sum + int(el)
    print(total_sum)