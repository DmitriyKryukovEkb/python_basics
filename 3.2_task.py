def user_questionnaire(name, second_name, birth_year, city):
    print(f'{name} {second_name} {birth_year} года рождения, живет в {city}.')


name_1 = input('Введите ваше имя: ')
second_name_1 = input('Введите вашу фамилию: ')
birth_year_1 = input('Введите год вашего рождения: ')
city_1 = input('Введите город проживания: ')
user_questionnaire(name=name_1, second_name=second_name_1, city=city_1, birth_year=birth_year_1)
