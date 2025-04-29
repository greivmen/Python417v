def gret(n):
    if not n:
        return 0
    if n[0] < 0:
        return 1 + gret(n[1:])
    else:
        return gret(n[1:])


print("n =", gret([-2, 3, 8, -11, -4, 6]))
