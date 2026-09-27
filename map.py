a = list( map(int, input("Введите значения через пробел").split()) )

sum = 0
for n in a:
    sum += n
    
print("Summa =", sum)