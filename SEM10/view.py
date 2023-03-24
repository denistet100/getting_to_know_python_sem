def print_pb(phone_book):
    if len(str(phone_book)) > 0:
        print('-' * len(str(phone_book)))
        print(phone_book)
        print('-' * len(str(phone_book)))
    else:
        print('Пусто!')
