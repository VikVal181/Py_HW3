# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

number = int(input('Введите колличество элементов списка: '))
my_list = []

print(f'Ввете элементы списка:')
for i in range(number):
    my_list.append(float(input()))

print(my_list)

max = my_list[0] % 1
min = max

for i in range(1, len(my_list)):
    if my_list[i] % 1 > max:
        max = my_list[i] % 1
    elif my_list[i] % 1 < min:
        min = my_list[i] % 1

print(f'Разница max и min дробных частей = {round((max - min), 2)}')
