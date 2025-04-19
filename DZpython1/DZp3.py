a = int(input("Количество символов: "))
b = input("Тип символа: ")
n = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
i = 0
while i < a:
    if n == 0:
        print(b, end=" ")
    elif n == 1:
        print(b)
    else:
        print("Данные ввода не корректны")
        break
    i += 1


