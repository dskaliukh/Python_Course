
def get_flag(string="", yes="да", no="нет"):
    s = ""
    while s != yes and s != no:
            s = input(string)
            s = s.lower()
            s = s.replace(" ", "")
    if s == yes:
         return True
    else:
         return False

flag = True

while flag:
    name = input("Добрый день!\nКак Вас зовут? ")
    age = int(input(f"{name}, сколько Вам лет: "))

    if age >= 18 and get_flag("Есть билет? (да/нет):"):
        print ("Вход разрешён")
    else:
        print("Вход запрещён")
    flag = get_flag("Есть ли с Вами кто-то ещё? (да/нет)")