'''то же самое, но ввод и вывод через файлы'''
with open('stdin.txt', 'r', encoding='utf-8') as file_1:
    number = file_1.read()
    NEW_LINE = ''
    for i in range(len(number)):
        NEW_LINE += chr(int(number[i]) + 96)
with open('stdout.txt', 'w', encoding='utf-8') as file_2:
    file_2.write(NEW_LINE)
