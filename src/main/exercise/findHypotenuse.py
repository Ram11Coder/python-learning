# Exercise : find the hypotenuse of right triangle
import math
a = float(input("Enter the value a :"))
b = float(input("Enter the value b :"))

res = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"hypotenuse of ({a} , {b} ) is : {res}")