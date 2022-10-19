def log_phone(list):
    with open('phonebook.txt','a') as f:
        f.write(f'{list[0]} || {list[1]}\n')
        f.close

