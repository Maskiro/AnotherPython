import os
import sys
fio = input('Ваше ФИО, пожайлуста:')
if not fio.replace(" ", "").isalpha():
    print('Введите ваше ФИО, а не цифры')
    quit()
birth = input('Ваш день рождения, в мм.дд.гг:')
if not birth.replace(".", "").isdigit():
    print('Неверно, нужны цифры, ваша дата рождения!')
    quit()
city = input('Ваш город рождения:')
if not city.isalpha():
    print('Введите ваше ФИО, а не цифры, любые цифровые значения пишите в буквах')
    quit()
city_now = input('Ваш город проживания(если имеется):')
if not city_now.isalpha():
    print('Ошибка данных, не пишите цифры. Любые цифровы значения пишите в буквах')
    quit()
print(f'Спасибо вам', fio, 'родом из', city, 'роживающий в городе', city_now)
print(f'Ваш день рождения:', birth)
number = input('Впишите, пожайлуста, свой номер телефона:')
print(f'Мы свяжимся с вами по номеру:', number) # хехехехехехеехехехехехехехехехехехехе