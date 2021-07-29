from sys import argv
script_name, rate_hour, worked_hours, bonus = argv
print(f'{script_name}:')
print(f'{rate_hour}руб/ч * {worked_hours}ч + {bonus}руб = {int(rate_hour) * int(worked_hours) + int(bonus)}')
