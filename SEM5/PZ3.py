# a, b, z = random создать 2 многочлена, сложить 2 многочлена, вывести 3й многочлен
# a*x**n + b*x**(n-1)+ .. + z*x**(n-n) = 0


import random


def make_list_polinomial(num):
    num_list_rand = [random.randint(0, 20) if i > 0 else random.randint(1, 20) for i in range(num)]
    # print(num_list_rand)
    return num_list_rand


def polinomial(num_rand):
    dict_polin = {}
    list_polin = []
    cnt_num = len(num_rand)

    for i in range(cnt_num):
        if num_rand[i] != 0:
            dict_polin[cnt_num - i - 1] = f'{num_rand[i]}'

    for key, value in dict_polin.items():
        if key != 0:
            if key > 1:
                if int(value) > 1:
                    list_polin.append(f'{value}*x**{key}')
                else:
                    list_polin.append(f'x**{key}')
            else:
                if int(value) > 1:
                    list_polin.append(f'{value}*x')
        else:
            if int(value) > 0:
                list_polin.append(f'{value}')

    str_polin = "+".join(list_polin)
    str_polin += f' = 0'
    return str_polin


def parsing(str_pol):
    list_pol = str_pol.split('+')
    # print(list_pol)
    save_list = []
    for i in range(len(list_pol)):
        if len(list_pol[i]) > 2:
            new_list_pol = list_pol[i].replace('*', '')
            list_1_pol = new_list_pol.split('x')
            # print(list_1_pol)
            if '' in list_1_pol:
                for j in range(len(list_1_pol)):
                    if list_1_pol[j] not in '':
                        continue
                    else:
                        list_1_pol[j] = list_1_pol[j].replace('', '1')
            if len(list_1_pol) < 2:
                if ' = 0' in list_1_pol[0]:
                    list_1_pol = list_1_pol[0].replace(' = 0', '').split('x')
                    list_1_pol.append('0')
                    # print(list_1_pol)
            elif len(list_1_pol) == 2:
                if ' = 0' in list_1_pol[1]:
                    list_1_pol[1] = '1'
                    # print(list_1_pol)
        save_list.append(list_1_pol)
    # print(save_list)
    cnt_degree = int(save_list[0][1]) + 1
    # print(cnt_degree)
    iter = 0
    while iter < len(save_list):
        cnt_degree -= 1
        # print('cnt_degree: ', cnt_degree)
        # print(f'save_list[{iter}][1]: ', save_list[iter][1])
        const = int(save_list[iter][1])
        cnst_cnt_degree = cnt_degree
        j = iter
        while const != cnt_degree:
            save_list.insert(j, ['0', f'{cnt_degree}'])
            # print(save_list)
            j += 1
            cnt_degree -= 1
        cnt_degree = cnst_cnt_degree
        # print('cnt_degree: end  ', cnt_degree)
        iter += 1
    # print(save_list)
    ret_list = []
    for value in save_list:
        ret_list.append(int(value[0]))
    # print(save_list)
    return ret_list


numb = int(input('Какой степени многочлен:')) + 1

polinom_1 = polinomial(make_list_polinomial(numb))
polinom_2 = polinomial(make_list_polinomial(numb))
print('polinom_1: ', polinom_1)
print('polinom_2: ', polinom_2)

sum_pol = list(map(lambda x, y: x + y, parsing(polinom_1), parsing(polinom_2)))
# print(sum_pol)

end_polin = polinomial(sum_pol)
print('end_polin: ', end_polin)
