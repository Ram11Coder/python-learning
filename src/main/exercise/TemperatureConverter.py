# Temp converter
unit = input("Enter the temperature in Fahrenheit/Celsius (F/C) : ")
temp = float(input("Enter the temperature : "))

if unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temperature in celsius {temp}")
elif unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit {temp}")
else:
    print(f"{unit} is invalid unit of measurement")
