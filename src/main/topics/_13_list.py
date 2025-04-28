
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