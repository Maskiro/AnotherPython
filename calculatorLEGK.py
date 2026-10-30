frest = int(input("Введите число: "))
sec = int(input("Введите второе число: "))
calc = input("Введите операцию: +, -, *, /: ")
if calc == "+":
    print(frest + sec)
elif calc == "-":
    print(frest - sec)
elif calc == "*":
    print(frest * sec)
elif calc == "/":
    if sec == 0:
        print("Ошибка: деление на ноль!")
    else:
        print(f"{frest} / {sec} = {frest / sec}")
