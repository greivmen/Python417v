from nevcar.ca import Car


class Electro(Car):
    def __init__(self, brand, model, graduation_year, mileage, battery):
        super().__init__(brand, model, graduation_year, mileage)
        self.battery = battery

    def print_info(self):
        car_info = super().print_info()
        return f"{car_info}\nЭтот автомобиль имеет мощность {self.battery}%"
