# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def division(number):
    remainder = number // 2
    integer = number % 2

    return integer, remainder
def convert_to_binary(num):
    binary_list = []

    while num > 0:
        i, num = division(num)
        binary_list.insert(0, i)

    return binary_list

number = int(input('Введите десятичное число: '))

print(*convert_to_binary(number), sep='')