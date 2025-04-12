# Excercise : Shopping cart program

# food = input("What would you like to order? : ")
# price = float(input("What is the price of food?:"))
# quantity = int(input("What is the quantity of order?:"))
# print(f"Total bill of ordered {food}/s : ${price * quantity}")

# Using loop and collection

foods = []
prices = []
total = 0

while True:
    food = input("Enter the food (Q/q to quit) : ")
    if food.lower() == 'q':
        break;
    else:
        price = float(input(f"Enter the price of a {food} : $"))
        foods.append(food)
        prices.append(price)

for price in prices:
    total += price

print("----- YOUR CART -----")
for food in foods:
    print(food, end=" ")
print()
print(f"Total price of foods = ${total}")