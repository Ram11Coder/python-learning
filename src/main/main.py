# Day 1 - first program
import string
import time

print("Hello world!")
print('Welcome')

# Data types (String, Integer, float , boolean)

# Strings
name = "Ram"

print(f"Hello {name}")  # String format

# Integer
year = 2025
print(f"Current year : {year}")

# float
pi = 3.14
print(f"Pi value is {pi}")

# boolean
is_Admin = True
print(f"Are you a admin {is_Admin}")
# if
if is_Admin:
    print("You have a admin")
else:
    print("You are not a admin")

# Type casting - converting one data type into another data type
# str(), int(), float(), bool()

print(type(name))
year = str(year)
print(f"Year data type : {type(year)}")

print(bool(name))
print(bool(""))

# input() - A function that prompt the user to enter data and returns the data as string

name = input("What is your name? : ")
age = int(input("What is your age? : "))

age += 1
print(f"Your name is : {name}")
print(f"Your age is : {age}")

# Day 2 : Arithmetic operations

num = 1

num += 1
print(num)
num -= 1
print(num)
num *= 1
print(num)
num /= 1
print(num)
num %= 1
print(num)
num **= 2

print(num)

# math fun

result = round(pi)
print(result)
result = max(4, -23)
print(result)
result = min(4, -23)
print(result)
result = abs(-23)
print(result)
result = pow(4, abs(-2))
print(result)

# math lib

import math

x = int(input("Enter the value of x :"))
print(f"pi value is : {math.pi}")
print(f"e value is : {math.e}")
print(f"floor value of {x} : {math.floor(x)}")
print(f"ceil value of {x} : {math.ceil(x)}")
print(f"sqrt value of {x} : {math.sqrt(x)}")

# Logical operator = evaluate multiple conditions (and, or, not)
# and - both condition must be True
# or - at least one condition must be True
# not - inverts the condition (not False, not True)


# Conditional expression = A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# X if condition else Y

num = 6
print("Positive" if num > 0 else "Negative")
print("EVEN" if num % 2 == 0 else "ODD")

# Useful string methods
print(help(str))
name = input("Enter the name : ")
print(len(name))
print(name.find("r"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.rfind("a"))
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
name = name.replace("a", "b")
print(name)

username = input("Enter the username : ")

if len(username) <= 12 and username.find(" ") == -1 and username.isalpha():
    print(f"{username} statisfy the condition")
else:
    print(f"{username} does not statisfy the condition")

# Indexing = accessing elements of a sequence using [] (Indexing operation)
# [start : end : step]
#
# start : start of index
# end : till the end of index
# step : every step of index will be selected

credit_card = "1234_5678_9012_3456"

print(credit_card[0])
print(credit_card[3])
print(credit_card[0:4])
print(credit_card[::])
print(credit_card[:4])
print(credit_card[:-4])
print(credit_card[-4])
print(credit_card[::2])
print(credit_card[1:6:2])

# reverse a credit card
reversed_cc = credit_card[::-1]
print(f"Reversed credit card : {reversed_cc}")

# Format specifiers = {value:flags} format a value based on what flag are inserted

# .(number)f = round to that many decimal places (fixed point)
# .(number) = allocate that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate the positive values
# := = place  sign to left most position
# : = insert a space before positive numbers
# :, = comma separator


price1 = 1233.34
price2 = -32.34

print(f"Price 1 value : ${price1:.3f}")
print(f"Price 2 value : ${price2:+.2f}")
print(f"Price 1 value : ${price1:10}")
print(f"Price 1 value : ${price1:010}")
print(f"Price 1 value : ${price1:<10}")
print(f"Price 1 value : ${price1:>10}")  # bydefault
print(f"Price 1 value : ${price1:^10}")  # center aligned
print(f"Price 1 value : ${price1:+}")  # positive symbol
print(f"Price 1 value : ${price1: }")  # positive symbol
print(f"Price 1 value : ${price1:,}")
print(f"Price 1 value : ${price1:+,.2f}")

# while loop

# print 0 to entered number

n = int(input("Enter the number : "))
i = 0
while i <= n:
    print(i)
    i += 1

numb = int(input("Enter the input : "))
while True:
    if numb < 0:
        print("Input should be positive, please provide +ve input again :")
        numb = int(input())
    else:
        break

# for loop -> fixed no of iteration

for i in range(0, 6):
    print(i)

# reverse for loop
for x in reversed(range(1, 11)):
    print(x)

print("HAPPY NEW YEAR!")

# dir -> List the different methods in the collection
# print(dir(num))

# help(num)

# collection = single variable to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but add/remove OK. No Duplicates
# Tuple = () ordered and unchangeable
# in -> to check the value in the collection

fruits = ["Apple", "Orange", "Banana"]

for fruit in fruits:
    print(fruit)

print("Orange" in fruits)

fruits[1] = "Grape"
print(fruits[1])
fruits.append("Pineapple")
print(fruits.index("Pineapple"))
fruits.insert(0, "Mango")
fruits.sort()
print(fruits.reverse())
print(fruits)
fruits.clear()
print(fruits)
# fruits.remove("Pineapple")
print(fruits.count("Mango"))

# Set:

colors = {"RED", "ORANGE", "GREEN"}

# print(colors[0]) throws error because it is unordered
print("YELLOW" in colors)
colors.add("GREEN")
colors.add("PINK")

for color in colors:
    print(color)
print(len(colors))
colors.remove("PINK")
colors.pop()
print(colors)
colors.clear()

# Tuple

days = ("MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY")

# tuple' object does not support item assignment
# days[0] ="MOONDAY"
print(days)
print(days.count("MONDAY"))
print(days.index("WEDNESDAY"))

# 2 Dimension(Matrix)

fruits = ["Apple", "Orange", "Grape"]
vegetables = ["Carrot", "Brinjal", "Radish"]
meats = ["Chicken", "Lamb", "Fish"]

groceries = [fruits, vegetables, meats]
print(groceries)
print(groceries[1][1])

for grocery in groceries:
    for food in grocery:
        print(food, end=" ")
    print()

# Dictionary : a collection of {key:value} pairs
#              ordered and changeable. NO Duplicates

states_capital = {"TamilNadu": "Chennai",
                  "Karnataka": "Bangalore",
                  "Kerala": "Trivandrum"}

print(states_capital)
print(states_capital.get("TamilNadu"))

states_capital.update({"UP": "Lucknow"})
state = "MP"
print(states_capital.get(state))
if states_capital.get(state):
    print(states_capital.get(state))
else:
    print(f"{state} state not available in dict")

states_capital.pop("UP")
states_capital.popitem()
# states_capital.clear()

for states in states_capital:
    print(states)

keys = states_capital.keys()
print(keys)

for key in keys:
    print(key)

print(states_capital.values())

for val in states_capital.values():
    print(val)

items = states_capital.items()  # [(),(),()]
print(items)

for k, v in states_capital.items():
    print(f"{k} : {v}")

# Random

import random

low = 1
high = 100
print(random.randint(low, high))
options = ["rock", "paper", "scissor"]

option = random.choice(options)
print(option)

print(random.random())

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "A", "K", "Q"]
random.shuffle(cards)
print(cards)


# function = A block of reusable code
#            place () after the function name to invoke it


def call_me(name):
    print(f"Hey! call me as {name}")


call_me("Rocky")


# return = statement used to end a function and send a result back to caller


def second_max(li):
    li = list(set(li))
    li.sort(reverse=True)
    return li[1]


arg = [3, 2, 1, 6, 3, 6]
print(second_max(arg))


# Default argument = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces no of arguments
#                    1. Positional, 2.Default, 3. Keyword, 4. arbitrary

def net_price(price, discount=0, tax=0.05):
    return price * (1 - discount) * (1 + tax)


print(net_price(500, 0.1))
print(net_price(500))


def time_counter(end, start=0):  # default argument preceed with non-default argument
    for i in range(start, end):
        time.sleep(1)
        print(i)


time_counter(2)


# Keyword argument - an argument preceded by an identifier, helps with readability
# order of argument doesn't matter

def greeting(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")


greeting("Hello", first="Rocky", title="Mr.", last="Bhai")

# inbuilt func have keyword arg
print("1", "2", "3", sep="-")

# Arbitrary arg = Varying amount of arguments,
# we are not sure about how many arg user gonna pass in while invoking the function
# *args = allow you to pass multiple non-key arguments (tuple)
# **kwargs = allow you to pass multiple keyword-arguments (dict)
# * unpacking operator
# * operator unpacks an iterable (like a list, tuple, or string), spreading out its elements.
#

# Ex of unpacking list

nums = [1, 3, 4, 5, 6]
print(nums)
print(*nums)

a = [1, 2]
b = [3, 4]
merge_list = [a, b]
merge_value = [*a, *b]
print(merge_list)
print(merge_value)


def print_name(*args):
    print(*args, end=" ")


print_name("Mr.", "Rocky", "Bhai")
print()


# The ** operator unpacks a dictionary, spreading out its key-value pairs.
# You're passing a dictionary as named arguments to a function.
#
# You want to merge dictionaries.
#
# You want a flexible function that accepts any keyword arguments.


def print_address(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} : {v}")


print_address(street="Vivekanandha Street", dist="Chennai", state="TN", pin="123456")

# Iterables = An object/collection that can return its element one at a time,
# allowing it to be iterated over in a loop
# ex: list,set,tuple,dict,string

# Membership operator : used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, dict)
#                       1. in
#                       2. not in


fruit = "APPLE"
ch = input("Enter a character : ")
if ch in fruit:
    print(f"{ch} is present in {fruit}")
else:
    print(f"{ch} is not present in {fruit}")

grade_dict = {"Ram": "A", "Raju": "C", "Rocky": "F", "Revi": "B"}

student = input("Enter the student to get grade details : ")

if student in grade_dict:
    print(f"{student} grade is : {grade_dict[student]}")
else:
    print(f"{student} is not present")

# list comprehension = A concise way to create lists in python
#                     compact and easier to read than traditional loops
# syntax: [expression for value in iterable if condition]

triples = [x * 3 for x in range(0, 11)]
print(triples)

numbers = [1, -2, 3, -4, 5, -6]
print([num for num in numbers if num > 0])


# Match-case statement (switch)= An alternative to using many elif statements
# Execute some code if a value matche 'case'
# Benefits : cleaner and syntax is more readable
# case - => wildcard


def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wednesday"
        case 5:
            return "It's Thursday"
        case 6:
            return "It's Friday"
        case 7:
            return "It's Saturday"
        case _:
            return "It's not valid day"


print(day_of_week(1))
print(day_of_week("Pizza"))

# Module = a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own)
# useful to break up a large program reusable separate files

# print(help("modules"))

# import math
import math as m

print(m.pi)
from math import pi

print(pi)

import math_module as mm

print(mm.pi)
print(mm.sq(10))


# variable scope : Where a variable is visible and accessible
# scope resolution : (LEGB) Local -> Enclosed -> Global -> Built-in

# local
def func():
    x = 1
    print(x)


func()


# enclosed
def func1():
    x = 2

    def func2():
        print(x)

    func2()


func1()

# Global - outside of any func()
x = 3


def func3():
    print(x)


func3()

from math import e

print(e)

# if __name__ = __main__: (this script can be imported or run standalone)
# Functions and classes in this module can be reused without the main block of code executing
# Good practise (code is modular,
# helps readability, leaves no global variables, avoid unintended execution)
#
# ex : Library = import lib for functionality
# when running lib directly, display a help page
# In Python, every module has a built-in variable called __name__:
# If the file is being run directly, __name__ == "__main__"
# If the file is being imported, __name__ == "module_name"
#  Why is this useful?
# To separate logic: Keeps function definitions separate from runtime behavior.
# To prevent side effects when importing code.
# To support reusability and testing: You can import functions without accidentally running the whole script.

print(__name__)


def main():
    print("inside main : ")


if __name__ == '__main__':
    main()
import other_module

# Python OOPS
# object = A "bundle" of related attributes(variables) and methods (functions)
#          Ex: Phone, cup, book
#          You need a "class" to create many objects
# class = A blueprint used to design the structure and layout of an object

# dunder method = double underscore method
# constrcutor (__init__(self))

# instance var - defined inside the constructor
from car import Car

car1 = Car("BMW", 2024, "Black", False)
print(car1.num_of_cars)
car2 = Car("Jaguar", 2025, "White", True)
car3 = Car("Audi", 2024, "Yellow", False)

car1.describe()
car1.drive()
car1.stop()

# class var = shared among all instances of class
#               Define outside the constructor
#               Allow you to share data among all objects created from that class


print(car1.num_of_cars)
# Class variable directly access from Class
print(Car.num_of_cars)


# Inheritance = Allow a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               ex: class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} : WOOF!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} : MEOW!")


class Mouse(Animal):
    def speak(self):
        print(f"{self.name} : SQUEEK!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Cherry")
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

dog.speak()
cat.speak()
mouse.speak()


# Multiple inheritance = Inherit from more than one parent class
# 						Ex: C(A,B)
# Multilevel Inheritancce = Inherit from the parent which inherit from another parent
# 						Ex: C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

    def alive(self):
        print(f"Prey {self.name} is alive")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

    def alive(self):
        print(f"Predator {self.name} is alive")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


class Fish(Predator, Prey):
    pass


rabbit = Rabbit("Tony")
rabbit.flee()
rabbit.eat()
rabbit.sleep()

hawk = Hawk("Hawky")
hawk.eat()
hawk.sleep()
hawk.hunt()

fish = Fish("Nemo")
fish.eat()
fish.sleep()
fish.flee()
fish.hunt()
fish.alive()


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

#   Polymorphism = Greek word that means to "have many forms or faces"
#			   Poly = Many
#			   Morph = Form
#
#			   Two ways to acheive polymorphism
#   		   1. Inheritancce = An object could be treated of the same type as a parent class
#			   2. Duck typing = Object must have necessary attributes/methods


from abc import ABC, abstractmethod


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

# Duck typing = Another way to achieve polymorphism besides inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck"

class Duck:
    def quack(self):
        print("Quack!")

    def swim(self):
        print("Swimming like a duck 🦆")


class Person:
    def quack(self):
        print("I'm imitating a duck!")

    def swim(self):
        print("I'm swimming... cautiously.")


def in_pond(thing):
    # We only care if 'thing' can quack() and swim(), not its type
    thing.quack()
    thing.swim()


donald = Duck()
alice = Person()

in_pond(donald)  # Quack! / Swimming like a duck 🦆
in_pond(alice)  # I'm imitating a duck! / I'm swimming... cautiously.


# Static methods = A method that belong to a class rather than any object from that class(instance) usually used for general utility functions
#
# Instance methods = Best for operations on instance of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    # Instance method
    def emp_details(self):
        return f"{self.name} = {self.position}"

    # Static method
    @staticmethod
    def is_valid_job_position(position):
        job_positions = ["Developer", "Tester", "Manager"]
        return position in job_positions


print(Employee.is_valid_job_position("Manager"))
print(Employee.is_valid_job_position("Architect"))

emp1 = Employee("Ram", "Developer")
emp2 = Employee("Rocky", "Tester")

print(emp1.emp_details())
print(emp2.emp_details())
print(emp1.is_valid_job_position("Tester"))


# Class Method = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself
# Best for class-level data or require access to the class itself

class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # instance method
    def get_info(self):
        print(f"{self.name} = {self.gpa}")

    @classmethod
    def get_count(cls):
        print(f"Total student count : {cls.count}")

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa of total students : {cls.total_gpa / cls.count:.2f}"


student1 = Student("David", 3.4)
student2 = Student("Vikram", 2.5)
student3 = Student("Manoj", 2.4)

student1.get_info()
student2.get_info()
student3.get_info()

print(Student.get_average_gpa())
Student.get_count()


# Magic methods = Dunder methods (double underscore) __init__, __Str__, __eq__
# They are automatically called by many of pythons built-in operations.
# They allow developers to define or customize the behaviour of objects


class Book:

    # constructor
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    def __getitem__(self, item):
        if item == 'title':
            return self.title
        elif item == 'author':
            return self.author
        elif item == 'num_pages':
            return self.num_pages
        else:
            return f"Key {item} was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 297)
book3 = Book("The Lion, the witch and the Wardrobe", "C.S. Lewis", 197)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 310)
print(book1)
print(book1 == book4)
print(book1 > book2)
print(book1 < book3)
print(book1 + book3)
print("Lion" in book3)
print(book1['title'])


# @Decorator = Decorator used to define a method as a property (It can be accessed like an attribute)
# Benefits : Add additional logic when read,write or delete attribute
# Gives you getter, setter and deleter method

# _attribure -> private var
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

# exception = An event that interrupt the flow of a program
# (ZeroDivisionError,TypeError,ValueError)
# 1. try, 2. expect, 3. finally

try:
    num = int(input("Enter the number : "))
    print(1 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("input should be numeric value")
except Exception:
    print("Something went wrong!")
finally:
    print("Clean up activity ")

# python file detection

import os

# Relative file path :exercise\test.txt
#  Absolute file path : C:\Users\intel\PycharmProjects\python-learning\src\main\exercise\test.txt
file_path = "exercise\\test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' is exist!")
    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a folder")
else:
    print("The location does not exist")

# File writing (.txt, .json, .csv)

txt_data = "I like pizza!"
file_path = "output.txt"

# using with -> it automatically file also
# open parameter return the file object
with open(file=file_path, mode='w') as file:
    file.write(txt_data)
    print(f"txt file {file_path} was created")

# mode (x) - create a file if not exists, if it already exists then throes FileExistsError exception
# mode (r) - read the file
# mode (a) - append the file
# mode (w) - It will override the file

import json

employee = {
    "name": "Rocky",
    "age": 27,
    "Job": "Developer"
}
json_file_path = "emp.json"
try:
    with open(file=json_file_path, mode='x') as file:
        json.dump(employee, file, indent=4)
        print(f"json file {json_file_path} was created")
except FileExistsError:
    print("The file already exist")

import csv

employee_list = [["Name", "Age", "Job"],
                 ["Ram", 27, "Senior developer"],
                 ["Vicky", 28, "Senior UI developer"],
                 ["Siva", 30, "Tester"], ]
csv_file_path = "emp.csv"
try:
    with open(file=csv_file_path, mode='w', newline="") as file:
        writer = csv.writer(file)
        for row in employee_list:
            writer.writerow(row)
        print(f"csv file {csv_file_path} was created")
except FileExistsError:
    print("The file already exist")

# file reading

# text file read
try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have read permission for that file')

# Json file read
try:
    with open(json_file_path, 'r') as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have read permission for that file')

# Json file read
try:
    with open(csv_file_path, 'r') as file:
        for line in csv.reader(file):
            print(line)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print('You do not have read permission for that file')

# datetime modules

import datetime

print(datetime.date.today())

date = datetime.date(2025, 4, 23)
print(f"date : {date}")

time = datetime.time(10, 4, 23)
print(f"time : {time}")
now = datetime.datetime.now()
print(now)
modifed_date_time = now.strftime("%H:%M:%S %d-%m-%Y")
print(modifed_date_time)

target_date_time = datetime.datetime(2030, 1, 1, 1, 1, 1)

if target_date_time < now:
    print("Target date has passed")
else:
    print("Target date has not passed")


# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)


import threading
import time


def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")

def read_book():
    time.sleep(2)
    print(f"You finish reading book")

def send_mail():
    time.sleep(4)
    print(f"You finish sending mail")

chore1 =threading.Thread(target=walk_dog,args=("Scooby",)) # if it is only one arg then we need to end with , then python consider as tuple
chore1.start()

chore2 = threading.Thread(target=read_book)
chore2.start()

chore3 = threading.Thread(target=send_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("All chores are completed!")


# Fetch API response
import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokeman = "pikachu"

pokeman_info = pokemon_info(pokeman)
if pokeman_info:
    print(pokeman_info["name"].capitalize())
    print(pokeman_info["id"])
