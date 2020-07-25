import random
from datetime import datetime
import json


def revers_string(my_str):
    return my_str[::-1]


# Считывание и запись фалов json
with open('questions.json', 'r') as file:
    date = json.load(file)

    for i in date['questions']:
        i['answer'] = input(i['q'])

with open("questions.json", 'w') as file:
    json.dump(date, file, indent=4)


# Считывание и запись фалов txt
with open('Text_read.txt', 'r') as file_r, open('Text_write.txt', 'a+') as file_w_r:
    read = file_r.read()
    print(read)
    file_w_r.write(read)
    string = input("Enter you string")
    file_w_r.write(revers_string(string))


# Угадайка, попробуйте угадать число из диапазона от 1 до 50, у вас 10 попыток
attempts = 10
num = input('попробуйте угадать число от 1 до 50:\n')
while not num.isdigit():
    print("Вы ввели не число, повторите попытку:\n")
    num = input("попробуйте угадать число от 1 до 50:\n")
num = int(num)

random_num = random.randint(1, 50)

for i in range(1, attempts + 1):
    attempts -= 1
    if num == random_num:
        data = {"Guessed the number": str(datetime.now())}
        with open("questions.json", 'a') as file:
            json.dump(data, file, indent=4)
        print("Поздравляю вы угадали !!!))")
        break

    elif attempts == 0:
        print("Попытки закончились")

    elif num != random_num:
        print(f"Не угадали не беда, количество попыток: {attempts}")
        num = input('попробуйте угадать число от 1 до 50:\n')
        while not num.isdigit():
            print("Вы ввели не число, повторите попытку:\n")
            num = input("попробуйте угадать число от 1 до 50:\n")

        num = int(num)
