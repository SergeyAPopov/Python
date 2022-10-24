def search_data():
    with open('data.txt', 'r', encoding='utf-8') as base:
        user_data = input('Введите данные для поиска: ')
        for i in base:
            if i.find(user_data) !=-1:
                return i


def edit_data(old_data, new_data):
    with open('data.txt', 'r', encoding='utf-8') as base:
        a=[]
        for i in base:
            a.append(i)
    a[a.index(old_data)] = new_data
    with open('data.txt', 'w+', encoding='utf-8') as base:
        for i in a:
            base.write(f'{i}')
