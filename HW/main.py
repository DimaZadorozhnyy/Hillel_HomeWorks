from HW6.add import add
from HW6.subtraction import subtraction
from HW6.divide import divide
from HW6.multiply import multiply

if __name__ == "__main__":
    while True:
        first_digit = input("Введите первое число: ")
        if first_digit == 'exit':
            print("Окончание работы программы")
            break

        # Проверка на то, чтобы пользователь ввел имменно число !
        while not first_digit.isdigit():
            first_digit = input("Введите первое число: ")
        first_digit = float(first_digit)

        # Проверка на то, чтобы пользователь ввел имменно символ !
        symbol = input("Введите опрецию (+, -, * или /): ")
        while symbol not in ['+', '-', '*', '/']:
            symbol = input("Введите опрецию (+, -, * или /): ")

        # Проверка на то, чтобы пользователь ввел имменно число !
        second_digit = input('Введите второе число: ')
        while not second_digit.isdigit():
            second_digit = input("Введите второе число: ")
        second_digit = int(second_digit)

        if symbol == "+":
            print(f"Результатом сложения является:{add(first_digit, second_digit)}")
        elif symbol == '*':
            print(f"Результатом умножения является: {multiply(first_digit, second_digit)}")
        elif symbol == '-':
            print(f"Результатом вычетания является: {subtraction(first_digit, second_digit)}")
        elif symbol == '/':
            print(f"Результатом диления является: {divide(first_digit, second_digit)}")
