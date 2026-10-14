def calculate_order(*args, discount=0,  delivery=0):
    if discount  >= 0 and discount <= 100:
        order = 0
        for n in args:
            order += n
        return order * (1 - discount/100) + delivery
#    else:
#        print("Ошибка: скидка должна быть от 0 до 100 процентов.")

calc =  calculate_order(
    100,
    200,
    50,
    discount=-10,
    delivery=5
)

if calc is None:
    print("Ошибка: скидка должна быть от 0 до 100 процентов.")
else:
    print(calc)