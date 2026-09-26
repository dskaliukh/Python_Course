name = input("Как тебя зовут? ")
print("Привет,", name)
age = int(input(f"{name}, Сколько тебе лет: "))
print(f"Отлично, тебе {age} лет!")
if age <= 40:
    age_ = age + 10
else:
    age_ = "много" 
print (f"Через 10 лет тебе будет {age_}.")