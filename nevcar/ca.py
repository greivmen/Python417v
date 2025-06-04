class Car:
    def __init__(self, brand, model, graduation_year, mileage):
        self.brand = brand
        self.model = model
        self.graduation_year = graduation_year
        self.mileage = mileage

    def print_info(self):
        return f"{self.brand}, {self.model}, {self.graduation_year} год, {self.mileage} км"


__author__ = "admin"

if __name__ == '__main__':
    print(f"Module {__name__} (author: {__author__})")
