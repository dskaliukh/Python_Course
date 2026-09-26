with open("hello.txt", "w") as file:
    file.write("Привет! Я изучаю Python.")

with open("hello.txt", "r") as file:
    s = file.read()

print (s)
