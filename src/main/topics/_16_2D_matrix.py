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
