while True:
    try:
        number = int(input("Введите число больше 0: "))
        if number < 0:
            print("Число должно быть положительным! Попробуйте ещё раз.")
        elif number == 0:
            print("Число должно быть больше 0! Попробуйте ещё раз.")
        else:
            break
    except ValueError:
        print("Ошибка! Попробуйте ещё раз.")

print("Вы ввели:", number)