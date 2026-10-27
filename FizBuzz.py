a = int(input("Введите число от 1 до 100: "))
if a < 1 or a > 100:
    print("Введите число от 1 до 100!!")
elif a % 15 == 0:
    print("fizzbuzz")
elif a % 3 == 0:
    print("fizz")
elif a % 5 == 0:
    print("buzz")
else:
    print(a)