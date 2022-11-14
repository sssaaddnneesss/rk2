'''программа возвращающая букву из цифры'''
number = input('')
NEW_LINE = ''
for i in range(len(number)):
    NEW_LINE += chr(int(number[i]) + 96)
print(NEW_LINE)
