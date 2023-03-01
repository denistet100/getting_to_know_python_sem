# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.(это обязательно? мне лень всё самому вводить.)

import random


num_cnt_1 = int(input('Введите n - кол-во элементов первого множества:'))
num_cnt_2 = int(input('Введите m - кол-во элементов первого множества:'))
"""
my_list_1 = [random.randint(0, 20) for _ in range(num_cnt_1)]
my_list_2 = [random.randint(0, 20) for _ in range(num_cnt_2)]
print(my_list_1)
print(my_list_2)
"""
# Функций мне не хватает...

my_list_1 = []
for i in range(num_cnt_1):
    numb = int(input('Введите элемент первого множества:'))
    my_list_1.append(numb)
    
my_list_2 = []
for i in range(num_cnt_2):
    numb = int(input('Введите элемент второго множества:'))
    my_list_2.append(numb)

my_list_3 = sorted(list(set(my_list_1) & set(my_list_2)))
print(my_list_3)
