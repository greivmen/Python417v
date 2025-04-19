a = [int(input("-> ")) for i in range(int(input("n: ")))]
s = 0
z = 0
for i in a:
    if i != 0:
        s += i
        z += 1
t = s / z
print("Среднее арифметическое: ", t)
