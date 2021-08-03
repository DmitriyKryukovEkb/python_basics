with open('5.7_file.txt', 'r', encoding="utf-8") as firm_file:
    all_lines_list = firm_file.readlines()
    profit_counter = total_profit = 0
    firm_dict = {}
    for firm in all_lines_list:
        firm = firm.strip()
        firm_list = firm.split(' ')
        profit = int(firm_list[2]) - int(firm_list[3])
        if profit >= 0:
            profit_counter += 1
            total_profit += profit
        firm_dict.update({firm_list[1] + ' ' + firm_list[0]: profit})
    average_dict = {'average_profit': total_profit/profit_counter}
    final_list = [firm_dict, average_dict]
import json
with open('5.7_json', 'w') as firm_json:
    json.dump(final_list, firm_json, ensure_ascii=False)
