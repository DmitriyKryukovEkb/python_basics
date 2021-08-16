from datetime import date


class Date:

    def __init__(self, string_date):
        self.string_date = string_date

    @classmethod
    def conv_digit(cls, string_date):
        output_list = []
        try:
            input_list = string_date.split('-')
            for i, el in enumerate(input_list):
                output_list.append(int(el))
            return output_list
        except Exception as err:
            print(f'Не удалось выделить дату из строки! {err}')


    @staticmethod
    def date_check(input_list):
        try:
            if not 0 < input_list[0] < 32:
                raise ValueError('День указан некорректно')
            elif not 0 < input_list[1] < 13:
                raise ValueError('Месяц указан некорректно')
            elif not 0 < input_list [2] <= date.today().year + 10:
                raise ValueError('Год указан некорректно')
        except ValueError as err:
            print(err)
        else:
            print('Дата проверена')


day_cls = Date('31-12-2021')
day = day_cls.conv_digit(day_cls.string_date)
print(f'{day[0]}.{day[1]}.{day[2]}')
if day:
    day_cls.date_check(day_cls.conv_digit(day_cls.string_date))
