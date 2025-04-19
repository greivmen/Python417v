def decor(args1):
    def cnt(fn):
        def wrap(*args2):
            print(args1, ", ".join(map(str, args2)), "=", end=" ")
            fn(args2)

        return wrap

    return cnt


@decor("Сумма числил:")
def summa(args2):
    print(sum(args2))


@decor("Среднее арифметическое чисел:")
def _ar(args2):
    print(sum(args2) / len(args2))


summa(2, 3, 3, 4)

_ar(2, 3, 3, 4)


# другой вариант
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


