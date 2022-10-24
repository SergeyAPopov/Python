def write_data(a):
    with open ('data.txt', 'a', encoding='utf-8') as base:
        base.write(f'{a} \n')

def get_data():
    data_id = input('Введите id сотрудника: ')
    data_name= input("Введите ФИО сотрудника: ")
    data_phone= input("Введите номер телефона сотрудника: ")
    data_post =input("Введите должность сотрудника: ") 
    data_salary =input("Ввседите зарплату сотрудника: ")
    return (f'{data_id} || {data_name} || {data_phone} || {data_post}|| {data_salary}')