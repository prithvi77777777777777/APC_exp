class Shape:
    def display_name(self):
        print(type(self).__name__)

class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width): self.length, self.width = length, width
    def area(self): return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height): self.base, self.height = base, height
    def area(self): return 0.5 * self.base * self.height

for shape in (Circle(3), Rectangle(4, 5), Triangle(6, 4)):
    shape.display_name()
    print("Area:", round(shape.area(), 2))
