a = input('Введите ФИО: ')
b = a.upper()
c = b.split()
print(list(c[2])[0], list(c[0])[0], list(c[1])[0])