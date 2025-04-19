n = int(input("Количество студентов: "))
student = {}
for i in range(1, n + 1):
    name = input(str(i) + "-й студент: ")
    bal = int(input("Балл: "))
    student[name] = bal
# print(student)
sr_bal = sum(student.values()) / n
res = [name for name, bal in student.items() if bal > sr_bal]
print("\nСредний балл: " + str(round(sr_bal)), "." " Студенты с балом выше среднего:", sep="")
for name in res:
    print(name)
