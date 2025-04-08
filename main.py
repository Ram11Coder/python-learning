# Day 1 - first program
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

# Excercise : Shopping cart program

food = input("What would you like to order? : ")
price = float(input("What is the price of food?:"))
quantity = int(input("What is the quantity of order?:"))
print(f"Total bill of ordered {food}/s : ${price * quantity}")

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

# Exercise : find the circumference of circle
radius = float(input("Enter the radius of circle : "))
circumference = 2 * math.pi * radius
print(f"Circumference value is : {round(circumference, 2)}")

# Excercise : Area of the circle
area = math.pi * pow(radius, 2)
print(f"Area value is : {round(area, 2)}")

# Exercise : find the hypotenuse of right triangle

a = float(input("Enter the value a :"))
b = float(input("Enter the value b :"))

res = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"result is : {res}")

# Exercise : calculator

operator = input("Enter the operator (+,-,*,/)")
num1 = float(input("Enter the humber 1 : "))
num2 = float(input("Enter the humber 2 : "))

if operator == "+":
    print(round(num1 + num2, 2))
elif operator == "-":
    print(round(num1 - num2, 2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))
else:
    print(f"Enter the operator {operator} is not valid")
