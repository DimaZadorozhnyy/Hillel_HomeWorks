from math import sqrt
''''
1. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время
года, которому этот месяц принадлежит (зима, весна, лето или осень).
'''


def get_season(number):
    if number in [1, 2, 12]:
        return f"{number}-й месяц это зима"
    elif number in range(3, 6):
        return f"{number}-й месяц это весна"
    elif number in range(6, 9):
        return f"{number}-й месяц это лето"
    elif number in range(9, 12):
        return  f"{number}-й месяц это осень"


number = input("Введите номер месяца от 1 до 12:\n")
while not number.isdigit() or number not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
    print("Некоректный ввод, повторите попытку")
    number = input("Введите номер месяца от 1 до 12:\n ")
number = int(number)

print(get_season(number))


"""
2. Реализовать функцию, которая принимает строку и расделитель и возвращает словарь {слово: количество повторений}
"""


def converter(string, separate):
    string = string.split(separate)
    my_dict = {}
    my_string = my_dict.fromkeys(string, 0)
    for i in string:
        my_string[i] += 1
    return my_string


delimiter = input("delimiter:\n")
my_str = input('String:\n')
print(converter(my_str, delimiter))


'''
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, 
площадь квадрата и диагональ квадрата.
'''


def get_rectangle_data(a):
    perimeter = a * 4
    area = a**2
    diagonal = a * sqrt(2)
    return f" Периметр квадрата равен {perimeter}\n Площадь квадрата равна {area}\n Диагональ квадрата равна {diagonal}"


a = input("Введите длинну стороны а: \n")
while not a.isdigit():
    print("Некоректный ввод, повторите попытку !")
    a = input("Введите длинну стороны а: \n")
a = int(a)


print(get_rectangle_data(a))