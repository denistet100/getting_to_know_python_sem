# Задача 32:
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list_1 = [random.randint(-10, 10) for _ in range(20)]
print(list_1)
min_nmbr = int(input('min'))
max_nmbr = int(input('max'))

for i in range(len(list_1)):
    if min_nmbr <= list_1[i] <= max_nmbr:
        print(i, end = '  ')
