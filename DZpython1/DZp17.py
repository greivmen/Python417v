class Car:

    def __init__(self, model, year, creator, power, colour, price):
        self.__model = model
        self.__year = year
        self.__creator = creator
        self.__power = power
        self.__colour = colour
        self.__price = price

    def print_ifo(self):
        print("Данные автомобиля".center(40, "*"))
        print(f"Название модели: {self.__model}\nГод выпуска: {self.__year}\nПроизводитель: {self.__creator}\nМощность "
              f"двигателя: {self.__power} л.с\nЦвет машины: {self.__colour}\nЦена: {self.__price} $")
        print("=" * 40)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) or isinstance(model, float):
            self.__model = model
        else:
            print("Координаты должны быть строками!")

    def get_year(self):
        return self.__year

    def set_year(self, year):
        if isinstance(year, int) or isinstance(year, float):
            self.__year = year
        else:
            print("Координаты должны быть числами!")

    def get_creator(self):
        return self.__creator

    def set_creator(self, creator):
        if isinstance(creator, str) or isinstance(creator, float):
            self.__creator = creator
        else:
            print("Координаты должны быть строками!")

    def get_power(self):
        return self.__power

    def set_power(self, power):
        if isinstance(power, str) or isinstance(power, float):
            self.__power = power
        else:
            print("Координаты должны быть строками!")

    def get_colour(self):
        return self.__colour

    def set_colour(self, colour):
        if isinstance(colour, str) or isinstance(colour, float):
            self.__colour = colour
        else:
            print("Координаты должны быть строками!")

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if isinstance(price, int) or isinstance(price, float):
            self.__price = price
        else:
            print("Координаты должны быть числами!")


h1 = Car("X7 M50i", 2021, "BMV", "530", "white", 10790000)
# h1.print_ifo()

h1.print_ifo()
h1.model = "X6"
h1.print_ifo()
print(h1.model)
# h1.set_year(2025)
# print(h1.get_year())
# h1.set_creator("KIA")
# print(h1.get_creator())
# h1.print_ifo()
# h1.set_power("5345")
# print(h1.get_power())
# h1.print_ifo()
# h1.set_colour("RED")
# print(h1.get_colour())
# h1.print_ifo()
# h1.set_price(123)
# print(h1.get_price())
# h1.print_ifo()