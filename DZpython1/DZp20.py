class Human:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, v):
        if isinstance(v, str):
            self.__surname = v
        else:
            raise ValueError("Фамилия должно быть строкой")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, v):
        if isinstance(v, str):
            self.__name = v
        else:
            raise ValueError("Имя должно быть строкой")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, v):
        if isinstance(v, int):
            self.__age = v
        else:
            raise ValueError("Возраст должен быть числом")

    def print_info(self):
        return f"{self.__name} {self.__surname} {self.age} лет"


class Student(Human):
    def __init__(self, surname, name, age, spec, group, ball):
        super().__init__(surname, name, age)
        self.spec = spec
        self.group = group
        self.ball = ball

    @property
    def spec(self):
        return self.__spec

    @spec.setter
    def spec(self, v):
        if isinstance(v, str):
            self.__spec = v
        else:
            raise ValueError("Специальность должна быть строкой")

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, v):
        if isinstance(v, str):
            self.__group = v
        else:
            raise ValueError("Группа должна быть строкой")

    @property
    def ball(self):
        return self.__ball

    @ball.setter
    def ball(self, v):
        if isinstance(v, int):
            self.__ball = v
        else:
            raise ValueError("Средний балл должен быть числом")

    def print_info(self):
        return (f"Студент: {super().print_info()}, {self.spec}, группа {self.group} средний балл:"
                f" {self.ball}")


class Teacher(Human):
    def __init__(self, surname, name, age, subject, experience):
        super().__init__(surname, name, age)
        self.subject = subject
        self.experience = experience

    @property
    def subject(self):
        return self.__subject

    @subject.setter
    def subject(self, v):
        if isinstance(v, str):
            self.__subject = v
        else:
            raise ValueError("Тема должна быть строкой")

    @property
    def experience(self):
        return self.__experience

    @experience.setter
    def experience(self, v):
        if isinstance(v, int):
            self.__experience = v
        else:
            raise ValueError("Опыт должна быть строкой")

    def print_info(self):
        return f"Преподаватель: {super().print_info()}, предмет: {self.subject}, уровень навыка: {self.experience}"


class Graduate(Student):
    def __init__(self, surname, name, age, spec, group, ball, diploma):
        super().__init__(surname, name, age, spec, group, ball)
        self.diploma = diploma

    @property
    def diploma(self):
        return self.__diploma

    @diploma.setter
    def diploma(self, v):
        if isinstance(v, str):
            self.__diploma = v
        else:
            raise ValueError("Диплом должен быть строкой")

    def print_info(self):
        return f"Дипломник: {super().print_info()}, тема диплома: {self.diploma}"


p1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 2)
print(p1.print_info())
p1 = Student("Загидуллин", 'Линар', 32, "РПО", "PD_011", 5)
print(p1.print_info())
p1 = Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5,
              "Защита персональных данных")
print(p1.print_info())
p1 = Teacher("Даншин", "Андрей", 38, "Астрофизика", 110)
print(p1.print_info())
p1 = Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5)
print(p1.print_info())
p1 = Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
print(p1.print_info())
