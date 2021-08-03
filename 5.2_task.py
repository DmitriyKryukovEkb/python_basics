with open('5.2_file.txt', 'r') as input_file:
    all_lines = input_file.readlines()
    print(f'В файле содержится {len(all_lines)} строк')
    for i, string in enumerate(all_lines, start=1):
        print(f'В {i}-й строке {len(string.split(" "))} слов.')
