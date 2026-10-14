from pathlib import Path 
from math    import isfinite


def save_order(total):
	"""	
		inf происходит от английского infinity — бесконечность.
		NaN происходит от Not a Number — «не число».
		
		a = float("inf")		# inf — положительная бесконечность.
		b = float("-inf")		# -inf — отрицательная бесконечность.
		c = float("nan")		# nan — «не число».
	"""
	# Проверяем что total является конечным положительным числом
	if  (not isinstance(total, (int, float)) 
	     or isinstance(total, bool) or not isfinite(total) 
		 or total <= 0):
		print("Ошибка: сумма должна быть конечным положительным числом.")
		return False
		
	# Каталог, в котором находится Python-файл
	base_dir = Path(__file__).parent

	# Путь к каталогу для заказов
	orders_dir = base_dir / "orders"

	# Создаём ошибочный путь для проверки конструкции except 
	"""
		Здесь:
		Path() создаёт объект пути.
		r"..." позволяет записать путь с обратными слешами 
		без обработки специальных последовательностей.
	""" 
	# orders_dir = Path(r"Z:\orders")

	# Путь к файлу для заказов
	file_path = orders_dir / "order.txt"

	try:
		# Создаём каталог, если его ещё нет
		# parents=True  — создать недостающие родительские каталоги.
		# exist_ok=True — не считать ошибкой уже существующий каталог.
		orders_dir.mkdir(parents=True, exist_ok=True)
		with file_path.open("w", encoding="utf-8") as file:
			file.write(f"Общая стоимость: {total:.2f}")
		return True
	except OSError as error:
		print(f"Ошибка сохранения файла: {file_path} ")
		print(error)
		return False

def get_num():
	while True:
		try:
			num = int(input("Введите количество товаров: "))
			if num <= 0:
				print("Количество должно быть больше нуля! Повторите ввод.")
			else:
				return num
		except ValueError:
			print("Ошибка! Это не число. Повторите ввод.")

def get_price(numero = 0):
	#print("numero = ", numero)
	if numero:
		prompt = f"Введите цену товара №{numero}: "
	else:
		prompt = "Введите цену товара: "
	while True:
		try:
			price = float(input(prompt))
			if  (not isfinite(price) or price <= 0):
				print("Цена должна быть конечным числом больше нуля! \nПовторите ввод.")
			else:
				return price
		except ValueError:
			print("Ошибка! Это не число. Повторите ввод.")



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
