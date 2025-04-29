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
import random
import time
from dataclasses import asdict
from itertools import count
from multiprocessing.context import set_spawning_popen
from platform import python_implementation
from sys import prefix
from textwrap import dedent
from urllib.request import proxy_bypass_registry

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


#----вВОРОНЫ
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
