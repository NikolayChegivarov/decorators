import datetime
from functools import wraps

def logger(path):
    """записывает
     в файл 'main.log' дату и время вызова функции, имя функции, аргументы, с которыми вызвалась,
     и возвращаемое значение"""
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            with open(path, 'a', encoding='UTF-8') as log_file:
                log_file.write(f"Дата и время вызова функции: {datetime.datetime.now()}\n")
                log_file.write(f"Имя функции: {old_function.__name__}\n")
                if args or kwargs:
                    log_file.write(f"Аргументы: {args}, {kwargs}\n")
                else:
                    log_file.write("Аргументы отсутствуют\n")
                result = old_function(*args, **kwargs)
                log_file.write(f"Возвращаемое значение: {result}\n\n")
            return result
        return new_function
    return __logger
