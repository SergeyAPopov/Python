
from re import A


def what_to_do():
    print(f' 1 - Записать новый контакт \n 2 - Найти информацию в справочнике')
    a = int(input('Введите необходимое действие:'))
    if a == 1 or a == 2:
        return a
    else:
        print('Введено некорректное значение!')    

def find_info():
    search_info = str(input('Введите иня контакта:'))
    with open('phonebook.txt','r') as f:
        for line in f:
            if search_info in line:
                print(line)
        f.close

def get_info():
    x = str(input('Введите имя контакта: '))
    y =  str(input('Введите телефон контакта: '))
    return [x,y]
