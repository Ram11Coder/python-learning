
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