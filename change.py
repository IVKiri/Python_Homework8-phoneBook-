

def change_contact(data):
    flag = False
    key = input('Введите имя для изменения: ').lower()
    
    for k, v in data.items():
        if key.lower() in k.lower():
            print(f"контакт найден:\n{k}", end=' - ')
            for i, j in v.items():
                print(i, end=': ')
                print(*j, end=' | ')
            print('\n')
            flag = True
            action = input('Что необходимо изменить?\n'
                '0 - удалить контакт\n'
                '1 - Имя\n'
                '2 - Телефон \n'
                '3 - День рождения\n'
                '4 - email\n'
                'q - в главное меню\n')
            if action == '0':
                del data[k]
                print(f"Контакт {k} удален \n")
                break
            elif action == '1':
                new_name = input('Введите новое имя: ')
                data[new_name] = data[k]
                del data[k]
                print(f'Имя изменено на {new_name}')
                break
            elif action == '2':
                d = input('Введите 1 для изменения\nвведите 2 для добавления номера\nq - в главное меню\n')
                if d == '2':
                    data[k]['phone'].insert(0, input('Введите номер телефона (без пробелов): '))
                    print('Номер добавлен.')
                elif d == '1':
                    number = 0
                    for i in data[k]['phone']:
                        print(number+1, ' - ', i)
                        number+=1
                    number = int(input('Какой номер изменить?\n'))
                    act = input('изменить - 1, удалить - 2\n')
                    if act == '1':
                        data[k]['phone'].pop(number-1)
                        data[k]['phone'].insert(0, input('Введите номер телефона (без пробелов): '))
                        print('Номер изменён.')
                    elif act == '2':
                        data[k]['phone'].pop(number-1)
                        print('Номер удалён.')
                    else:
                        print('Неверный ввод.')
                        break
                elif d == 'q':
                    break
                else:
                        print('Неверный ввод.')
                        break
            elif action == '3':
                data[k]['birthday'] = input('Введите дату рождения: ')
            elif action == '4':
                data[k]['email'] = input('Введите email: ')
            elif action == 'q':
                break
            else:
                print('Неверный ввод.')
                break
                      
          
    if flag == False:
        print('Имя не найдено.')