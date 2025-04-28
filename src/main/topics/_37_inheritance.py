
# Polymorphism = Greek word that means to "have many forms or faces"
#			   Poly = Many
#			   Morph = Form
#
#			   Two ways to acheive polymorphism
#   		   1. Inheritance = An object could be treated of the same type as a parent class
#			   2. Duck typing = Object must have necessary attributes/methods

from  math import pi
from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, height):
        self.height = height

    def area(self):
        return self.height ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping


shapes = [Circle(4), Square(5), Triangle(3, 4), Pizza(topping="pepperoni", radius=15)]

for shape in shapes:
    print(f"Area is : {shape.area():.2f}/cm2")


# pizza consider 3 forms (Pizza,Circle,Shape)