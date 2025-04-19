s = 0

z = [(2, 4, 6), (5, 8, 2), (1, 6, 8)]


def glob(a, b, c):
    def rectangle(x, y):
        return x * y
    global s
    s = 2 * (rectangle(a, b) + rectangle(a, c) + rectangle(b, c))
    return s


print("Глобальная переменная:")
for a, b, c in z:
    print(glob(a, b, c))


def _local(a, b, c):
    def rectangle(x, y):
        return x * y
    ar = 2 * (rectangle(a, b) + rectangle(a, c) + rectangle(b, c))
    return ar


print("Локальная переменная:")
for a, b, c in z:
    print(_local(a, b, c))


def _nonlocal(a, b, c):
    ar = 0

    def rectangle(x, y):
        nonlocal ar
        ar += 2 * x * y
    rectangle(a, b)
    rectangle(a, c)
    rectangle(b, c)
    return ar


print("Нелокальная переменная:")
for a, b, c in z:
    print(_nonlocal(a, b, c))
