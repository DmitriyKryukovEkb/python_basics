class MyError(Exception):

    def __init__(self, in_list):
        self.list = in_list


class DigitList:

    def __init__(self, digit_list):
        self.digit_list = list(digit_list)
        self.digital = True
        self.dont_stop = True

    def digit_check(self):
        try:
            for i, el in enumerate(self.digit_list):
                try:
                    el = float(el)
                    if el.is_integer():
                        el = int(el)
                    self.digit_list[i] = el
                except ValueError:
                    self.digital = False
                    raise MyError(f'Список {self.digit_list} содержит нечисловые элементы')
        except MyError as error_1:
            print(error_1)
        if self.digital:
            print(f'В списке {self.digit_list} содержатся только числовые значения')

    def new_numbers(self):
        while self.dont_stop:
            number = input('Для выхода из цикла введите "stop". Введите новый элемент списка: ')
            if number.lower() in ('stop', 'стоп'):
                self.dont_stop = False
                break
            try:
                if not number.isdigit():
                    raise MyError('Будьте ласковы, в следующий раз введите число')
                else:
                    list_1.digit_list.append(int(number))
            except MyError as digit_error:
                print(digit_error)


list_1 = DigitList(input('Введите первоначальный список элементов через запятую: ').strip().split(','))
list_1.digit_check()
if list_1.digital:
    list_1.new_numbers()
    print(f'Результирующий список: {list_1.digit_list}')
else:
    print('Вы даже первоначальный список числами заполнить неспособны! Как вас можно пускать в бесконечный цикл, вы же '
          'выход не отыщите!')
