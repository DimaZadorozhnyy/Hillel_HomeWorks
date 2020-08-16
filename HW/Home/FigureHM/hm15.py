class Triangle:

    def __init__(self, side_1, side_2, side_3, height_t):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
        self.height_t = height_t

    def triangle_area(self):
        return (1 / 2) * (self.side_1 * self.height_t)

    def triangle_perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class Square:
    def __init__(self, side):
        self.side = side

    def square_area(self):
        return self.side ** 2

    def square_perimeter(self):
        return self.side * 4


class Rectangle:
    def __init__(self, side_1, side_2):
        self.side_1 = side_1
        self.side_2 = side_2

    def rectangle_area(self):
        return 2 * (self.side_1 * self.side_2)

    def rectangle_perimeter(self):
        return self.side_2 * self.side_1


side_a = 2
side_b = 3
side_c = 4
height = 5

figure = input("Выберите фигуру: \n треугольник - 1\n квадрат -2\n прямоугольник - 3")
if __name__ == "__main__":
    if figure == "1":
        find = Triangle(side_a, side_b, side_c, height)
        print(f"area = {find.triangle_area()}\n perimeter = {find.triangle_perimeter()}")
    elif figure == "2":
        find = Square(side_a)
        print(f"area = {find.square_area()}\n perimeter = {find.square_perimeter()}")
    elif figure == "3":
        find = Rectangle(side_a, side_b)
        print(f"area = {find.rectangle_area()}\n perimeter = {find.rectangle_perimeter()}")


