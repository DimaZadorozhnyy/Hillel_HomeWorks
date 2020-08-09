import string
import random
import zipfile


PASSWORD_LENGTH = 4


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
    while True:
        password = random.randint(1000, 9999)
        password = str(password)
        if password in wrong_passwords:
            continue
        elif extract_archive(file_to_open, password):
            break
        wrong_passwords.append(password)
        tries += 1
        continue

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')
    print(wrong_passwords, "\n", tries, '\n', password)

#############
filename = 'archive.zip'
hack_archive(filename)
