# name = "5"
# age = 20
# print(name, type(name))
# print(age, type(age))
# print(name + str(age))
# a = 4
# b = 5
# print("a  =", a, id(a))
# print("b  =", b, id(b))
# a = b
# print("a  =", a, id(a))
# print("b  =", b, id(b))
# a = b = c = 5
# a, b, c = 5, 'Hello', 9.2
# print(a)
# print(b)
# print(c)
import json
import random
import time
from dataclasses import asdict
from itertools import count
from platform import python_implementation
from runpy import run_path
from sys import prefix
from textwrap import dedent
from tkinter.font import names

# first_name = "admin"
# print(first_name)
#
#
# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)

# a = 1
# b = 2
# print('a:', a)
# print('b:', b)

# c = a  # c = 1
# a = b  # a = 2
# b = c  # b =  1

# a, b = b, a
# print('a:', a)
# print('b:', b)
#
# print("строка "
#       "символов")
# print('эстрона символов эстрона символов \nэстрона символов эстрона символов')

# s1 = 'Hello'
# s2 = 'Python'
# s3 = s1 + " " + s2 + "___"
# print(s3)
# print(s3 * 3)
#

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 ** 2)
# print(7 / 2)
# print(7 // 2)
# print(7.5 % 2)

# a, b, c = 5, 7, 3
# sum_ = a + b + c
# print("Сумма:",sum_)
# print("Произведение", a * b * c)
# print("Среднее арифмитическое", sum_ / 3)
# print(sum_)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)


# num = 97531
# print("Исходное число", num)
#

# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# print("Обратное число", res)
# print("Среднее арифметическое", num / 5)


# name = "Вадим"
# age = 33
# print("Меня зовут", name, ". Мне", age, "лет")
# print("Меня зовут " + name + ". Мне " + str(age), "лет")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="", end="\n\n")
# print("Новая строка")

# name = input("Ваше имя: ")
# print("Hello", name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# res = num ** power
# print("Число", num, "в степени", power, "равно:", res)
#
# b1 = True
# b2 = False
# # print((b1, type(b1))
# print(b1 + 5)
# print(b2 + 5)

# print(bool("python"))
# print(bool(""))
# print(bool(5))
# print(bool(-5))
# print(bool(0))
# print(True)
# print(False)
# print(None)

# test = None
# print(test, type(test))
# test = 5
# print(test, type(test))

# print(7 == 7)
# print(2 + 5 == 7 + 3)
# print(7 != 10 - 3)
# print(8 > 5)
# print(8 >= 8)
#
# print(8 < 5)
# print(8 >= 8)
#
# print("hello" > "HELLO")

# print(5 - 3 == 2 and 1 + 3 == 4)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
#     print("Добро пожаловать")
# else:
#     print("Доступ запрещен")
#

# import this
# print(this)

# a = input("Введите первую сторону:")
# b = input("Введите вторую сторону:")
# c = input("Введите третью сторону:")
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or b == c or a == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if (day >= 1) and day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресение")
# else:
#     print("Токого дня не существует")
#

# n = int(input("Введите количество ворон - "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода даных")


# n = int(input("Введите количество ворон - "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# ----вВОРОНЫ
# n = int(input("Введите количество ворон - "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# DZ---1
# num = 97531
# print("Исходное число", num)
# a = num // 10000
# b = num // 1000 % 10
# c = num // 100 % 10
# d = num // 10 % 10
# e = num // 1 % 10
# pr = a * b * c * d * e
# ar = (a + b + c + d + e) / 5
# print("Произведение цифр числа:", pr)
# print("Среднее  арифметическое:", ar)


# n = int(input("Введите количество ворон - "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")
#


# n = int(input("Введите число от 1 до 99: "))
#
# if 1 <= n <= 99:
#     print("В кармане:", end=" ")
#
#
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите число от 1 до 99: "))
# if 11 <= n <= 19:
#     print(n, "копеек")
# a = n % 10
# if a == 1:
#     print(n, "копейка")
# elif 2 <= a <= 4:
#     print(n, "копейки")
# else:
#     print(n, "копеек")


# n = int(input("Введите число от 1 до 99: "))
#
# if 1 <= n <= 99:
#     print("В кармане:", end=" ")
#     if 11 <= n <= 14:
#         print(n, "копеек")
# a = n % 10
# if a == 1:
#     print(n, "копейка")
# elif 2 <= a <= 4:
#     print(n, "копейки")
# else:
#     print("Ошибка ввода данных")


# n = int(input("Введите число от 1 до 99: "))
# a = n % 10
# if a == 1:
#     print(n, "копейка")
#     if 2 <= a <= 4:
#         print(n, "копейки")
#     if 11 <= n <= 19:
#         print(n, "копеек")
# else:
#     print(n, "копеек")


# n = int(input("Введите число от 1 до 99: "))
# if 11 <= n <= 19:
#     print(n, "копеек")
# a = n % 10
# if a == 1:
#     print(n, "копейка")
# elif 2 <= a <= 4:
#     print(n, "копейки")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите число от 1 до 99: "))
#
# if 1 <= n <= 19:
#     print(n, "копеек")
#     a = n % 10
#     if a == 1:
#         print(a, "копейка")
# elif 2 <= n <= 4:
#     print(n, "копейки")
# else:
#     print(n, "копеек")
#

# cop = int(input("Введите число от 1 до 99: "))
# if 11 <= cop <= 14:
#     print(cop, "копеек")
# else:
#     ost = cop % 10
#     if ost == 1:
#         print(cop, "копейка")
#     elif 2 <= ost <= 4:
#         print(cop, "копейки")
#     else:
#         print(cop, "копеек")


# cop = int(input("Введите число от 1 до 99: "))
# if 11 <= cop <= 14:
#     print(cop, "копеек")
# else:
#     ost = cop % 10
#     if ost == 1:
#         print(cop, "копейка")
#     elif 2 <= ost <= 4:
#         print(cop, "копейки")
#     else:
#         print(cop, "копеек")

# cop = int(input("Введите число от 1 до 99: "))
# if 1 <= cop <= 99:
#     print(end="")
#     if 11 <= cop <= 14:
#         print(cop, "копеек")
#     else:
#         ost = cop % 10
#         if ost == 1:
#             print(cop, "копейка")
#         elif 2 <= ost <= 4:
#             print(cop, "копейки")
#         else:
#             print(cop, "копеек")
# else:
#     print("Ошибка ввода данных")


# Тернарное выражение>>>>>>>>>>>>>>>>>>>>>>>>

# a, b = (30, 20)
# print(a if a < b else b)

# a, b = 30, 30
# print("a == b" if a == b else "a > b" if a > b else "a < b")

# Исключение>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# a = 0
# b = "2.2"
# print(a + int(b))


# n = (input("Введите первое число"))
# m = (input("Введите второе число"))
# try:
#     print(int(n) + int(m))
# except ValueError:
#     print(n + m)

# Циклы while
#
# i = 0 # переменная счетчик
# while i < 5: # условие
#     print("i =", i)
#     i += 1 # изменения счетчика

# Итерация - один шаг цикла


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 2
# while i <= 20:
#     print("i =", i)
#     i += 2

# n = int(input("Введите количество символов: "))
# print("$" * n)

# n = int(input("Введите количество символов: "))
# print("$" * n)
#
# i = 0
# while i < n:
#     print("*",  end="")
#     i += 1

#
# a = int(input("Введите начало диапазона "))
# b = int(input("Введите конец диапазона "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a
#     a += 1
# print("Сумма целых ", res)

# n = (input("Введите цело число "))

# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("число не целое")
#         n = (input("Введите цело число "))
# if n % 2 == 0:
#     print("четное")
# else:
#     print("не четное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\n Цикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1
#
# while True:
#     n = int(input("Введите положительное число "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число "))
#     if n == 0:
#         break
#     res *= n
# print("Результат ", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл околнчен, i =", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\t Внутрений цикл j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while  i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while  i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#            print("+",  end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

#
# a = int(input("Количество символов: "))
# b = input("Тип символа: ")
# n = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
# i = 0
# while i < a:
#     if n == 0:
#         print(b, end=" ")
#     elif n == 1:
#         print(b)
#     else:
#         print("Данные ввода не корректны")
#         break
#     i += 1

# w = int(input("Введите ширину прямоугольника"))
# h = int(input("Введите высоту прямоугольника"))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# st = [i * 1 for i in "Hello"]
# print(st)
#
# s = []
# print(s, type(s))
#
# s2 = list("Hello")
# print(s2, type(s2))

# s1 = [1, 2, 3]
# s2 = [4, 5, 6]
# s3 = s1 + s2
# print(s3)
# print(s3 * 2)
#

# n = list(range(10))
# print(n)

# a = [0 for i in range(5)]
# print(a)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите количество элементов списка: ")))]
# print(a)

# lst = [5, 9, 8, 2, 3]
#
# for i in range(len(lst)):
#     print(lst[i], end=" ")
#
# print()
#
# for g in lst:
#     print(g, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
#
# print("Сумма отрицательных элементов", s)

# n = list(range(21, 41))
# print(n)
# for i in

# lst = [3, 7, 4, 6, 2]
# print(lst[::-1])
# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[6:])
# print(lst[3:4])
# print(lst[4:7])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# st = "HelloWorld"
# print(st[1:5])
# print(st[2:5])

# lst = []
# n = int(input("Введите количество элементов "))
# for i in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     lst.insert(0, x)
# print(lst)


# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 7, 3, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 7, 3, 2]
# c = []
#
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)
#

# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print(random.choice(city))
# print(random.choice(s))

# w = 12
# h = 4
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# for i in range():
#     print(i)


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = a
# for i in range(len(a)):
#     if a[i] == 0:
#         s
# print("Среднее арифметическое: ", a)


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)

# lst = [5, 9, 5, 4]
# for i in range(len(lst)):
#     print(lst[i], end="  ")


# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         s +=  a[i]
#     elif a == 0:
# print("Среднее арифметическое: ", s)

#
# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = 0
# z = 0
# for i in a:
#     if i > 0:
#         s += i
#         z += 1
#     if z > 0:
#         average = s / z
#         print("Среднее арифметическое: ", average)

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = 0
# z = 0
# for i in a:
#     if i != 0:
#         s += i
#         z += 1
# t = s / z
# print("Среднее арифметическое: ", t)
#

# a = [int(input("-> ")) for i in range(int(input("n: ")))]
# s = 0
# for i in a:
#     if i > 0:
#         s += i
#
#  print("Среднее арифметическое: ", s)

# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# print("Список: ", a)
# num = [i for i in a if i > 0]
# print("Новый список, состоящий из положительных элементов: ", num)
# print("Наибольший элемент списка: ", max(a))
#

# Модули:

# import math
#
# num1 = math.sqrt(2)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# import math as m
#
# num1 = m.sqrt(2)
# num2 = m.ceil(3.2)
# num3 = m.floor(3.8)
# print(num1)
# print(num2)
# print(num3)

#
# from math import sqrt, ceil, floor
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)

# from math import *
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)
#
# from math import pi
# # print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности: ", round(2 * pi * radius, 2))
#

# import time
# import locale
#
# print(time.ctime())
# print(time.localtime())
# res = time.localtime()
# print(res.tm_year)
# print(res.tm_year)
# print(time.strftime("%m/%d/%Y, %H:%M:%S.", time.localtime(2312312312)))
# print(time.strftime("Today is %B %d %Y."))
# locale.setlocale(locale.LC_ALL, "de")
# print(time.strftime("Сегодня %B %d %Y."))
#
# pause = 2.5
# print("Програма запущена: ", )
# time.sleep(pause)
# print(pause, "seconds")

# stat = time.time()
# time.sleep(5)
# finish = time.time() - stat
# print(finish)

# Function
# print()
#
#
# def hello(name, age):
#     print("Меня зовут", name, "Мне", age, "лет")
#
#
# hello("Irina", 20)
# hello(81, "Oleg")

# def get_sum(a, b):
#     print(a + b)
#
# x = 2
# y = 5
# get_sum(x, y)
#

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н
#
# def display_info(name, age):
#     print("Name:", name, "\nAge: ", age)
#
#
# display_info("Ira", 23)
# display_info("23", " Ira")
# display_info(age=23, name=" Ira")

# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)
#
# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# from math import pi

#
# a = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# b = int(input("Основание: "))
# c = int(input("Высота: "))
#
#
# def s(b, c):
#     return b * c / 2
#
#
# x = b
# y = c
#
# res = s(x, y)
# print("Площадь: ", res)
#

# def pl(yrov):
#     ...
#
#
# a = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# i == 0
# if pl(a):
#     a == 1

# a = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# b = int(input("Основание: "))
# c = int(input("Высота: "))
#
#
# def s(b, c):
#     return b * c / 2
#
#
# x = b
# y = c
#
# res = s(x, y)
# i = 0
# while i < a:
#     if a == 1:
#         print("Площадь: ", res)
#     elif a == 2:
#         print("Площадь: ",)
#     elif a == 3:
#         print("Площадь: ",)
#     else:
#         print("Данные ввода не корректны")
#         break
#     i += 1

# a = (input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# def primer(zadacha):
#     if len(zadacha) == 1:
#         return True
#     return False
#
#
# a = (input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# p = input("Основание: ")
# if primer(p):

#
# a = (input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# b = (input("Основание: "))
# c = (input("Высота: "))


# def get_sum(b, c):
#     b * c / 2
#
#
# a = (input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
# b = (input("Основание: "))
# c = (input("Высота: "))
#
#
# print("Площадь: ", )


# def calculate_area():
#     choice = int(input("1- прямоугольник, 2 - треугольник, 3 - круг: "))
#
#     if choice == 1:
#         length = float(input("Длина: "))
#         width = float(input("Ширина: "))
#         area = length * width
#         print("Площадь", area)
#     elif choice == 2:
#         base = float(input("Основание: "))
#         height = float(input("Высота: "))
#         area = 0.5 * base * height
#         print("Площадь", area)
#     elif choice == 3:
#         radius = float(input("Радиус: "))
#         area = math.pi * radius ** 2
#         print("Площадь", area)
#     else:
#         print("Неверный выбор")
#
#
# calculate_area()


# choice = int(input("1- прямоугольник, 2 - треугольник, 3 - круг: "))
#
#
# def figur_rectangle():
#     if choice == 1:
#         length = input("Длина: ")
#         width = input("Ширина: ")
#         area = length * width
#         print("Площадь", area)
#
#
# def figur_dsd():
#     if choice == 2:
#         length = input("Длина: ")
#         width = input("Ширина: ")
#         area = length * width
#         print("Площадь", area)
#
#
# def figur_asd():
#     if choice == 3:
#         length = input("Длина: ")
#         width = input("Ширина: ")
#         area = length * width
#         print("Площадь", area)

#
# choice = int(input("1- прямоугольник, 2 - треугольник, 3 - круг: "))
#
#
# def figur_rectangle():
#     if choice == 1:
#         length = input("Длина: ")
#         width = input("Ширина: ")
#         area = length * width
#         print("Площадь", area)
#
#
# figur_rectangle()
# from math import pi
# figura = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
#
#
# def rectangle(length, width):
#     if figura == 1:
#         a = int(input("Длина: "))
#         b = int(input("Ширина: "))
#         res = a * b
#         print("Площадь", res)
#
#
# def triangle():
#     if figura == 2:
#         base = int(input("Основание: "))
#         height = int(input("Высота: "))
#         ras = 0.5 * base * height
#         print("Площадь", ras)
#
#
# def a_circle():
#     if figura == 3:
#         radius = int(input("Радиус: "))
#         ras = round(pi * radius ** 2, 2)
#         print("Площадь", ras)
#
#
# rectangle()
# triangle()
# a_circle()
#


#
# def get_sum(a, b):
#     print("Площадь:", a * b)
#
#
# a = 10
# b = 16
#
#
# get_sum(2, 4)
#

# from math import pi
#
#
# def rectangle():
#     length = float(input("Длина: "))
#     width = float(input("Ширина: "))
#     area = length * width
#     print("Площадь:", area)
#
#
# def triangle():
#     base = float(input("Основание: "))
#     height = float(input("Высота: "))
#     area = 0.5 * base * height
#     print("Площадь:", area)
#
#
# def circle():
#     radius = float(input("Радиус: "))
#     area = round(pi * radius ** 2, 2)
#     print("Площадь:", area)
#
#
# figura = (input("1 - прямоугольник, 2 - треугольник, 3 - круг: "))
#
# if figura == '1':
#     rectangle()
# elif figura == '2':
#     triangle()
# elif figura == '3':
#     circle()
# else:
# from random import randint
# #     print("Ошибка ввода")fro
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0=: ", tpl3.count(0))
#
# point = (0, 0)
#
#
# match point:
#     case (0, 0)
#         print()

# t = (10, 11, [1, 2, 3], [4, 5, 6], ["hello", "world"])
# print(t)

# s = {"one", "two", "tre"}
# s.add("flor")
# print(s)
# # s.remove("flor")
# # print(s)
#
# el = "two"
# if el in s:
#     s.remove(el)
# print(s)
# s.discard("five")
# print(s)
#
# print()
#
# s.pop()
# print(s)


# s = {"one", "two", "three"}
# for i in s:
#     print(i, end=" ")

# print()
#
# s = {input("-> ") for x in range(10)}
# print(s)

# s = {"one", "two", "three"}
# print("two" in s)

# lst = ["ab_1", "ab_2", "bc_1", "bc_2"]
# print([i for i in lst if "a" in i])
# # print(tuple(i for i in lst if "a" in i))
# # print({i for i in lst if "a" in i})
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])

# s = {"one", "two", "three"}
# s.add("four") # Добавляет элемент в множество
# print(s)
# s.remove("four")
# print(s)
# el = "two"
# if el in s:
#     s.remove(el)  # Удаляет элемент по значениям
# print(s)

# s.discard("five")
# print(s)
# el = s.pop()
# print(s)
# print(el)
# # s.clear()
# # print(s)

# Python
# Programming language
#
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# print("Искомые буквы являются: ", )


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# a |= b
# print(a)

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# c = a - b
# for i in c:
#     print("Искомые буквы являются: ", i, end=" ")
#
#

# print("Искомые буквы являются: ", c)


# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a & b
# print(c)

# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# c = a - b
#
# print("Искомые буквы являются: ")
# for gg in c:
#     print(gg, end=" ")

#
# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# q = int(input("Какой элемент исключить: "))
# del d[q]
# print(d)
#
# goods = {
#     "1": ["Core-i3-4330", 9, 4500],
#     "2": ["Core-i5-4570K", 3, 8500],
#     "3": ["Core-i3-FX-6300", 4, 3700],
#     "4": ["AMD-i5-FX-6300", 4, 3700],
#     "5": ["Core-i5-3450", 6, 6400],
# }
# for i in goods:
#
# region = {
#     "John": ["N :", 3056, "S", 8463, "E :", 8441, "W :", 2694],
#     "Tom": ["N : 4832", "S : 6786", "E : 4737", "W : 3612"],
#     "Anne": ["N : 5239", "S : 4802", "E : 5820", "W : 1859"],
#     "Fiona": ["N : 3904", "S : 3645", "E : 8821", "W : 2451"],
# }
#

#
# region = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# for i in region:
#     print(i, '\n',  "N :", region[i]["N"], '\n',  "S :", region[i]["S"], '\n',  "E :", region[i]["E"], '\n', "W :",
#           region[i]["W"], )
# # print(region["John"]["W"])
# name = input("Имя: ")
# reg = input("Регион: ")
# print(region[name][reg])
# nev_z = (input("Новое значение: "))
# region[name][reg] = nev_z
# print(region[name])

# print(region["John"]["N :"])

#
# r = {"John": {"N :": 3056}}
# print(r["John"]["N :"])


# a = input("Имя: ")
# b = int(input("Регион: "))
# region[a][1] = b
# while True:
#     a = input("Имя: ")
#     if a != "0":
#         b = int(input("Регион: "))
#         region[a][1] = b
#     else:
#         break
# for i in region:


# a = ["Декабрь", "Январь", "Февраль", "Март"]
# b = [12, 1, 2, 3]
# c = [1.0, 2.0, 3.0]
# print(dict(zip(a, b)))
# print(list(zip(a, b, c)))
# print(tuple(zip(a, b, c)))
# print(list(zip(a)))
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(a)

# Области видимости (scope)
#
# name = "Tom"
#
#
# def hi():
#     name = "Same"
#     surname = "Jonson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()

# a = {int(input("1-й студент: ")) for i in range(int(input("Количество студентов: ")))}
# s = 0
# z = 0
# for i in a:
#     if i != 0:
#         s += i
#         z += 1
# t = s / z
# print("Среднее арифметическое: ", t)


# Ввод количества студентов
# n = int(input("Введите количество студентов: "))
#
# students = []
#
# # Ввод данных для каждого студента
# for i in range(n):
#     surname = input(f"Введите фамилию студента {i + 1}: ")
#     score = float(input(f"Балл: {i + 1}: "))
#
#     students.append({
#         'surname': surname,
#         'score': score
#     })
#
#
#
#     if i != 0:
#         gf = input("-й студент: ")
#
#         zdas = float(input("Балл: "))
#
#
# print(gf, s)


#
# n = int(input("Введите количество студентов: "))
# students = {}
# for i in range(1, n + 1):
#     name = input(str(i) + "-й студент: ")
#     bal = int(input("Балл: "))
#     students[name] = bal
# print(students)
# sr_bal = sum(students.values()) / n
# res = [name for name, bal in students.items() if bal > sr_bal]
# print("\nСредний балл: " + str(round(sr_bal)), "." " Студенты с балом выше среднего:", sep="")
# for name in res:
#     print(name)
#
#


# n = int(input("Введите количество студентов: "))
# students = {}
# for i in range(1, n + 1):
#     name = input(str(i) + "-й студент: ")
#     bal = int(input("Балл: "))
#     students[name] = bal
# print(students)
# sr_bal = sum(students.values()) / n
# res = []
# for name, bal in students.items():
#     if bal > sr_bal:
#         res.append(name)
#         print("\nСредний балл: " + str(round(sr_bal)), "." " Студенты с балом выше среднего:", sep="")
# for name in res:
#     print(name)


# s = 0
#
# z = [(2, 4, 6), (5, 8, 2), (1, 6, 8)]
#
#
# def glob(a, b, c):
#     def rectangle(x, y):
#         return x * y
#     global s
#     s = 2 * (rectangle(a, b) + rectangle(a, c) + rectangle(b, c))
#     return s
#
#
# print("Глобальная переменная:")
# for a, b, c in z:
#     print(glob(a, b, c))
#
#
# def _local(a, b, c):
#     def rectangle(x, y):
#         return x * y
#
#     ar = 2 * (rectangle(a, b) + rectangle(a, c) + rectangle(b, c))
#     return ar
#
#
# print("Локальная переменная:")
# for a, b, c in z:
#     print(_local(a, b, c))
#
#
# def _nonlocal(a, b, c):
#     ar = 0
#
#     def rectangle(x, y):
#         nonlocal ar
#         ar += 2 * x * y
#     rectangle(a, b)
#     rectangle(a, c)
#     rectangle(b, c)
#
#     return ar
#
#
# print("Нелокальная переменная:")
# for a, b, c in z:
#     print(_nonlocal(a, b, c))

# b = [66, 99, 68, 59, 76, 60, 88, 74, 81, 68]
# # res = list(filter(lambda s: s > 75, b))
# res = list(filter(lambda s: s > sum(b) / len(b), b))
# print(res)


# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print(list(range(1, 10)))
#
#


# def outer(n):
#     return lambda sd: n + sd
#
#
# f = outer(5)
# print(f(10))
#
#
# print((lambda n: lambda x: n + x)(5)(10))

# def sef():
#     return n
#
#
# n = [2, 3, 3, 4]
# for n in n:
#     print("сумма чисел", n, "=", sum(n))

# s = [2, 3, 3, 4]
#
#
# def cnt(fn):
#     def wrap():
#         fn()
#         print("Средне арифметическое:", s, "=", sum(s) / len(s))
#
#     return wrap
#
#
# @cnt
# def n():
#     print("Сумма чисел:", s, "=", sum(s))
#
#
# n()

# s = [2, 3, 3, 4]
#
#
# def cnt(fn):
#     def wrap():
#         fn()
#         print("Средне арифметическое:", ", ".join(map(str, s)), "=", sum(s) / len(s))
#     return wrap
#
#
# @cnt
# def n():
#     print("Сумма чисел:", ", ".join(map(str, s)), "=", sum(s))
#
#
# n()
#
#


# def outer(fn):
#     def wrap(*args):
#         fn(*args)
#
#     return wrap()
#
# def
# def average_decorator(func):
#     def wrapper(*args):
#         result = func(*args)
#         average = result / len(args)
#         print(f"Среднее арифметическое чисел {args} = {average}")
#
#         return result
#     return wrapper
#
#
# @average_decorator
# def sum_numbers(*args):
#     result = sum(args)
#     print(f"Сумма чисел {args} = {result}")
#     return result
#
#
# sum_numbers(2, 3, 3, 4)
#
# def cnt(fn):
#     def wrap(*args):
#         s = fn(*args)
#         v = s / len(args)
#         print(f"Среднее арифметическое чисел {args} = {v}")
#         return wrap()
#
# def sum_ch(*args):
#
# def decor(args1):
#     def cnt(fn):
#         def wrap(*args2):
#             print(args1, args2, "=", end=" ")
#             fn(args2)
#
#         return wrap
#     return cnt
#
#
# @decor("Сумма числил:")
# def summa(args2):
#     print(sum(args2))
#
#
# @decor("Среднее арифметическое чисел:")
# def _ar(args2):
#     print(sum(args2) / len(args2))
#
#
# summa(2, 3, 3, 4)
#
#
# _ar(2, 3, 3, 4)


# def decor(args1):
#     def cnt(fn):
#         def wrap(*args2):
#             # print("Средне арифметическое:", ", ".join(map(str, s)), "=", sum(s) / len(s))
#             print(args1,  ", ".join(map(str, args2)), "=", end=" ")
#             fn(args2)
#
#         return wrap
#     return cnt
#
#
# @decor("Сумма числил:")
# def summa(args2):
#     print(sum(args2))
#
#
# @decor("Среднее арифметическое чисел:")
# def _ar(args2):
#     print(sum(args2) / len(args2))
#
#
# summa(2, 3, 3, 4)
#

# _ar(2, 3, 3, 4)
#

# text = "Замените в этой строке все появления буквы \"о\" на букву \"О\", кроме первого и последнего вхождения."
# s = text.count('о')
# print(text.replace("о", "О", s - 1).replace("О", "о", 1))
#


# print(text.find("о"))
# print(text.rfind("о"))


# print(text.find("о", 14, 15))
# print(text.index("о", 14))


# print(text.lower())
# print(text.upper())

#
# text = "Замените в этой строке все появления буквы \"о\" на букву \"О\", кроме первого и последнего вхождения."
# s = text.count('о')
# _res = text.replace('о', 'О', s - 1).replace('О', 'о',  1)
# print(_res)
#
#
#
#
# print("Вносим изменение в локальный репозиторий")
import re

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счета. [6789]. H.ello_World."
# # reg = r"6[0-9][0-9][0-9]"
# reg = r"20*"
# print(re.findall(reg, s))
#

# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения", re.sub(r"\s#.*", "", d))
# print("Дата рождения", re.sub(r"-", ".", d))
# print("Дата рождения", re.sub(r"-", ".", re.sub(r"\s#.*", "", d)))

# st = "author=Пушкин А.С.; title = Евгений Онегин; price = 200; year= 1831"
# # reg1 = r"\w+\s*=\s*\w+[\s\w.]*"
# reg1 = r"\w+\s*=[^;]+"
# print(re.findall(reg1, st))
# print(re.split(r";\s+", st))

# s1 = "12 сентября 2025 года"
# # reg1 = r"\d{4}"
# # reg1 = r"\d{2,4}"
# reg1 = r"6[0-9][А-я]"
# print(re.findall(reg1, s1))

# st = "+7 499 456-45-78, +74994564578, +7(499) 456 45 78, 74994564578"
# reg1 = r"\+?7\d{10}"
# print(re.findall(reg1, st))
# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счета. [6789]. H.ello_World."
#
# reg = r"\w+\.$"
#
# # print(re.findall(reg, s))

#
# def validate_password(password):
#     return re.findall(r"^[A-Za-z0-9@_-]{6,18}$", password)
#
#
# print(validate_password("ma-p@sswOrd"))

#
# s = "5 + 7*2 - 4"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, s))
#
# a = "31-11-2021"
# pattern = r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-1]|20[0-9][0-9])"
# print(re.findall(pattern, a))

# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
#
# print(re.sub(reg, r"\2.\1.\3", s))

# Рекурсия:

# def elevatr(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print("=>", n)
#     elevatr(n - 1)
#     print(n, end=" ")
#
# n1 = 5
# elevatr(n1)


#
# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
# def sum_list(lst):  #[1, 3, 5, 7, 9]
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
#
# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_item(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))

# ДЗЗЗЗЗЗЗ

# def gret(n):
#     if n < 0:
#         print("n =")
#         return
#     print("=>", n)
#     gret(n - 1)
#     print(n, end=" ")
#
#
# s = 3, 4, 3, -2, 3
# gret(s)

#
# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле\nИзменить сторонку в списке;\nЗаписать список в файл;\n")
# f.close()
#
# f = open("text2.txt", "r")
# read_file = f.readline()
# print(read_file)
# read_file[1] = "Hello World\n"
# print(read_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_file)
# f.close()

# f = open("test.txt")
# print(f.read(3))
# print(f.tell())  # Возвращает позицию условного курсора в файл
# print(f.seek(1))  # Перемещает условный курсор в заданную позицию
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text.txt", "r+")
# print(f.write("I am learning Paython"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()
# with open("test.txt", "w+") as f:
#     print(f.write("0123456789"))
# print(f.closed)
#
# lst = [4.5, 2.8, 3.9, 1.0, 1.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open("res.txt", 'w') as f:
#     f.write(str(lst))
#
# print("Файл создан")
#


# print(os.getcwd())
# print(os.listdir())
# print(os.listdir("folder"))
# os.makedirs("nested1/nested2/nested3")
# os.remove("text2.txt")
# os.rename("res.txt", "res2")
# os.rename("res2",

# for root, dirs, files in os.walk("nested1", topdown=False):
#     print("Root", root)
#     print("\tDirs", dirs)
#     print("\tfiles", files)
# import os

# dirs = [r"Work\F1", r"Work\F2\F21"]
# for d in dirs:
#     os.makedirs(d)
# Work\w.txt
# Work\F1\f11.txt
# Work\F1\f12.txt
# Work\F1\f13.txt
# Work\F2\F21\f211.txt
# Work\F2\F21\f212.txt

# files = {
#     "Work": ["w.txt"],
#     r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
#     r"Work\F2\F21": ["f211.txt", "f212.txt"]
# }
#
# for d, f in files.items():
#     for file in f:
#         file_path = os.path.join(d, file)
#         open(file_path, "w").close()
#
#
# files_with_text = [r"Work\w.txt", r"Work\F1\f12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt"]
#
# for file in files_with_text:
#     with open(file, "w") as f:
#         f.write(f"Какой-то текст в файле {file}")


# def gret(n):
#     if n == 0:
#         print("n =")
#         return
#     print("=>", n)
#     gret(n < 0)
#     print(n, end=" ")
#
#
# s = [3, 4, 3, -2, 3]
# gret(s)


# def gret(n):
#     a = 0
#     for i in n:
#         if i < 0:
#             a += 1
#     return a

#
# def gret(n):
#     if n > 0:
#         return n
#     else:
#         return gret(n[1:])
#
#
#
# def gret(n):
#     if not n:
#         return 0
#     if n[0] < 0:
#         return 1 + gret(n[1:])
#     else:
#         return gret(n[1:])
#
#
# print("n =", gret([-2, 3, 8, -11, -4, 6]))

# Файлы

# f = open("text.txt")
# print(f)
# print(*f)
# f.close()
# print(f.closed)

# f = open("text.txt", "r")
# print(f.read())
# f.close()

# f = open("text1.txt", "w")
# f.write("This is line1\nThis is line2\nThis is line3\n")
#
# f.close()

# f = open("text1.txt", "r")
# print(f.readline())
# print(f.readline())
# f.close()

# f = open("xyz.txt", "w")
# f.write("Hello\nWorld")
# f.close()
#
# f = open("xyz.txt", "a")
# f.write("\nNew text")
# f.close()

# f = open("xyz.txt", "w")
# lst = [str(i) for i in range(10, 1000, 10)]
# print(lst)
# for ind in lst:
#     f.write(ind + '\t')
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл")
# f.close()
# f = open("text2.txt", "r")
# red_file = f.readlines()
# print(red_file)
# red_file[1] = "Hello World\n"
# print(red_file)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(red_file)
# f.close()


# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# print("Тест:\n""Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
# z = int(input("pos1 = "))
# y = int(input("pos2 = "))
# f.close()
# f = open("text2.txt", "r")
# red_file = f.readlines()
# # print(red_file)
# if z < 0 or y < 0 or z >= len(red_file) or y >= len(red_file):
#     print("Не корректный ввод")
# else:
#     red_file[z], red_file[y] = red_file[y], red_file[z]
#     zam_str = ''.join(red_file)
#     print(zam_str)
# f.close()
# f = open("text2.txt", "w")
# f.writelines(red_file)
# f.close()

# class Point:
#     x = 1
#     y = 2
#
#     def set_coords(self, x1, y1):
#         self.x = x1
#         self.y = y1
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 100
# # p1.y = 200
# p1.set_coords(100, 200)
# Point.set_coords(p1, 111, 222)
#
# # print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
#
# print(Point.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ". center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nАдрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birhday, phone, country, city, addrws):
#         self.name = first_name
#         self.birthday = birhday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = addrws
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1896", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Юлия")
# print(h1.get_name())
#
#

# class Person:
#     skill = 10
#
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("\nДанные сотрудника:", self.name, self.surname)
#
#     def add_slill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person()
# p1.print_info("Виктор", "Резник")
# p1.add_slill(3)
#
# p2 = Person()
# p2.print_info("Анна", "Долгих")
# p2.add_slill(2)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота:", self.name)
#         Robot.k += 1
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#     def __del__(self):
#         print(self.name, "выключается ")
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "Был последним")
#         else:
#             print("Работающих роботов осталось", Robot.k)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
#
# del droid1
# del droid2
#
# print("Численность роботов:", Robot.k)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Вызов _set_x")
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# print(p1.x)
#
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#         self.__kg = new_kg
#
#
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = 41
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = "десять"
# print(w.kg, "кг =>", w.to_pound(), "фунтов")

# cnt())

# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         mx = a
#         if b > mx:
#             mx = b
#         if c > mx:
#             mx = c
#         if d > mx:
#             mx = d
#         return mx
#
#
# print(Numbers.max(3, 5, 7, 9))

# class Point:
#     """"Класс для предоставления координатор точек на плоскостей"""
#     x = 1
#     y = 2
#
#     def set_coords(self, x1, y1):
#         self.x = x1
#         self.y = y1
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 100
# # p1.y = 200
# # print(p1.x, p1.y)
# p1.set_coords(100, 200)

# print(p1.__dict__)
#
# p2 = Point()
# print(p2.x, p2.y)
# print(p2.__dict__)
#
# print(Point.__doc__)
# ==============================================
# class Car:
#     model = "model"
#     year = "year"
#     creator = "creator"
#     power = "power"
#     colour = "colour"
#     price = "price"
#
#     def print_ifo(self):
#         print("Данные автомобиля".center(40, "*"))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.creator}\nМощность  "
#               f"двигателя: {self.power} л.с\nЦвет машины: {self.colour}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def input_info(self, model, year, creator, power, colour, price):
#         self.model = model
#         self.year = year
#         self.creator = creator
#         self.power = power
#         self.colour = colour
#         self.price = price
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#
# h1 = Car()
# h1.print_ifo()
# h1.input_info("X7 M50i", "2021", "BMV", "530", "white", "10790000")
# h1.print_ifo()
# h1.set_model("X6")
# h1.print_ifo()
# print(h1.get_model())

# ========================================================

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print("Инициализатор")
#
#     def __del__(self):
#         print("Финализатор (деструктор)")
#
#     def print_info(self):
#         print("\nДанные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill)
#
#
# p1 = Person("Виктор", "Резник")
# p1.print_info()
# p1.add_skill(3)
# # del p1
# p1 = 5
#
# p2 = Person("Анна", "Долгих")
# p2.print_info()
# p2.add_skill(2)
#
# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(1, 2)
# p2 = Point(10, 20)
# p3 = Point(100, 200)
# print(Point.count)
# print(p1.count)
# print(p2.count)
#
# # print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k += 1
#
#     def sya_hi(self):
#         print("Приветствую меня зовут: ", self.name)
#
#     def __del__(self):
#         print(self.name, "выключается")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось: ", Robot.k)
#
#
# droid1 = Robot('R2-D2')
# droid1.sya_hi()
# print("Численность роботов: ", Robot.k)
#
# droid2 = Robot('P5-CO')
# droid2.sya_hi()
# print("Численность роботов: ", Robot.k)
#
# droid3 = Robot('C3-PO')
# droid3.sya_hi()
# print("Численность роботов: ", Robot.k)
#
# print("\nЗдесь роботы могут делать какую-то работу\n")
#
# print("Роботы закончили свою работу давайте их выключим:")
#
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов: ", Robot.k)
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point. __check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p1.set_coord(1, "2.5")
# print(p1.get_coord())
#
# print(Point.__check_value(5))
# # p1.set_coord("abc", 2)
# print(p1.get_coord())
# p1.x = "abc"
# p1.x = "abc"
# p1.y = "qwe"
# print(p1.__dict__)
# print(p1.x, p1.y)

#
# class Pont:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         print("Вызов __set.x")
#         self.__x = x
#
#     def __get_x(self):
#         print("Вызов __get_x")
#         return self.__x
#
#     x = property( __get_x, __set_x)
#
#
# p1 = Pont(5, 10)
# print(p1.x)
# p1.x = 50
# print(p1.x)
#
# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются только числами")
#
#     def to_pound(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = 41
# print(w.kg, "кг =>", w.to_pound(), "фунтов")
# w.kg = "десять"
#
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name1):
#         if isinstance(name1, str):
#             self.__name = name1
#         else:
#             print("Не строка")
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age1):
#         if isinstance(age1, int):
#             self.__age = age1
#         else:
#             print("Не число")
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# person = Person("Irina", 26)
# print(person.__dict__)
# person.name = "Igor"
# print(person.__dict__)
# person.age = 23
# print(person.__dict__)
# del person.name
# print(person.__dict__)
#
#

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# # print(Point.__dict__)
# print(Point.get_count())
#
#

# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         return a, b, c, d
#
#
# print(max(Numbers.max(3, 5, 7, 9)))


# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#     @classmethod
#     def from_string(cls, sting_date):
#         day, month, year = map(int, sting_date.split("."))
#         date = Date(day, month, year)
#         return date
#
#
# date1 = Date.from_string("23.10.2025")
# print(date1.string_to_db())

# sting_date = "23.10.2025"
# day, month, year = map(int, sting_date.split("."))
# print(day, month, year)
# date = Date(day, month, year)
# print(date.string_to_db())
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащей {self.surname} был открыт")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащей {self.surname} был закрыт.")
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены!:")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} Было успешно добавлено")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец счета: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percent()
# print()
#
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#
#
#         self.verifu_weight(weight)
#         self.verify_ps(ps)
#
#         self.fio = fio
#
#         self.__password = ps
#         self.__weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(re.findall("[a-zа-яё-]", fio, re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквф и дифис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 70:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 70 лет")
#
#     @staticmethod
#     def verifu_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть стройкой")
#         s = ps.split()
#         if len(s) != 2 or len(s[0]) != 4:
#             raise TypeError("Неверный формат паспорта!")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, year):
#         self.verify_fio(year)
#         self.__old = year
#
#     @property
#     def password(self, ps):
#         return self.__password
#
#     @old.setter
#     def old(self, year):
#         self.verify_fio(year)
#         self.__old = year
#
#
# p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.2)
# p1.fio = "Соболев игорь Николаевич"
# print(p1.fio)
#

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line:
#
#     def draw_line(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_line(self) -> None:
#         print(f"Рисование прямоугольника : {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20), "yellow", 2)
# line.draw_line()
# rect = Rect(Point)
#
# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(sum_numbers(1, 2, 3))  # 6
# print(sum_numbers(10, 20))   # 30

#
# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Ширина должна быть больше 0")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Высота должна быть больше 0")
#
#     def area(self):
#         return self.__width * self.__height
#
#     def print_info(self):
#         print(f"Прямоугольник:\nШирина: {self.__width}\nВысота: {self.__height}\nЦвет: {self.color}\nПлощадь: "
#               f"{self.area()}")
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.__dict__)
# print(rect.area())
# rect.print_info()

# Перегрузка методов

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y=None):
#         if y is None:
#             self.x = x
#         else:
#             self.x = x
#             self.y = y
#
#
# p1 = Point(1, 2)
# print(p1.__dict__)
# p1.set_coord(10, 20)
# print(p1.__dict__)
# p1.set_coord(100)
# print(p1.__dict__)

# Абстаркктныек метолы и Абстрактные классы

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self) -> str:
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1) -> None:
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self) -> None:
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self) -> None:
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     def draw(self) -> None:
#         print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 20)))
# figs.append(Line(Point(10, 10), Point(20, 30)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(70, 70), Point(200, 200)))
#
# for f in figs:
#     f.draw()

# from abc import ABC, abstractmethod
#
# #
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         pass
#
#
# class Queen(Chess):
#     def move(self):
#         print("Ферзь перемещен на е2е4")
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()
# #
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if length is None:
#             self.width = self.length = width
#         if radius is None:
#                if length is None
#             self.width = width
#             self.length = length
#
#         else:
#             self.radius = radius
#
#     def clas_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод clas_area()")
#
#
# class SquareTable(Table):
#     def clas_area(self):
#         return self.width * self.length
#
#
# class RoundTable(Table):
#     def clas_area(self):
#         return round(pi * self.radius ** 2, 2)
#
#
# t = SquareTable(20, 10)
# print(t.__dict__)
# print(t.clas_area())
#
# t2 = SquareTable(20)
# print(t2.__dict__)
# print(t2.clas_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.clas_area())
#
# class A:
#     def __init__(self):
#         print("init A")
#
#
# class B(A):
#     def __init__(self):
#         print("init B")
#
#
# class C(A):
#     def __init__(self):
#         print("initC")
#
#
#
# class D(B, C):
#     def __init__(self):
#         print("init A")
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)
#
#
# class AA:
#     def __init__(self):
#         print("init A")
#
#
# class B(A):
#     def __init__(self):
#         print("init B")
#
#
# class C(AA):
#     def __init__(self):
#         print("initC")
#
#
#
# class D(B, C):
#     def __init__(self):
#         print("init A")
#
#
# d = D()
# print(D.mro())
# # print(D.__mro__)
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"{self.x}, {self.y}"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Init Styles")
#         self.color = color
#         self.width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Init Pos")
#         self.sp = sp
#         self.ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self.sp} {self.ep} {self.color} {self.width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
#
# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)  # Clock(300)
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         if item == "hour":
#             return (self.sec // 3600) % 24
#
#         if item == "min":
#             return (self.sec // 60) % 60
#
#         if item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour"
#             self.sec = s + 60 * m + value * 3600
#
# c1 = Clock(80000)
# print(c1.get_format_time())
# #
# # print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 14
# print(c1["hour", c1["min"], c1])
#
# # c2 = Clock(200)
# c4 = Clock(300)
# c3 = c1 + c2 + c4
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())
# from random
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return Cat("No name", 0, ["M", "F"])
#         else:
#             raise TypeError("Types are not support!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)
#
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimetr(self):
#         return 2 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimetr())
#
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def get_perimetr(self):
#         pass
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def get_perimetr(self):
#         return self.side * 4
#
#     def get_area(self):
#         return self.side * self.side
#
#     def draw(self):
#         return ("*  " * self.side + "\n") * self.side
#
#     def info(self):
#         print(f"=== Квадрат ===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь:{self.get_area()}\nПериметр:"
#               f"{self.get_perimetr()}\n{self.draw()}\n")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#
# def get_perimetr(self):
#     return self.side * 4
#
#
# def get_area(self):
#     return self.side * self.side
#
#
# def draw(self):
#     return ("*  " * self.side + "\n") * self.side
#
#
# def info(self):
#     print(f"=== Прямоугольник ===\nДлина: {self.lenght}\n Ширина: {self.widthmmmmmmmm}Цвет: {self.color}\nПлощадь"
#           f":{self.get_area()}\nПериметр:"
#           f"{self.get_perimetr()}\n{self.draw()}\n")
#
#
# sq = Square(3, "red")
# sq.info()

# Перегрузка операторов:
# Число секунд в одном дне: 24 * 60 * 60 =86400

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом!")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типам данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типам данных Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# # c1 += c2
# # # c4 = Clock(300)
# # # c3 = c1 + c2 + c4
# # print(c1.get_format_time())
# # print(c2.get_format_time())
# # print(c4.get_format_time())
# # print(c3.get_format_time())
# # if c1 == c2:
# #     print("Время одинаковое")
# # else:
# #     print("Время разное")
# if c1 != c2:
#     print("Время разное")
# else:
#     print("Время одинаковое")

############################################

# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             return IndexError("Неверный индекс ")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть положительным числом")
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)
#             self.marks.extend([None] * off)
#         self.marks[key] = value
#
#
# s1 = Student("Сергей", 5, 5, 3, 4, 5)
# # print(s1.marks[2])
# print(s1[2])
# s1[10] = 4
#
# print(s1.marks)
# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         elif self.pol == "F":
#             return f"{self.name} is good girl!!!"
#
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name'{self.name}', age={self.age}, pol={self.pol})"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(1, randint(2, 6))]
#
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Elsa", 5, "F")
# # cat3 = Cat("Murzik", 3, "M")
# print(cat1)
# print(cat2)
# # print(cat3)
# print(cat1 + cat2)

# Полиморфизм
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())
#
# from abc import ABC, abstractmethod
# import math
#
#
# class Shape(ABC):
#     def __init__(self, color):
#         self.color = color
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def draw(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class Square(Shape):
#
#     def __init__(self, side, color):
#         super().__init__(color)
#         self.side = side
#
#     def get_perimeter(self):
#         return self.side * 4
#
#     def get_area(self):
#         return self.side * self.side
#
#     def draw(self):
#         return ("*  " * self.side + "\n") * self.side
#
#     def info(self):
#         print(f"===Квадрат===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь {self.get_area()}\nПериметра: "
#               f"{self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width, color):
#         super().__init__(color)
#         self.length = length
#         self.width = width
#
#     def get_perimeter(self):
#         return (self.length + self.width) * 2
#
#     def get_area(self):
#         return self.length + self.width
#
#     def draw(self):
#         return ("*  " * self.width + "\n") * self.length
#
#     def info(self):
#         print(f"===Прямоугольник===\nДлина: {self.length}\nЩирина: {self.width}\nЦвет: {self.color}\nПлощадь"
#               f" {self.get_area()}\nПериметра: "f"{self.get_perimeter()}\n{self.draw()}\n")
#
#
# class Triangle(Shape):
#     def __init__(self, side1, side2, side3, color):
#         super().__init__(color)
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#
#     def get_perimeter(self):
#         return self.side1 + self.side2 + self.side3
#
#     def get_area(self):
#         p = self.get_perimeter() / 2
#         return round(math.sqrt(p * (p * self.side1) * (p - self.side2) * (p - self.side3)), 2)
#
#     def draw(self):
#         rows = []
#         for n in range(self.side2):
#             rows.append(" " * n + "*" * (self.side1 - 2 * n))
#         rows.reverse()
#         return "\n".join(rows)
#
#     def info(self):
#         print(f"===Треугольник===\nСторона1: {self.side1}\nСторона2: {self.side2}\nСторона3: {self.side3}\nЦвет:"
#               f" {self.color}\nПлощадь"f" {self.get_area()}\nПериметра: "f"{self.get_perimeter()}\n{self.draw()}\n")
#
#
# # sq = Square(3, "red")
# # sq.info()
#
# # rect = Rectangle(3, 7, "green")
# # rect.info()
#
# tr = Triangle(11, 6, 6, "yellow")
# tr.info()
#
# def string_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return string.strip(chars)
#
#     return wrap
#
#
# s1 = string_string("?:!.: ")
# print(s1(" !!! ? :Hello World! "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError("Аргумент должен быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StringStrip("?:!.: ")
# print(s1(" !!! ? :Hello World! "))

# a = 5
# print(type(a))
# class MyList(list):
#     def get_length(self):
#         return len(self)
# get_lengthMyList = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
# lst = MyList()
# lst.append(5)
# lst.append(7)
# print(lst, lst.get_length())

# import geometry.rect
# import geometry.sq
# # import geometry.trian
#
# from geometry import rect, sq, trian
# # from geometry import *
#
# if __name__ == "__main__":
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.perimeter())

# import json
#
# data = {
#     'name': 'Oleg',
#     'age': 35,
#     20: None,
#     True: 1,
#     'hobbies': ('running', 'singing'),
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 6
#         }
#
#     ],
#     None: "Кортеж"
#
# }
#
# with open("data_file.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
#
# with open("data_file.json", "r", encoding="utf-8") as f:
#     data1 = json.load(f)
#
# print(data1)
#
# json_string = json.dumps(data, ensure_ascii=False)
# print(json_string)
#
# res = json.loads(json_string)
# print(res, type(res))
#
# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'c', 'd', 'd', 'f', 'g', 'h', 'e', 'k', 'l', 'm', 'n']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(num)
#     print(tel)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         # st = ''
#         # for i in self.marks:
#         #     st += str(i) + ", "
#         #
#         # st = ", ".join(map(str, self.marks))
#         # return f'Студент: {self.name}: {st}'
#         return f'Студент: {self.name}: {", ".join(map(str, self.marks))}'
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edir_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def average_marks(self):
#         return sum(self.marks) / len(self.marks)
#
#     def get_file_name(self):
#         return self.name + ".json"
#
#     def dump_to_json(self):
#         data = {"name": self.name, 'marks': self.marks}
#         with open(self.get_file_name(), "w") as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         with open(self.get_file_name(), "r") as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         # st = ""
#         # for i in self.students:
#         st = "\n".join(map(str, self.students))
#         return f"Группа: {self.group}\n {st}"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         self.students.pop(index)
#
#
# st1 = Student("Bodnya", [5, 4, 3, 4, 5, 3])
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# # print(st1)
# # print(st2)
# sts1 = [st1, st2]
# grop1 = Group(sts1, "ГК Python")
# print(grop1)
# print()
# grop1.add_student(st3)
# print(grop1)
# print()
# grop1.remove_student(1)
# print(grop1)
# Козовякина Елена
#
#
#
# sts2 = [st2]
# grop2 = Group(st2, "ГК Web")
# print(grop2)

# st1.add_marks(5)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edir_mark(4, 4)
# print(st1)
# print(st1.average_marks())
# st1.dump_to_json()
# st1.load_from_file()
# st2.dump_to_json()
# st2.load_from_file()


# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#         @staticmethod
#         def load_from_file(file_name):
#             with open(file_name) as f:
#                 print({ for k, v in json.load(f).items()})
#
#                 file = "List_capital.json"
#                 while True:
#                     index = input(
#                         "Выбор действия:\n1- добавление данных\n2- удаление данных\n3- поиск данных\n4-
#                         редактирование "
#                         "данных\n5- просмотр данных\n6- завершение работы\nВвод")
#                     if index == "1":
#                         CountryCapital.add_country(file)
#                     elif index == "5":
#                         CountryCapital.load_from_file(file)
#                     elif index == "6":
#                         break
#                     else:
#                         print("Введен некорректный номер")

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def perimeter(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def perimeter(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
#
# s1 = Square(10)
# s2 = Square(20)
#
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.perimeter())
#
# from nevcar import ca, eleccar
#
# electric_car = ca.Electro("Tesla", "T", 2018, 99000)
# print(electric_car.print_info())
# from nevcar.ca import Car, ElectricCar
# from nevcar import *
#
#
# electric_car = eleccar.Electro("Tesla", "T", 2018, 99000)
# print(electric_car.print_info())

# from nevcar.el import Electro
#
#
# def run():
#     electric_car = Electro("Tesla", "T", 2018, 99000, 100)
#     print(electric_car.print_info())

# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ".lower())
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         if del_country in data:
#             del data[del_country]
#             with open(file_name, "w") as f:
#                 json.dump(data, f)
#
#         else:
#             print("Такой страны в базе дынных нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ".lower())
#
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#
#         if country in data:
#             print(f"Страна {country.capitalize()} столица {data[country].capitalizq()} есть в словаре")
#
#         else:
#             print(f"Страны {country.capitalize()} нет в словаре")
#
#
# file = "List_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - редактирование "
#                   "данных\n5 - просмотр данных\n6 - завершение работы\nВвод:")
#     if index == "1":
#         CountryCapital.add_country(file)
#     if index == "2":
#         CountryCapital.delete_country(file)
#
#     if index == "3":
#         CountryCapital.search_data(file)
#
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#
#     elif index == "6":
#         break
#     else:
#         print("Введен не корректный номер")

#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# print(top_users)
#
# max_complete = top_users[0][1]
# print(max_complete)
#
# users = []
#
# for user, num_complete in top_users:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# print(users)
#
# max_users = " and ".join(users)
# print(max_users)
# print(f"users {max_users} completed {max_complete} Todos")
#
#
# def keep(todo1):
#     is_complete = todo1["completed"]
#     has_max_count = str(todo1["userId"]) in users
#     return is_complete and has_max_count
#
#
# with open("filtered_data.json", "w") as f:
#     filtered_todos = list(filter(keep, todos))
#     json.dump(filtered_todos, f, indent=2)
#
#
# with open("filtered_data.json", "r") as f:
#     print(json.load(f))
#
#

# import csv
#
# from urllib3.filepost import writer

# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)} ")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году")
#
#         count += 1
#
#     print(f"Всего в файле: {count} строки")

# with open("data.csv") as f:
#     file_names = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=file_names)
#     count = 0
#
#     for row in file_reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)} ")
#         print(f"\t{row['Имя']} - {row['Профессия']}. Родился в {row['Год рождения']} году")
#         count += 1

# with open("student.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", 9, 15])
#     writer.writerow(["Саша", 5, 12])
#     writer.writerow(["Маша", 11, 17])

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", "w") as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)

#
# with open("student1.csv", "w") as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})

#
# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
#
# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(todos)
#
# with open('dict1_writer.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)
#

# Парсинг данных с сайтов

# from bs4 import BeautifulSoup
#
# f = open("index.html").read()
# soup = BeautifulSoup(f, "html.parser")
# # row = soup.find("div", class_="name").text
# # row = soup.find_all("div", class_="name")
# # row = soup.find_all("div", class_="row")[2].find("div", {"class": "name"})
# row = soup.find_all("div", {"data-set": "salary"})
# print(row)
#
