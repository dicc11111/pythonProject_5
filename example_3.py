with open('test3_txt', 'r') as my_file:
    test3 = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        test3.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, test3)) / len(test3)}')

    