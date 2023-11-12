import math


# ex1

class Shape:
    def __init__(self, figure):
        self.figure = figure


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Triangle")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


circle = Circle(3)
print(f"Perimeter: {circle.perimeter()}")
print(f"Area: {circle.area()}")

rectangle = Rectangle(10, 5)
print(f"Perimeter: {rectangle.perimeter()}")
print(f"Area: {rectangle.area()}")

triangle = Triangle(2, 3, 4)
print(f"Perimeter: {triangle.perimeter()}")
print(f"Area: {triangle.area()}")
