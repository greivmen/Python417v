f = open("DZtext.txt", "w")
f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
print("Тест:\n""Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n")
z = int(input("pos1 = "))
y = int(input("pos2 = "))
f.close()
f = open("DZtext.txt", "r")
red_file = f.readlines()
# print(red_file)
if z < 0 or y < 0 or z >= len(red_file) or y >= len(red_file):
    print("Не корректный ввод!")
else:
    red_file[z], red_file[y] = red_file[y], red_file[z]
    zam_str = ''.join(red_file)
    print(zam_str)
f.close()
f = open("DZtext.txt", "w")
f.writelines(red_file)
f.close()
