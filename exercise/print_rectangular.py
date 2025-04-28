# Rectangular pattern printing using *


length = int(input("Enter the length of rectangular : "))
width = int(input("Enter the width of rectangular : "))

for x in range(width):
    for y in range(length):
        print("*", end=" ") # end used to replace new line(\n) with space
    print()
