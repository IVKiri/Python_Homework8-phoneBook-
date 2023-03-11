import json
from reading_pb import print_pb
from searching_contacts import search_data
from new_contact import new_record
from change import change_contact
# import os
# os.chdir('phonebook')
# print(os.getcwd())

file = 'phone_book.json'
phone_book = {}

def load_data(path):
    with open(path, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
        BD_local = json.load(fh)  # загружаем из файла данные в словарь data
    print('БД успешно загружена')
    return BD_local

def save_file(path, data):
    # сохранить в json
    with open(path, 'w', encoding='utf-8') as fh:  # открываем файл на запись
        # преобразовываем словарь data в unicode-строку и записываем в файл
        fh.write(json.dumps(data, ensure_ascii=False))
    print('БД успешно сохранена')


def run_pb():
      
    work = True
    while work:
        action = input(
        'Выберите действие (введите нужную цифру):\n'
        '1 - чтение телефонной книги\n'
        '2 - добавить новый контакт\n'
        '3 - редактировать или удалить контакт\n'
        '4 - поиск\n'
        '5 - сохранить данные\n'
        'q - Выход\n').lower()

        if action == '1':
            print_pb(phone_book)
        elif action == '2':
            new_record(phone_book)
        elif action == '3':
            change_contact(phone_book)
        elif action == '4':
            search_data(phone_book)
        elif action == '5':
            save_file(file, phone_book)
        elif action == 'q':
            print('Выполнен выход.')
            save_file(file, phone_book)
            work = False
        else:
            print('НЕВЕРНАЯ ЦИФРА')

try:
    phone_book = load_data(file)
except:
    phone_book = {
        'Миша гараж': {'phone': ['72443351195', '72627397543'], 'birthday': '11-02-2010', 'email': "mail@mail.ru"},
        'Sasha': {'phone': ['78436840045', '77554802591']}}
    print('База данных не найдена. Создана тестовая БД.')

run_pb()