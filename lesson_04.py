from os import replace

with open("hello.txt", "w") as file:
    file.write("""\nПривет! Я изучаю Python.
Это адресная книга:
Иван Петрович
Пётр Иванович
Анна Васильевна
Иван Семёнович
Сергей Славович
""")

n = 0   # Количество строк в файле
nc = 0
s_in  = input("Введите строку, которую нужно заменить   : ")
s_out = input("Введите строку, на которую нужно заменить: ")

f_name = "hello"
with (open(f_name + ".txt", "r") as source,
      open(f_name + ".tmp", "w") as target):
    for line in source:
        if s_in in line:
            new_line = line.replace(s_in, s_out)
            target.write(new_line)
            print (f"{n:03d}: \"{line.rstrip('\n')}\" -> \"{new_line.rstrip('\n')}\"")
            nc += 1
        else:
            target.write(line)
            print (f"{n:03d}: \"{line.rstrip('\n')}\"")
        n += 1

replace(f_name + ".tmp", f_name + ".txt")
print("\nКоличество строк в файле   :", n)
print("Количество изменённых строк:", nc)
