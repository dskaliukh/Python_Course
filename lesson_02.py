name = input("Как тебя зовут? ")
print("Привет,", name)
age = int(input(f"{name}, Сколько тебе лет: "))
print(f"Отлично, тебе {age} лет!")

age_ = "Пенсионер"
if age < 13:
    age_ = "Ребёнок"
elif age < 18:
    age_ = "Подросток" 
elif age < 65:
    age_ = "Взрослый" 


print (f"Ты {age_}.")