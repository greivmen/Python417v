from math import pi


def rectangle():
    length = float(input("Длина: "))
    width = float(input("Ширина: "))
    ras = length * width
    print("Площадь:", ras)


def triangle():
    base = float(input("Основание: "))
    height = float(input("Высота: "))
    ras = 0.5 * base * height
    print("Площадь:", ras)


def circle():
    radius = float(input("Радиус: "))
    ras = round(pi * radius ** 2, 2)
    print("Площадь:", ras)


figura = input("1 - прямоугольник, 2 - треугольник, 3 - круг: ")

if figura == '1':
    rectangle()
elif figura == '2':
    triangle()
elif figura == '3':
    circle()
else:
    print("Ошибка ввода")
