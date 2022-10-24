import UI
import logger
import model

def edit_bdata():
    old_data = model.search_data()
    UI.print_data('Введите данные нового сотрудника: ')
    new_data = logger.get_data() + '\n'
    model.edit_data(old_data, new_data)


while True:
    mode = int(UI.type_of_task())
    if mode == 1:
        data = model.search_data()
        UI.print_data(data)
        
    elif mode == 2:
        data = logger.get_data()
        logger.write_data(data)
        
    elif mode ==3:
        edit_bdata()
    else:
        break
