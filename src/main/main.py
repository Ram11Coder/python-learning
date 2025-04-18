# Day 1 - first program
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
