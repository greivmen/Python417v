class Student:
    def __init__(self, name):
        self.name = name
        self.lp = self.Laptop("HP", "i7", 16)

    def show(self):
        print(f"{self.name} => {self.lp.model}, {self.lp.processor}, {self.lp.memory}")

    class Laptop:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory


stud1 = Student("Roman")
stud1.show()
stud2 = Student("Vladimir")
stud2.show()

