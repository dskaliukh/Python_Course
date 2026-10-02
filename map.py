print('четыреста')
#print(#'пятнадцатая')
print('база')
# print('ответьте')
print('Жизнь как коробка шоколадных конфет')
print
print('никогда не знаешь, что тебе попадётся.')

a = list( map(int, map(float, input("Введите значения через пробел").split()) ))

sum = 0
for n in a:
    sum += n

print("Summa =", sum)

number = 7.999
print(number, type(number))

int_number = int(number)
print(int_number, type(int_number))

string_number = str(number)
print(string_number, type(string_number))

a = input()
b = int(input())
print(a * b)