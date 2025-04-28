
# Super() = Function 	used in a child class to call methods from a parent class(superClass)
# Allows you to extend the functionality of the inherited methods

# Below scenario, we can create a parent class holds the common attributes subclasses

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {self.is_filled}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It is circle with an area of {3.14 * self.radius * self.radius}cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is square with an area of {self.width * self.width}cm^2")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()


circle = Circle("Red", True, radius=5)
square = Square("Blue", True, width=5)
triangle = Triangle("Yellow", True, height=5, width=6)

circle.describe()
square.describe()
triangle.describe()
