my_file = open('test2_txt', 'r')
content = my_file.readlines()
print(f'Количество строк в файле - {len(content)}')

my_file = open('test2_txt', 'r')
content = my_file.readlines()
for i in content:
    print(f'Количество слов - {len(i.split())}')
    my_file.close ()