def divide(a, b):
    while b == 0:
        print("На ноль делить нельзя")
        b = input("Попробуйте заново: ")
        while not b.isdigit():
            b = input("Введите второе число: ")
        b = int(b)
    res = a / b
    return res