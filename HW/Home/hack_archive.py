import string
import random
import zipfile
from itertools import product


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем и возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def hack_archive(file_name):
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток
    my_list = []
    for i in product("1234567890", repeat=4):
        password = ''.join(i)
        tries += 1
        if extract_archive(file_to_open, password):
            break
        elif password in wrong_passwords:
            continue
        wrong_passwords.append(password)

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')
    print(wrong_passwords, "\n", tries, '\n', password)


#############

filename = 'archive.zip'
hack_archive(filename)