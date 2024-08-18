my_dict = {'Имя': 'Елена', 'год рождения': 1988}
print(my_dict)

print(my_dict.get('Имя'))
print(my_dict.get('Фамилия'))
my_dict ['Фамилия'] = 'Нечаева'
print(my_dict.get('Фамилия'))

my_dict.update({'Отчество': 'Сергеевна', 'телефон': +79999999999})
print(my_dict)

a = my_dict.pop('Отчество')
print(a)
print(my_dict)

my_set = {'B', 1, 2, 2, 1, 'B', 'A', 0.5}
print(my_set)
my_set.update({'C', (4,5,6)})
my_set.discard(0.5)
print(my_set)
