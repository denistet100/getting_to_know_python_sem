# 1. Открыть файл телефонной книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

# имя
# номер
# коммент

__author__ = "Tramp_Gemtleman"

import re


def menu():
    dict_phnbk = {}
    while True:
        print('________________________________________________________________________________________________________'
              '______________________________________________')
        anc = 0
        try:
            anc = int(input('Меню: \n 1:Сохранить телефонную книгу, 2: Показать все контакты, 3:Найти контакт '
                            '4:Добавить контакт, 5:Изменить контакт,  6: Удалить контакт, 7: Выход \n Введите запрос:'))
        except ValueError:
            print('Вы ввели не число!')

        # Сохранить телефонную книгу
        if anc == 1:
            cntc_output(dict_phnbk)
            save_dir(dict_phnbk)
        # Показать все контакты
        elif anc == 2:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print('Справочник пуст')
            else:
                cntc_output(dict_phnbk)
        # Найти контакт
        elif anc == 3:
            cntc_find(dict_phnbk)
        # Добавить контакт
        elif anc == 4:
            dict_phnbk = add_cntc(dict_phnbk)
            print('Сохранись!')
        # Изменить контакт
        elif anc == 5:
            new_cntc = cntc_find(dict_phnbk)
            no_cntc = new_cntc
            keys = new_cntc.keys()
            print('___________')
            change = int(input('Что Вы хотите изменить?\n 1:Имя Фамилию, 2: Телефон, 3:Комментарий \n Введите запрос:'))
            if change == 1:
                change_name = input('Введите новое Имя Фамилию:')
                new_cntc = {change_name: new_cntc[keys]}
            elif change == 2:
                change_phone = input('Введите новое телефон:')
                new_cntc = {keys: [change_phone, new_cntc[keys][1]]}
            elif change == 3:
                change_comm = input('Введите новое комментарий:')
                new_cntc = {keys: [new_cntc[keys][0], change_comm]}
            dict_phnbk = del_cntc(dict_phnbk, no_cntc)
            dict_phnbk = add_cntc(dict_phnbk, new_cntc)
        # Удалить контакт
        elif anc == 6:
            no_cntc = cntc_find(dict_phnbk)
            print(f'Удалили контант:{cntc_output(no_cntc)}')
            dict_phnbk = del_cntc(dict_phnbk, no_cntc)
            print('Сохранись!')
        # Выход
        elif anc == 7:
            print('End')
            break
        # Не верная цифра
        else:
            print('Введите ещё раз')


def open_read_dir():
    dict_phnbk = {}
    with open('phonebook.txt', 'r', encoding='UTF-8') as f:
        for line_cntc in f.read().splitlines():
            key, value = line_cntc.split(':')
            pattern = r'\'{1}\w+\'{1}'
            value = (re.findall(pattern, value))
            value_phone, value_comm = value
            dict_phnbk[key] = [value_phone[1:-1], value_comm[1:-1]]
        return dict_phnbk


def save_dir(dict_phnbk):
    str_phnbk = ''
    if len(dict_phnbk) != 0:
        for key, value in dict_phnbk.items():
            str_phnbk += f'{key}:{value}\n'
        with open('phonebook.txt', 'w', encoding='UTF-8') as f:
            f.write(str_phnbk)
        print('save')
    else:
        print('Нечего сохранять!')


def add_cntc(dict_phnbk, new_cntc_in={}):
    if len(dict_phnbk) == 0:
        dict_phnbk = open_read_dir()
    if len(new_cntc_in) < 1:
        name_cntc = input('Введите имя фамилию:')
        phone_cntc = input('Введите телефон:')
        comment_cntc = input('Введите комментарий:')
        new_cntc_in.setdefault(name_cntc, [phone_cntc, comment_cntc])
    dict_phnbk.update(new_cntc_in)
    return dict_phnbk


def cntc_find(dict_phnbk):
    while True:
        name_cntc_dict = {}
        if len(dict_phnbk) == 0:
            dict_phnbk = open_read_dir()
        name_cntc = input('Введите имя фамилию:')
        list_keys = list(map(lambda keys: keys,  dict_phnbk.keys()))
        pattern_name_cntc = r'\w*' + re.escape(name_cntc) + r'\w*'
        r = re.compile(pattern_name_cntc)
        new_list = list(filter(r.match, list_keys))
        if len(new_list) > 0:
            for key in new_list:
                name_cntc_dict.setdefault(key, dict_phnbk[key])
            cntc_output(name_cntc_dict)
        else:
            print(f'Не найдено!')

        if len(name_cntc_dict) == 1:
            return name_cntc_dict
        else:
            print('Выберите один номер. Введите его точнее!')


def cntc_output(dict_phnbk):
    for line_dict_phnbk in dict_phnbk:
        phone_and_comm = dict_phnbk[line_dict_phnbk]
        print(f'{phone_and_comm[0]} {line_dict_phnbk} {phone_and_comm[1]}')


def del_cntc(dict_phnbk, no_cntc):
    if len(dict_phnbk) == 0:
        dict_phnbk = open_read_dir()
    for key in no_cntc:
        del dict_phnbk[key]
    return dict_phnbk


menu()
