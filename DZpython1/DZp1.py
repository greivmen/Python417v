num = 97531
print("Исходное число", num)
a = num // 10000
b = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
e = num // 1 % 10
pr = a * b * c * d * e
ar = (a + b + c + d + e) / 5
print("Произведение цифр числа:", pr)
print("Среднее  арифметическое:", ar)
