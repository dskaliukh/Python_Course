with open("hello.txt", "a") as file:
    file.write("\nПривет! Я изучаю Python.")

n = 0   # Количество строк в файле
with open("hello.txt", "r") as file:
    for s in file:
        print (s, end='')
        n += 1
print("\nКоличество строк в файле :", n)
