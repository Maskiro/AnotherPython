name = input("Введите свое имя: ")
surname = input("Введите свою фамилию: ")
if surname == "":
    print("Вы не ввели фамилию.")
if name == "":
    print("Вы не ввели имя.")
else:
    print("Привет, ", name, surname + '!')
if name.islower() or surname.islower():
    print(f"Напишите ваше имя и фамилию с заглавной буквы: {name.capitalize()} {surname.capitalize()}")