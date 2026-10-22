import random
long = int(input('Введите длину пароля: '))
if long < 1:
    print('Длина пароля должна быть больше 0')
if long > 20:
    print('Длина пароля должна быть меньше 20')
else:
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()') for i in range(long))
    print('Ваш пароль:', password)