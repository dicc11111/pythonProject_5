def summary():
    with open ('file_5.txt', 'w+') as file_obj:
        line = input ('Введите цифры через пробел \n')
        file_obj.writelines (line)
        my_numb = line.split ()

        print (sum (map (int, my_numb)))


summary ()
