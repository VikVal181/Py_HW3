# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def find_sum_pair(in_list):
    out_list = []
    length_in_list = len(in_list)
    for i in range(int(length_in_list / 2)):
        out_list.append(in_list[i] * in_list[length_in_list - 1 - i])

    if length_in_list % 2 != 0:
        out_list.append(in_list[int(length_in_list / 2)] ** 2)

    return out_list

number = int(input('Введите колличество элементов списка: '))
my_list = []

print(f'Ввете элементы списка:')
for i in range(number):
    my_list.append(int(input()))

print(my_list)
print(find_sum_pair(my_list))
