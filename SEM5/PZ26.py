# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree(num_1, num_2):
    if num_2 == 1:
        return num_1
    return num_1 * degree(num_1, num_2 - 1)


num_numerator = int(input('введи число: '))
num_degree = int(input('введи степень числа: '))
print(degree(num_numerator, num_degree))
