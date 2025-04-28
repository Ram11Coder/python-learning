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

# Calculator using 2D

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))


for num in num_pad:
    for n in num:
        print(n, end=" ")
    print()

