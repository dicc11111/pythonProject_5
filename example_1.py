my_file = input('Введите данные \n')
file = open("test_txt", "w")
while my_file:
    file.writelines(my_file)
    my_file = input('Введите данные \n')
    if not my_file:
        break

file.close()
file = open("test_txt", "r")
content = file.read()
print(content)
file.close()