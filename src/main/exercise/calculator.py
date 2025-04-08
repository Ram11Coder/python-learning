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
