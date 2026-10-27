yrpsw = str(input('Введите свой пароль, он должен быть не менее 10 знаков и не содержать пробелы, а так же иметь спец символы и цифры: '))
while True:
    spac = " " in yrpsw
    spec = any(not c.isalnum() and not c.isspace() for c in yrpsw)
    simf = int(sum(1 for char in yrpsw if char.isalpha()))
    sim = int(sum(1 for char in yrpsw if char.isdigit()))
    if simf + sim < 10:
        print('Слишком маленький пароль! Попробуйте снова')
        continue
    elif yrpsw and spac:
        print('Присутсвуют пробелы!!! Попробуйте снова')
        continue
    elif not spec:
        print('Нет спец. символов! Попробуйте снова')
        continue
    elif not sim:
        print('Нету цифр! Попробуйте снова')
        continue
    elif print('Ваш пароль подходит!'):
        print(f'Ваш пароль: {yrpsw}')
    break