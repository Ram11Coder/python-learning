
# @Decorator = Decorator used to define a method as a property (It can be accessed like an attribute)
# Benefits : Add additional logic when read,write or delete attribute
# Gives you getter, setter and deleter method

# _attribute -> private var
class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")


rectangle = Rectangle(3, 4)

rectangle.height = 5
rectangle.width = 6
print(rectangle.height)
print(rectangle.width)
del rectangle.height
del rectangle.width


# Decorator =  A function that extends the behaviour of another function
# without modifying the base function
# Pass the base function as an argument to the decorator
#
# 	 @add_sprinkles
# ex : get_ice_cream("Vanilla")

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Added sprinkles")
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Added fudge")
        func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"This is your {flavour} ice cream")


get_ice_cream("Vanila")