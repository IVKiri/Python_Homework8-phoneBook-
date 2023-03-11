

def search_data(data):
    flag = False
    key = input('Введите имя для поиска: ').lower()
    
    for k, v in data.items():
        if key.lower() in k.lower():
            print(f"контакт найден:\n{k}", end=' - ')
            for i, j in v.items():
                print(i, end=': ')
                print(*j, end=' | ')
            print('\n')
            flag = True
          
    if flag == False:
        print('Имя не найдено.')