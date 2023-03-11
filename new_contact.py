

def new_record(book):
    k = input('Введите новое имя: ')
    a = {}
    a['phone'] = list(input('Введите номер телефона (без пробелов): ').split())
   
    a['birthday'] = input('Дата рождения: ')
    a['email'] = input('email: ')
    book[k] = a