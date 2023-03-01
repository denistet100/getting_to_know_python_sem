# a, b, z = random создать 2 многочлена, сложить 2 многочлена, вывести 3й многочлен

# a*x**n + b*x**(n-1)+ .. + z*x**(n-n) = 0



# ПОГОДИ, Я ЕЩЁ НЕ ДОДЕЛАЛ!!!!!!!!


import random


def polinomial(num):
    num_rand = [random.randint(0, 20) for _ in range(num)]
    print(num_rand)
    dict_polin = {}
    list_polin = []
    str_polin = ''

    for i in range(num):
        if num_rand[i] != 0:
            dict_polin[num - i - 1] = f'{num_rand[i]}'

    for key, value in dict_polin.items():
        if key != 0:
            if key > 1:
                list_polin.append(f'{value}*x**{key}')
            else:
                list_polin.append(f'{value}*x')
        else:
            list_polin.append(f'{value}')

    str_polin = "+".join(list_polin)
    str_polin += f' = 0'
    return str_polin


def parsing(str_pol):
    list_pol = str_pol.split('+')
    print(list_pol)
    for i in range(len(list_pol)):
        # translation_map = str.maketrans('*', '')
        if len(list_pol[i]) > 2:
            new_list_pol = list_pol[i].replace('*', '')
            list_1_pol = new_list_pol.split('x')
            print(list_1_pol)


def sum_pol(str_pol_1, str_pol_2):
    pass


numb = int(input('Какой степени многочлен:'))

a = polinomial(numb)
b = polinomial(numb)
print(a)
print(b)

parsing(a)
parsing(b)
