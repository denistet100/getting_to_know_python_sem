import phone_book
import view

pb = phone_book.PhoneBook('phone_bd.txt')


def start():
    while True:
        print(pb.main_menu())
        # length_pb = len(str(pb))
        length_pb = pb.count_pb(pb)
        choice = input('Выберите пункт меню: ')
        length_menu = len(pb.main_menu().split('\n')) - 1
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            match int(choice):
                case 1:
                    view.print_pb(pb)
                case 2:
                    name = input('Введите имя: ')
                    phone = input('Введите телефон: ')
                    comment = input('Введите комментарий: ')
                    pb.new_contact(name, phone, comment)
                case 3:
                    word = input('Введите поисковой запрос: ')
                    view.print_pb(pb.search(word))
                case 4:
                    view.print_pb(pb)
                    if length_pb > 0:
                        while True:
                            index = input('Введите индекс контакта, который хотите изменить: ')
                            if index.isdigit() and 0 < int(index) <= length_pb:
                                name = input('Введите имя (или Enter - оставить без изменений): ')
                                phone = input('Введите телефон (или Enter - оставить без изменений): ')
                                comment = input('Введите комментарий (или Enter - оставить без изменений): ')
                                pb.change(int(index)-1, name, phone, comment)
                                break
                            else:
                                view.print_pb('Проверьте правильность введённых данных.')
                case 5:
                    view.print_pb(pb)
                    if length_pb > 0:
                        while True:
                            index = input('Введите индекс контакта, который хотите удалить: ')
                            if index.isdigit() and 0 < int(index) <= length_pb:
                                pb.delete(int(index)-1)
                                break
                            else:
                                view.print_pb('Проверьте правильность введённых данных.')
                case 6:
                    pb.save()
                case 7:
                    return
        else:
            view.print_pb('Проверьте правильность введённых данных.')
