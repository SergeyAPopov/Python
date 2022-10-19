import model
import logger


solution = model.what_to_do()

if solution == 1:
    contact = model.get_info()
    logger.log_phone(contact)
elif solution ==2:
    model.find_info()



