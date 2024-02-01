# первая задача
import os
import datetime
from functools import wraps

def logger(old_function):
    """записывает
     в файл 'main.log' дату и время вызова функции, имя функции, аргументы, с которыми вызвалась,
     и возвращаемое значение"""
    @wraps(old_function)
    def new_function(*args, **kwargs):
        # Открываем файл в режиме добавления.
        with open('main.log', 'a', encoding='UTF-8') as log_file:
            # Записываем дату и время вызова функции
            log_file.write(f"Дата и время вызова функции: {datetime.datetime.now()}\n")
            # Записываем имя функции
            log_file.write(f"Имя функции: {old_function.__name__}\n")
            # Записываем аргументы функции
            if len(args) > 0 or len(kwargs) > 0:
                log_file.write(f"Аргументы: {args}, {kwargs}\n")
            else:
                log_file.write("Аргументы отсутствуют\n")
            # Вызываем исходную функцию и получаем результат
            result = old_function(*args, **kwargs)
            # Записываем возвращаемое значение функции
            log_file.write(f"Возвращаемое значение: {result}\n\n")

        # Вернуть результат исходной функции
        return result

    return new_function


def test_1():
    # Проверяет, существует ли файл с именем "main.log" в текущем каталоге, и если да, то удаляет этот файл.
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, 'r', encoding='UTF-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()