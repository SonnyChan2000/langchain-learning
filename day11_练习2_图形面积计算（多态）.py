class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius

def print_shape_info(shape):
    print(f"面积: {shape.area():.1f}, 周长: {shape.perimeter():.1f}")

r = Rectangle(4, 5)
c = Circle(3)
print_shape_info(r)
print_shape_info(c)