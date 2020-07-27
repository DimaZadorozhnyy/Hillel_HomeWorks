from datetime import datetime
"""
1
Input: Feb 12 2019 2:41PM
Output: 2019-02-12 14:41:00
Функция принимает строку (пример - Input) и возвращает строку (пример - Output)
"""


def convert_date(res_convert):
    res_date = datetime.strptime(res_convert, '%b %d %Y %I:%M%p')
    return res_date


date = 'Feb 12 2019 09:35PM'
print(convert_date(date))


"""
2
Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""


def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


digit = input("Введите число на проверку\n")
while not digit.isdigit():
    print("Вы ввели не число")
    digit = input("Введите число на проверку\n")
digit = int(digit)
print(is_prime(digit))


"""
3
Напишите функцию, которая принимает 1 аргумент (строка) и выполняет следующие действия на каждую из букв строки:
i - инкремент (+1)
d - дикремент (-1)
s - возведение в квадрат
o - добавить число в результативный список
остальные буквы игнорируются
Исходное число = 0
Результативный список = []
Вернуть результативный список
parse(iiisdoso"")  ==>  [8, 64]
"""


def some_fun(string):
    res_list = []
    count = string.count('i') - string.count('d')
    step = count
    for i in range(string.count('s')):
        count = count * step
    res_list.append(count)
    step = count
    for i in range(string.count('o') - 1):
        count = count * step
        res_list.append(count)
    return res_list


my_str = "iiisdoso"
print(some_fun(my_str))
