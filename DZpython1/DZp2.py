cop = int(input("Введите число от 1 до 99: "))
if 1 <= cop <= 99:
    print(end="")
    if 11 <= cop <= 14:
        print(cop, "копеек")
    else:
        ost = cop % 10
        if ost == 1:
            print(cop, "копейка")
        elif 2 <= ost <= 4:
            print(cop, "копейки")
        else:
            print(cop, "копеек")
else:
    print("Ошибка ввода данных")


