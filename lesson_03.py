name = input("Добрый день!\nКак Вас зовут? ")
age = int(input(f"{name}, сколько Вам лет: "))
ticket = ""
if age >= 18:
    while ticket != "да" and ticket != "нет":
        ticket = input("Есть билет? (да/нет):")
if age >= 18 and ticket == "да":
    print ("Вход разрешён")
else:
    print("Вход запрещён")