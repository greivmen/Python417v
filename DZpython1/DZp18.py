class Area:
    __count = 0

    @staticmethod
    def triangle(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        Area.__count += 1
        return area

    @staticmethod
    def triangle2(base, height):
        area = 0.5 * base * height
        Area.__count += 1
        return area

    @staticmethod
    def square(side):
        area = side ** 2
        Area.__count += 1
        return area

    @staticmethod
    def rectangle(length, width):
        area = length * width
        Area.__count += 1
        return area

    @staticmethod
    def get_count():
        return Area.__count


triangle_vid = Area.triangle(3, 4, 5)
print("Площадь треугольника по формуле Герона (3,4,5):", triangle_vid)
triangle_vid2 = Area.triangle2(6, 7)
print("Площадь треугольника через основание и высоту (6,7):", triangle_vid2)
square_vid = Area.square(7)
print("Площадь квадрата (7):", square_vid)
rectangle_vid = Area.rectangle(2, 6)
print("Площадь прямоугольника (2,6):", rectangle_vid)

print("Количество подсчетов площади:", Area.get_count())
