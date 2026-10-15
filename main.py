from order_tools import *

n = get_num() 
total = 0
for i in range(n) :
	total += get_price (i + 1)

saved = save_order(total)

print(f"Общая цена: {total:.2f}")

if saved:
	print("Заказ успешно сохранён!")
else:
	print("Не удалось сохранить заказ!")