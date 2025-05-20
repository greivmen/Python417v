class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value):
        self.__surname = surname
        self.__num = num
        self.__percent = percent
        self.__value = value
        print(f"Счет #{self.num} принадлежащий {self.surname} счет был открыт.")
        print("*" * 50)

    def __del__(self):
        print("*" * 50)
        print(f"Счет #{self.num} принадлежащий {self.surname} счет был закрыт.")

    @staticmethod
    def convert(value, rate):
        return value * rate

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):
        cls.rate_eur = rate

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str) or isinstance(surname, float):
            self.__surname = surname
        else:
            print("Фамилия должно состоять из строки!")

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if isinstance(num, str) or isinstance(num, float):
            self.__num = num
        else:
            print("№ должен состоять из строки!")

    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent):
        if isinstance(percent, int) or isinstance(percent, float):
            self.__percent = percent
        else:
            print("% должен быть числом!")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if isinstance(value, str) or isinstance(value, float):
            self.__value = value
        else:
            print("Баланс должен состоять числом!")

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        if isinstance(surname, str) or isinstance(surname, float):
            self.__surname = surname
        else:
            print("Фамилия должно состоять из строки!")

    def get_num(self):
        return self.__num

    def set_num(self, num):
        if isinstance(num, str) or isinstance(num, float):
            self.__num = num
        else:
            print("№ должен состоять из строки!")

    def get_percent(self):
        return self.__percent

    def set_percent(self, percent):
        if isinstance(percent, int) or isinstance(percent, float):
            self.__percent = percent
        else:
            print("% должен быть числом!")

    def get_value(self):
        return self.__value

    def set_value(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__value = value
        else:
            print("% должен быть числом!")

    def convert_to_usd(self):
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f"Состояние счета: {usd_val} {Account.suffix_usd}")

    def convert_to_eur(self):
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f"Состояние счета: {eur_val} {Account.suffix_eur}")

    def edit_owner(self, surname):
        self.surname = surname

    def add_percent(self):
        self.value += self.value * self.percent
        print("Проценты были успешно начислены")
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.value:
            print(f"К сожалению у вас нет {val} {Account.suffix}")
        else:
            self.value -= val
            print(f"{val} {Account.suffix} было успешно снято")

        self.print_balance()

    def add_money(self, val):
        self.value += val
        print(f"{val} {Account.suffix} было успешно добавлено!")
        self.print_balance()

    def print_balance(self):
        print(f"Текущий баланс {self.value} {Account.suffix}")

    def print_info(self):
        print("Информация о счете")
        print("-" * 20)
        print(f"#{self.num}")
        print(f"Владелец:{self.surname}")
        self.print_balance()
        print(f"Проценты: {self.percent:.0%}")
        print("-" * 20)


acc = Account("Долгих", "12345", 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
print()
Account.set_usd_rate(1)
Account.set_eur_rate(3)
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner("Дюма")
# print(acc.surname)
# acc.num = 300
print(acc.surname)
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(3000)
print()

acc.withdraw_money(100)
print()
acc.add_money(5000)
print()
acc.withdraw_money(3000)
print()
