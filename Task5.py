# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def positive(in_list):
    if len(in_list) == 1:
        return 1
    else:
        length = len(in_list)
        return in_list[length-2] + in_list[length-1]

def negative(in_list):
    if len(in_list) == 1:
        return 1
    else:
        return in_list[1] - in_list[0]

def fibonachi(num):
    fibonachi_list = [0]

    for i in range(num):
        fibonachi_list.append(positive(fibonachi_list))
        fibonachi_list.insert(0, negative(fibonachi_list))

    return fibonachi_list

number = int(input('Введите число: '))

print(fibonachi(number))