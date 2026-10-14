"""
Что мы сейчас действительно освоили
*args → собирает позиционные аргументы в tuple;
**kwargs → собирает именованные аргументы в dict;
keys() → ключи;
values() → значения;
items() → ключ + значение;
перебор словаря через for;
использование *args и **kwargs вместе
"""

def show(**kwargs):
    #print(kwargs)
    for k , v in kwargs.items():
        print(k.ljust(4), ' = ', v)


#show(name="Dmitry", age=47, city="Madrid")

def test(*args, **kwargs):
    print(args)
    print(kwargs)

#test(5, 10, 15, name="Anna", age=30)

def info(*args, **kwargs):
    print("Числа:")
    for n in args:
        print(n)
    print("\nПараметры:")
    for k, v in kwargs.items():
        print(k.ljust(5)," = " , v)

info(10, 20, 30, name="Dmitry", city="Madrid")

count = 0

def add_count():
    global count
    count += 1
    
add_count()
add_count()
add_count()

print(count)