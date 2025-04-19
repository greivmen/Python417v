region = {
    "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
    "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
    "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
    "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
}
for i in region:
    print(i, '\n',  "N :", region[i]["N"], '\n',  "S :", region[i]["S"], '\n',  "E :", region[i]["E"], '\n', "W :",
          region[i]["W"], )
name = input("Имя: ")
reg = input("Регион: ")
if name in region and reg in region[name]:
    print(region[name][reg])
    try:
        nev_z = int(input("Новое значение: "))
        region[name][reg] = nev_z
        print(region[name])
    except ValueError:
        print("Не корекктынй ввод данных!")
else:
    print("Не корекктынй ввод данных!")

# >Другой вариант... если не заморачиваться с поверками:

# region = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451},
# }
# for i in region:
#     print(i, '\n',  "N :", region[i]["N"], '\n',  "S :", region[i]["S"], '\n',  "E :", region[i]["E"], '\n', "W :",
#           region[i]["W"], )
# name = input("Имя: ")
# reg = input("Регион: ")
# print(region[name][reg])
# nev_z = input("Новое значение: ")
# region[name][reg] = nev_z
# print(region[name])
